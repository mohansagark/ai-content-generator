from pydantic import BaseModel, Field

class RewriteRequest(BaseModel):
    content: str = Field(..., min_length=1)
    scenario: str = Field(..., min_length=1)

class RewriteResponse(BaseModel):
    rewritten_content: str
