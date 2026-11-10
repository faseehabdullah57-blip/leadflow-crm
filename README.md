# LeadFlow AI CRM

AI-powered Customer Relationship Management and Business Automation platform.

## Project Objective

LeadFlow aims to help businesses capture, manage, qualify and follow up with customer leads through a centralised CRM system.

## Technology Stack

- Python 3.11
- FastAPI
- Uvicorn
- Pydantic
- Git and GitHub

## Current Features

- FastAPI application foundation
- Health-check API endpoint
- Automatic Swagger API documentation
- OpenAPI schema generation

## Planned Features

- Lead creation and management
- PostgreSQL database integration
- Customer authentication and authorisation
- Webhook integrations
- n8n workflow automation
- AI-powered lead qualification
- AI assistant and knowledge retrieval
- Human approval workflows
- CRM dashboard
- Automated testing
- Docker deployment

## Project Structure

```text
leadflow-crm/
├── app/
│   ├── __init__.py
│   └── main.py
├── .gitignore
├── requirements.txt
└── README.md

## Installation

Create a Python virtual environment:

```powershell
py -3.11 -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

## Run the Application

```powershell
python -m uvicorn app.main:app --reload
```

## API Documentation

- Health Check: http://127.0.0.1:8000/health
- Swagger UI: http://127.0.0.1:8000/docs
- OpenAPI Schema: http://127.0.0.1:8000/openapi.json

## Learning Project

This project is being developed as part of an AI Automation and CRM Engineering apprenticeship.

The objective is to demonstrate practical backend development, API engineering, database integration, AI integration, workflow automation and software engineering practices.

## Project Status

Currently: Initial FastAPI backend foundation completed.

More features will be implemented progressively.


