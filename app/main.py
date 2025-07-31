from fastapi import FastAPI
from app.api import prompt, rewrite

app = FastAPI()

app.include_router(prompt.router)
app.include_router(rewrite.router)
