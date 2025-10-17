from sqlalchemy.orm import Session
from models.chat import Chat
from database import SessionLocal
from services import workflow_service
import openai
import os

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def create_chat(session_id: str, message: str):
    """
    Create a chat message, get the LLM response (from OpenAI), and save both to DB.
    """
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

    db = SessionLocal()
    chat = Chat(session_id=session_id, message=message, response=reply)
    db.add(chat)
    db.commit()
    db.refresh(chat)
    db.close()

    return chat


def get_chats(session_id: str):
    """
    Retrieve all chats for a session from the database.
    """
    db = SessionLocal()
    chats = db.query(Chat).filter(Chat.session_id == session_id).all()
    db.close()
    return chats
