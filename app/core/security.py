from fastapi import Request, HTTPException, status, Depends
from .config import API_KEY

def verify_api_key(request: Request):
    api_key = request.headers.get("x-api-key")
    if api_key != API_KEY:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or missing API key")
