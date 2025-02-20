# FastAPI HTMX Project

This is a starter workspace for a FastAPI project integrated with HTMX and containerized using Docker.

## Project Structure

```
C:\Users\danny\travel_company/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── style.css
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```



## Getting Started

### Using Docker

1. Build and run the container:
   docker-compose up --build

2. Access the application:
   Open your browser and navigate to http://localhost:8000

### Without Docker

1. Install dependencies:
   pip install -r requirements.txt

2. Run the application:
   uvicorn app.main:app --reload

3. Access the application:
   Open your browser and navigate to http://localhost:8000

## About

This project is a minimal starter template that integrates FastAPI with HTMX for dynamic web interactions and is set up for Docker deployment. Customize and expand upon this template as needed.
