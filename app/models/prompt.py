from pydantic import BaseModel, Field

class PromptBuildRequest(BaseModel):
    scenario: str = Field(..., min_length=1)
    context: str = Field(..., min_length=1)

class PromptBuildResponse(BaseModel):
    prompt: str
