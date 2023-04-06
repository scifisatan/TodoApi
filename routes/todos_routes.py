from fastapi import APIRouter, HTTPException
from config.database import collection_name
from models.todos_model import Todo
from schemas.todos_schemas import TodoSerializer, TodosSerializer
from bson import ObjectId
from typing import List, Dict

todo_api_router = APIRouter()

@todo_api_router.get("/")
async def get_all_todos():
    todos = TodosSerializer(collection_name.find())
    return {"status": "ok", "data": todos}

@todo_api_router.get("/{id}")
async def get_todo(id: str) :
    try:
        todo = TodoSerializer(collection_name.find_one({"_id": ObjectId(id)}))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"status": "ok", "data": todo}

@todo_api_router.post("/")
async def post_todo(todo: Todo):
    try:
        _id = collection_name.insert_one(dict(todo))
        todo = TodoSerializer(collection_name.find_one({"_id": _id.inserted_id}))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    return {"status": "ok", "data": todo}

@todo_api_router.put("/{id}")
async def update_todo(id: str, todo: Todo):
    try:
        result = collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(todo)})
        if not result:
            raise HTTPException(status_code=404, detail="Todo not found")
        todo = TodoSerializer(collection_name.find_one({"_id": ObjectId(id)}))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    return {"status": "ok", "data": todo}

@todo_api_router.delete("/{id}")
async def delete_todo(id: str):
    try:
        result = collection_name.find_one_and_delete({"_id": ObjectId(id)})
        if not result:
            raise HTTPException(status_code=404, detail="Todo not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
        
    return {"status": "ok", "data": []}
