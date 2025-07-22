from fastapi import FastAPI, HTTPException

api=FastAPI()

to_do_list=[
    {'todo_id':1 , 'todo_name': 'sports', 'todo_description': 'go to the gym'},
    {'todo_id':2 , 'todo_name': 'study', 'todo_description': 'study math'},
    {'todo_id': 3,'todo_name': 'clean', 'todo_description':'clean the house'},
    {'todo_id': 4,'todo_name': 'meditate', 'todo_description':'meditate for 20 min'}
]

@api.get("/")
def root():
    return {"message": "Welcome to the FastAPI To-Do List"}


@api.get('/todos/{todo_id}')
def get_todo(todo_id:int):
    for todo in to_do_list:
        if todo['todo_id'] == todo_id :
            return {'result':todo}
    

@api.get('/todos')
def get_todo_n(first_n: int= None):
        if first_n:
            return to_do_list[:first_n]
        else:
            return to_do_list

@api.post('/todos')
def create_todo(todo: dict):
        new_todo_id=max((todo['todo_id'] for todo in to_do_list), default=0 ) + 1
        new_todo={
                'todo_id': new_todo_id,
                'todo_name': todo['todo_name'],
                'todo_description': todo['todo_description']
            }
        to_do_list.append(new_todo)
        return new_todo

@api.put('/todos/{todo_id}')
def update_todo(todo_id: int, updated_todo: dict):
    for todo in to_do_list:
        if todo['todo_id']== todo_id:
            todo['todo_name']= updated_todo['todo_name']
            todo['todo_description']= updated_todo['todo_description']
            return todo
    raise HTTPException(status_code=404, detail="todo not found")
    
@api.delete('/todos/{todo_id}')
def delete_todo(todo_id: int):
    for index, todo in enumerate(to_do_list):
        if todo['todo_id']== todo_id:
            deleted_todo= to_do_list.pop(index)
            return deleted_todo
    raise HTTPException(status_code=404, detail="Todo not found")

