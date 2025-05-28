import uvicorn
from fastapi import FastAPI
from backend.services.startup_services import startup_service
app = FastAPI(
    title="PyRag",
    version="1.0.0",
    license_info={
        "name": "Apache License 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0",
    },
    description="PyRag is a Python library for building and managing RAG (Retrieval-Augmented Generation) systems.",
)

app.add_event_handler("startup", startup_service)
@app.get("/")
async def read_root():
    return {"message": "Welcome to PyRag!"}
if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, log_level="info")
