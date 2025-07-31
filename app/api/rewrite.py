from fastapi import APIRouter, Depends, HTTPException
from app.models.rewrite import RewriteRequest, RewriteResponse
from app.core.security import verify_api_key
from app.core.config import OPENAI_API_KEY, OPENAI_MODEL
import openai

openai.api_key = OPENAI_API_KEY

router = APIRouter()

@router.post("/rewrite", response_model=RewriteResponse)
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
