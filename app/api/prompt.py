from fastapi import APIRouter, Depends
from app.models.prompt import PromptBuildRequest, PromptBuildResponse
from app.core.security import verify_api_key

router = APIRouter()

@router.post("/build-prompt", response_model=PromptBuildResponse)
def build_prompt(request: PromptBuildRequest, _: None = Depends(verify_api_key)):
    prompt = (
        f"You are an expert AI assistant. Your task is to generate content based on the following scenario and context.\n\n"
        f"Scenario: {request.scenario}\n"
        f"Context: {request.context}\n\n"
        f"Please generate a detailed, high-quality response that fits the scenario and context above."
    )
    return PromptBuildResponse(prompt=prompt)
