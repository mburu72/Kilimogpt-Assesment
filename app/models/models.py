from pydantic import BaseModel, Field
from sqlmodel import SQLModel, Field
from typing import Optional

class QuestionRequest(BaseModel):
    question: str = Field(..., min_length=3)
class AnswerResponse(BaseModel):
    question: str
    answer: str

class Chat(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    question: str
    answer: str
    session_id: str
