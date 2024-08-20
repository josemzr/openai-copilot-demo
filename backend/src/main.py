from fastapi import FastAPI, HTTPException, Path
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from uuid import uuid4

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Task model
class Task(BaseModel):
    id: str
    name: str
    description: str
    done: bool

# In-memory storage for tasks
tasks = {}

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return list(tasks.values())

@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task: Task):
    task_id = str(uuid4())
    task.id = task_id
    tasks[task_id] = task
    return task

@app.put("/tasks/{id}", response_model=Task)
def update_task(id: str, task: Task):
    if id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[id] = task
    return task

@app.delete("/tasks/{id}", status_code=204)
def delete_task(id: str = Path(..., description="The ID of the task to delete")):
    if id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[id]
    return

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)