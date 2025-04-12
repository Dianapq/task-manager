# task_manager/storage.py

from task_manager.tasks import Task

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append(Task(description))

    def list_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task}")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].complete()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
