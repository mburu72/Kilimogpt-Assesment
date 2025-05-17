from fastapi import APIRouter, HTTPException, Depends, Header
from app.models.db import engine
from app.models.models import QuestionRequest, AnswerResponse, Chat
from sqlmodel import Session, select
from app.services import llm_service

router = APIRouter()
def get_session():
    with Session(engine) as session:
        yield session

@router.post("/ask", response_model=AnswerResponse)
async def ask_question(payload: QuestionRequest,
                       session: Session = Depends(get_session),
                       session_id: str = Header(None, alias="X-Session-Id")):
   if not session_id:
       raise HTTPException(status_code=400, detail="Missing session id")

   answer = llm_service.ask_gpt(question_asked=payload.question)
   chat = Chat(question = payload.question, answer = answer, session_id=session_id)
   session.add(chat)
   session.commit()
   return AnswerResponse(
        question=payload.question,
        answer= answer
    )

@router.get("/history", response_model=list[AnswerResponse])
def get_chat_history(session: Session = Depends(get_session), session_id: str=Header(None, alias="X-Session-Id")):
    if not session_id:
        raise HTTPException(status_code=400, detail="Missing session Id")
    chats = session.exec(select(Chat).where(Chat.session_id == session_id)).all()
    return chats

@app.get("/health")
async def health_check():
    return {"status": "ok"}