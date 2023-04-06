def TodoSerializer(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "name": todo["name"],
        "description": todo["description"],
        "completed": todo["completed"]
    }

def TodosSerializer(todos) -> list:
    return [TodoSerializer(todo) for todo in todos]