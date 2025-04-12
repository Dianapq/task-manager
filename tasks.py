# task_manager/tasks.py

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def complete(self):
        self.completed = True

    def __str__(self):
        status = "[✓]" if self.completed else "[ ]"
        return f"{status} {self.description}"
