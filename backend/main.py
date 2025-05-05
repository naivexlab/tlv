from fastapi import FastAPI
from fastapi.responses import JSONResponse
from apiHandler import call_whois_api
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/search")
async def getWhoIsData(domain: str, data_type: str):
    """
    :param domain: The domain name to look up
    :param data_type: Requested data type - contactInfo, domainInfo
    :return: JSON response with the requested Whois data
    """
    try:
        formatted_req = format_request(domain, data_type)  # Step 1: Format request
        validation_error = validate_request(formatted_req)  # Step 2: Validate request
        if validation_error:
            return JSONResponse(status_code=400, content={
                "status": "fail",
                "message": validation_error.get("message"), # Return validation error response
            })
        
        api_response = call_whois_api(formatted_req)

        if api_response.get("status_code") != 200:
            return JSONResponse(status_code=api_response.get("status_code"), content={
                "status": "fail",
                "message": api_response.get("message"),
            })

        formatted_res = format_response(formatted_req, api_response.get("data"))

        return JSONResponse(status_code=formatted_res.get("status_code"), content={
            "status": formatted_res.get("status"),
            "message": formatted_res.get("message"),
            "data": formatted_res.get("data"),
        })

    except Exception as e:
        return JSONResponse(status_code=500, content={"status": "fail", "message" : "Server Error"})


def format_request(domain: str, data_type: str):
    domain = domain.lower().lstrip("www.").split('/')[0]
    data_type = data_type.lower()
    return {"domain": domain, "data_type": data_type}


def validate_request(formatted_req: dict):
    """ Validates domain and data_type, returning structured JSON response on failure """
    domain = formatted_req["domain"]
    data_type = formatted_req["data_type"]

    if data_type not in ["domain_info", "contact_info"]:
        return {"status": "fail", "message": "Invalid data type. Choose 'domain_info' or 'contact_info'."}

    return None  # No validation errors


def format_response(formatted_req, api_data):
    """
    Handle different types of data type responses, polish the response accordingly
    """

    whois_data = api_data.get("WhoisRecord", {}) 

    if formatted_req["data_type"] == "domain_info":
        return {
            "status_code": 200,
            "status": "success",
            "message": "Domain Info Fetched Successfully",
            "data": {
                "domainName": whois_data.get("domainName"),
                "registrar": whois_data.get("registrarName"),
                "registrationDate": whois_data.get("createdDateNormalized"),
                "expirationDate": whois_data.get("expiresDateNormalized"),
                "estimatedDomainAge": whois_data.get("estimatedDomainAge"),
                "hostnames": ", ".join(whois_data.get("nameServers", {}).get("hostNames", []))[:25],
            }
        }

    elif formatted_req["data_type"] == "contact_info":
        return {
            "status_code": 200,
            "status": "success",
            "message": "Contact Info Fetched Successfully",
            "data": {
                "registrantName": whois_data.get("registrant", {}).get("name") 
                                    or whois_data.get("registrant", {}).get("organization"),
                "technicalContactName": whois_data.get("technicalContact", {}).get("name")
                                        or whois_data.get("technicalContact", {}).get("organization"),
                "administrativeContactName": whois_data.get("administrativeContact", {}).get("name")
                                                or whois_data.get("administrativeContact", {}).get("organization"),
                "contactEmail": whois_data.get("contactEmail"),
            }
        }

    return {
        "status_code": 400,
        "status": "fail",
        "message": "Invalid data type provided. Use 'domain_info' or 'contact_info'.",
        "data": None
    }