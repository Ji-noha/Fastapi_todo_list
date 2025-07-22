from fastapi.testclient import TestClient

from app.todo import api, to_do_list

client=TestClient(api)

def setup_function():
    to_do_list.clear()

def test_read_todo():
    response= client.get("/todos")
    assert response.status_code== 200
    assert response.json() == []

def test_create_todo():
    response=client.post("/todos",json={"todo_name": "meals", "todo_description": "buy groceries"})
    assert response.status_code == 200
    data = response.json()
    assert data["todo_name"] == "meals"
    assert data["todo_description"] == "buy groceries"
    assert "todo_id" in data

def test_read_todo_by_id():
    client.post("/todos", json={"todo_name": "meals", "todo_description": "buy groceries"})
    response=client.get("/todos/1")
    assert response.status_code ==200
    data= response.json()
    todo=data["result"]
    assert todo["todo_id"] == 1
    assert todo["todo_name"] == "meals"
    assert todo["todo_description"] == "buy groceries"
    

    
def test_update_todo():
    client.post("/todos", json={"todo_name": "meals", "todo_description": "buy groceries"})
    response=client.put("/todos/1", json={"todo_name": "meals", "todo_description": "buy groceries"})
    assert response.status_code == 200
    data = response.json()
    assert data["todo_name"] == "meals"
    assert data["todo_description"] == "buy groceries"
    assert "todo_id" in data

def test_delete_todo():
    client.post("/todos", json={"todo_name": "meals", "todo_description": "buy groceries"})
    response=client.delete("/todos/1")
    assert response.status_code ==200
    data = response.json()
    assert data["todo_name"] == "meals"
    assert data["todo_description"] == "buy groceries"
    assert "todo_id" in data