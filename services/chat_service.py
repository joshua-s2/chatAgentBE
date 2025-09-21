from typing import List
from models.chat import Chat
from services import workflow_service
import os
import openai


chats: List[Chat] = []
chat_counter = 1

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def create_chat(session_id: str, message: str) -> Chat:
    """
    Create a chat message and get LLM response following workflow policy.
    """
    global chat_counter
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

    chat = Chat(id=chat_counter, session_id=session_id, message=message, response=reply)
    chats.append(chat)
    chat_counter += 1
    return chat

def get_chats(session_id: str) -> List[Chat]:
    """
    Retrieve all chats for a session
    """
    return [c for c in chats if c.session_id == session_id]
