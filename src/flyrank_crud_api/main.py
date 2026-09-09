from fastapi import  FastAPI
import  uvicorn

app=FastAPI()

my_tasks = [
    {"id": 1, "title": "Task 1", "done": True},
    {"id": 2, "title": "Task 2", "done": False},
    {"id": 3, "title": "Task 3", "done": False},
]


@app.get("/")
def hello():
    return { "name": "Task API", "version": "1.0", "endpoints": ["/tasks"] }


@app.get("/tasks")
def get_tasks():
    return my_tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in my_tasks:
        if task["id"] == task_id:
            return task
    return {f"Task {task_id} not found"},404



@app.post("/tasks")
def create_task(task: dict):
    if not  task["title"] or  not  task["title"].strip():
        return {"error": "Task title is required"}, 400
    new_task = {"id": len(my_tasks) + 1, "title": task["title"], "done": False}
    my_tasks.append(new_task)
    return new_task, 201    


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: dict):
    for t in my_tasks:
        if t["id"] == task_id:
            t["title"] = task.get("title", t["title"])
            t["done"] = task.get("done", t["done"])
            return t
    return {f"Task {task_id} not found"}, 404


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for t in my_tasks:
        if t["id"] == task_id:
            my_tasks.remove(t)
            return {"message": f"Task {task_id} deleted"}
    return {f"Task {task_id} not found"}, 404

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

