from fastapi import FastAPI, HTTPException
from routes.user import user

app = FastAPI()

app.include_router(user)