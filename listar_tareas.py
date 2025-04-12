# Listar tareas
def list_tasks():
    if not tasks:
        print("📭 No hay tareas.")
        return
    for idx, task in enumerate(tasks, 1):
        status = "✅" if task["completed"] else "❌"
        print(f"{idx}. {task['description']} [{status}] - ID: {task['id']}")
