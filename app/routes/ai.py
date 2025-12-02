from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import openai
import os

router = APIRouter()

class CommandRequest(BaseModel):
    command: str
    user_name: str = "User"

class CommandResponse(BaseModel):
    response: str

openai.api_key = os.getenv("OPENAI_API_KEY")

@router.post("/ai/process_command", response_model=CommandResponse)
def process_command(request: CommandRequest):
    if not openai.api_key:
        raise HTTPException(status_code=500, detail="OpenAI API key not configured")
    
    try:
        prompt = f"You are a compassionate AI caregiver assistant for seniors. Respond empathetically to: '{request.command}'. Address the user as {request.user_name}."
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful, empathetic AI caregiver for seniors."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7
        )
        
        ai_response = response.choices[0].message.content.strip()
        return CommandResponse(response=ai_response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI processing error: {str(e)}")