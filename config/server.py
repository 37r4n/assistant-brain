import os
from dotenv import load_dotenv

load_dotenv()

class Server:
    port: int = int(os.getenv("PORT", 8080)) 
    host: str = os.getenv("HOST", "127.0.0.1")

server = Server()