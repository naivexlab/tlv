## Getting Started with TLV Project [Frontend + Backend]

This project was bootstrapped with 
[Create React App](https://github.com/facebook/create-react-app) and 
[Fast api Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)

## Project Overview
- Frontend: React, Material UI, Axios
- Backend: FastAPI, Uvicorn, Gunicorn

## Installation and Setup

- ADD `WHOIS_API_KEY` environment variable or directly paste in `/backend/config.py` file

### Quick Run
```
bash /backend/restart.sh
bash /frontend/restart.sh
```

## Development

#### Frontend
```
cd frontend
npm install
npm start
```

Open [http://localhost:3000](http://localhost:3000) to view it in your browser.


#### Backend
```
cd backend
pip install -r requirements.txt
uvicorn main:app --host 127.0.0.1 --port 8000
```

Open [http://localhost:8000](http://localhost:8000) to view it in your browser.



## Prod

#### Frontend Build
```
npm run build
```

#### Frontend Serve Prod Locally
```
npm install -g serve
serve -s build
```

#### Backend Prod Mode
```
pip install gunicorn uvicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:8000
```
`
