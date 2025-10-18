from sqlalchemy.orm import Session
from models.chat import Chat
from models.session import Session as ChatSession  
from database import SessionLocal
from services import workflow_service
import openai
import os

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def create_chat(session_id: str, message: str):
    """
    Create a chat message, ensure session exists,
    get LLM response, and save both to DB.
    """
    db = SessionLocal()
    try:
        session = db.query(ChatSession).filter(ChatSession.id == session_id).first()
        if not session:
            session = ChatSession(id=session_id, name=f"Chat {session_id}")
            db.add(session)
            db.commit()
            db.refresh(session)

        policy_text = workflow_service.get_workflow_policy()

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": f"You are a helpful customer support agent. Follow this workflow policy strictly:\n{policy_text}"
                    },
                    {"role": "user", "content": message},
                ],
                max_tokens=500,
            )
            reply = response.choices[0].message.content

        except Exception as e:
            reply = f"LLM Error: {str(e)}"

        chat = Chat(session_id=session.id, message=message, response=reply)
        db.add(chat)
        db.commit()
        db.refresh(chat)
        
        return {
            "id": chat.id,
            "session_id": chat.session_id,
            "message": chat.message,
            "response": chat.response
        }
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()


def get_chats(session_id: str):
    """
    Retrieve all chats for a session from the database.
    """
    db = SessionLocal()
    try:
        chats = db.query(Chat).filter(Chat.session_id == session_id).all()
        return [
            {
                "id": chat.id,
                "session_id": chat.session_id,
                "message": chat.message,
                "response": chat.response
            }
            for chat in chats
        ]
    finally:
        db.close()
