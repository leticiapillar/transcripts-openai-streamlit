from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

client = OpenAI()

def audio_transcriptions(file, prompt="", model="whisper-1", format="text", language="en"):
    return client.audio.transcriptions.create(
        file=file,
        model=model, 
        response_format=format,
        language=language,
        prompt=prompt
    )