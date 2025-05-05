# Getting Started with TLV Project [Frontend + Backend]

This project was bootstrapped with 
[Create React App](https://github.com/facebook/create-react-app) and 
[Fast api Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)

# Project Overview
- Frontend: React, Material UI, Axios
- Backend: FastAPI, Uvicorn, Gunicorn

# Installation and Setup

## Frontend
go to /frontend directory, and run 

## Install Dependencies `npm install`

### Start Development Server `npm start`
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

### Build for production `npm run build`
Builds the app for production to the `build` folder.\

### Serve Prod Locally
    npm install -g serve
    serve -s build


## Frontend
go to /frontend directory, and run 

## Install Dependencies `npm install`

### Start Development Server `npm start`
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

### Build for production `npm run build`
Builds the app for production to the `build` folder.\

### Serve Locally
    npm install -g serve
    serve -s build

## Backend
go to /backend directory, and run

## Install Dependencies `pip install -r requirements.txt`

### Start Development Server `uvicorn main:app --host 127.0.0.1 --port 8000`
Runs the backend in the development mode.\
Open [http://localhost:8000](http://localhost:8000) to view it in your browser.

### Prod Mode: `uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4` 
    pip install gunicorn uvicorn
    gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:8000

