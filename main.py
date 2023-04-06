from fastapi import FastAPI
from routes.todos_routes import todo_api_router

app = FastAPI()

app.include_router(todo_api_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=5000, reload=True)

