"""
LeisureLytics — Marketing Website
=================================
A modern FastAPI application serving the marketing site for LeisureLytics,
a forecasting, workforce planning, and revenue management platform for leisure businesses.

Run with:
    uvicorn main:app --reload

Then visit http://127.0.0.1:8000
"""

from pathlib import Path

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# ---------------------------------------------------------------------------
# App setup
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(
    title="LeisureLytics",
    description="Forecasting, workforce planning, and revenue management for leisure businesses.",
    version="1.0.0",
)

# Mount static files (CSS, images, JS, etc.)
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

# Jinja2 template directory
templates = Jinja2Templates(directory=BASE_DIR / "templates")


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Landing page — hero, features, CTA."""
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    """About page — mission, delivery model, and leadership team."""
    return templates.TemplateResponse("about.html", {"request": request})


@app.get("/origin-story", response_class=HTMLResponse)
async def origin_story(request: Request):
    """Origin story page — senior-led agentic engineering model."""
    return templates.TemplateResponse("origin_story.html", {"request": request})


@app.get("/revenue-management-engine", response_class=HTMLResponse)
async def revenue_management_engine(request: Request):
    """Revenue management page — high-level overview of the full engine."""
    return templates.TemplateResponse("revenue_management_engine.html", {"request": request})


@app.get("/workforce-planning-agent", response_class=HTMLResponse)
async def workforce_planning_agent(request: Request):
    """Workforce planning page — business-focused planning agent overview."""
    return templates.TemplateResponse("workforce_planning_agent.html", {"request": request})


@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    """Contact page — enquiry form."""
    return templates.TemplateResponse("contact.html", {"request": request, "submitted": False})


@app.post("/contact", response_class=HTMLResponse)
async def contact_submit(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    message: str = Form(...),
):
    """Handle contact form submission (demo — just re‑renders with a thank‑you)."""
    # In production you'd persist or email this. For now, acknowledge receipt.
    return templates.TemplateResponse(
        "contact.html",
        {
            "request": request,
            "submitted": True,
            "form_name": name,
            "form_email": email,
            "form_message": message,
        },
    )
