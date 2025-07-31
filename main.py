import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request, status, Depends
from pydantic import BaseModel, Field
import openai



load_dotenv()
app = FastAPI()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
API_KEY = os.getenv("API_KEY")


if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY environment variable not set.")
if not API_KEY:
    raise RuntimeError("API_KEY environment variable not set.")

openai.api_key = OPENAI_API_KEY

class RewriteRequest(BaseModel):
    content: str = Field(..., min_length=1)
    scenario: str = Field(..., min_length=1)

class RewriteResponse(BaseModel):
    rewritten_content: str

def verify_api_key(request: Request):
    api_key = request.headers.get("x-api-key")
    if api_key != API_KEY:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or missing API key")

@app.post("/rewrite", response_model=RewriteResponse)
def rewrite_content(request: RewriteRequest, _: None = Depends(verify_api_key)):
    prompt = (
        f"Rewrite the following content in this scenario: {request.scenario}\n\n"
        f"Content:\n{request.content}"
    )
    try:
        response = openai.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that rewrites content as instructed."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=512,
            temperature=0.7
        )
        content = response.choices[0].message.content
        if content is not None:
            rewritten = content.strip()
        else:
            rewritten = ""
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Error contacting OpenAI API: {str(e)}")

    return RewriteResponse(rewritten_content=rewritten)
