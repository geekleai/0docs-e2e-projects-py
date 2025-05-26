from fastapi import FastAPI
from app.routers import customers, leads, opportunities, contacts, dashboard

app = FastAPI()

# Include all routers
app.include_router(customers.router)
app.include_router(leads.router)
app.include_router(opportunities.router)
app.include_router(contacts.router)
app.include_router(dashboard.router)

@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Welcome to the CRM API"}

@app.get("/about")
def about() -> dict[str, str]:
    return {"message": "This is the CRM application API."}