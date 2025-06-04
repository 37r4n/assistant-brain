import uvicorn
import config

if __name__ == "__main__":
    uvicorn.run("app.app:app", host=config.server.host, port=config.server.port, reload=True)
