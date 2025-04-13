def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    print("🗑️ Tarea eliminada (si existía).")