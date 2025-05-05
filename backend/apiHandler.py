import requests
from config import WHOIS_API_KEY

WHOIS_API_URL = "https://www.whoisxmlapi.com/whoisserver/WhoisService"

def call_whois_api(formatted_req: dict):
    """ 
        Calls the WHOIS API with error handling 
        Add Rate limiting, if needed
    """
    params = {
        "apiKey": WHOIS_API_KEY,
        "domainName": formatted_req["domain"],
        "outputFormat": "json"
    }
    try:
        response = requests.get(WHOIS_API_URL, params=params, timeout=10)  # Timeout added
        response.raise_for_status()  # Raises exception for 4xx, 5xx errors

        jsonResponse = response.json()

        if jsonResponse.get("ErrorMessage") != None:
            return {
                "status_code": 400,
                "message": "API Error, Please request in proper format. " + jsonResponse.get("ErrorMessage", {}).get("msg"),
                "data": None
            }

        if (jsonResponse.get("WhoisRecord", {}).get("domainAvailability") == "AVAILABLE" 
            or jsonResponse.get("WhoisRecord", {}).get("dataError") == "MISSING_WHOIS_DATA"):
            return {
                "status_code": 400,
                "message": "Domain Details Not Found",
                "data": None
            }
        
        if jsonResponse.get("WhoisRecord") is None:
            return {
                "status_code": 400,
                "message": "API Error, Please Check Request",
                "data": None
            }
        
        return {
            "status_code": 200,
            "message": "Response Fetched from API",
            "data": jsonResponse
        }

    except requests.exceptions.Timeout:
        return {
            "status_code": 408,
            "message": "Request to WHOIS API timed out. Please try again."
        }

    except requests.exceptions.RequestException:
        return {
            "status_code": 500,
            "message": "An error occurred while fetching WHOIS API data. Please try again."
        }