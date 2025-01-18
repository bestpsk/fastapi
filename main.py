from fastapi import FastAPI
import uvicorn
from routers import user

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(user.router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)