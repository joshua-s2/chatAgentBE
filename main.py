from dotenv import load_dotenv

load_dotenv()
from fastapi import FastAPI
from routes import session, chat, workflow
from fastapi.middleware.cors import CORSMiddleware
import os





app = FastAPI()

app.include_router(session.router, prefix="/api")
app.include_router(chat.router, prefix="/api")
app.include_router(workflow.router, prefix="/api") 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000","https://chat-agent-joshua.vercel.app"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def root():
    return {"message": "backend is running"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000)) 
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)