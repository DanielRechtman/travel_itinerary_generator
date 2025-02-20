from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Mount static files like CSS
app.mount("/app/static", StaticFiles(directory="app/static"), name="static")
# Set up templates for HTML rendering
templates = Jinja2Templates(directory="app/templates")

# Route for the homepage
@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
