# FastAPI To-Do-List 
A minimalist Python API to manage your tasks: add, update, delete, or list them.Just give a task name and a description and you're ready to go.
Includes a test_todo.py file to make sure everything runs smoothly and correctly.

# Features:
° add a new task (name+description)
° Update an existing task
° Delete a task
° View all tasks
° Includes automated tests (test_todo.py)

# How to Use :
- clone the project to your local machine:

```bash 
git clone https://github.com/your-username/your-repo-name.git 
```

- Then, Change into the project directory:
``` Bash
cd path/to/project 
```

- Build the docker image:
```bash 
docker build -t fastapi_todo . 
```

-Run the container:
```bash 
docker run -d -p 8000:8000 fastapi_todo 
```

-Open your browser and go to : 
http://localhost:8000/docs

# Requirements
All dependencies are already handled in the Docker image. No need to install anything locally.

#
Tests are included for development purposes, but you don't need to run them unless you're modifying the code."# Fastapi_todo_list" 
