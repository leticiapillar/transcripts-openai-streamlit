import pickle
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
from pathlib import Path

load_dotenv(find_dotenv())

PATH_CONFIGS = Path(__file__).parent/"configs"
PATH_CONFIGS.mkdir(exist_ok=True)

def audio_transcriptions(file, prompt="", api_key="", model="whisper-1", format="text", language="en"):
    client = OpenAI(api_key=api_key)
    return client.audio.transcriptions.create(
        file=file,
        prompt=prompt,
        model=model, 
        response_format=format,
        language=language,
    )

def save_api_key(api_key):
    with open(PATH_CONFIGS/"key", "wb") as f:
        pickle.dump(api_key,f)

def load_api_key():
    if (PATH_CONFIGS/"key").exists():
        with open(PATH_CONFIGS/"key", "rb") as f:
            return pickle.load(f)
    return ""
