from fastapi import FastAPI
from models import MsgPayload
from routers import messages, users, analytics

app = FastAPI()

# Include all routers
app.include_router(messages.router)
app.include_router(users.router)
app.include_router(analytics.router)

# Remove the duplicated routes and keep only the general ones
@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Hello"}


@app.get("/about")
def about() -> dict[str, str]:
    return {"message": "This is the about page."}
