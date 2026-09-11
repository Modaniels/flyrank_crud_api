from fastapi import  FastAPI
import  uvicorn
import  sqlite3

app=FastAPI()

db=sqlite3.connect("tasks.db", check_same_thread=False)


@app.get("/")
def hello():
    return { "name": "Task API", "version": "1.0", "endpoints": ["/tasks"] }


@app.get("/tasks")
def get_tasks():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM task")
    rows = cursor.fetchall()
    return rows

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM task WHERE id=?", (task_id,))
    row = cursor.fetchone()
    if row:
        return row
    else:
        return {"error": f"Task {task_id} not found"}, 404



@app.post("/tasks")
def create_task(task: dict):
   cursor=db.cursor()
   cursor.execute("INSERT INTO task (title, done) VALUES (?, ?)", (task["title"], task.get("done", False)))
   db.commit()
   task_id = cursor.lastrowid
   return {"id": task_id, "title": task["title"], "done": task.get("done", False)}
   


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: dict):
   cursor=db.cursor()
   cursor.execute("UPDATE task SET title=?, done=? WHERE id=?", (task["title"], task.get("done", False), task_id))
   db.commit()
   if cursor.rowcount == 0:
       return {"error": f"Task {task_id} not found"}, 404
   return {"id": task_id, "title": task["title"], "done": task.get("done", False)}


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

