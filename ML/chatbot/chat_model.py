from langchain_google_genai import ChatGoogleGenerativeAI as genai
from config import MODEL_NAME

# Initialize the chat model
CHAT_MODEL = genai(model=MODEL_NAME)

def get_chat_response(prompt):
    """
    Sends the prompt to the chat model and returns the response.
    """
    response = CHAT_MODEL.invoke(prompt)
    return response.content
