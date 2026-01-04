from .task import Task
import json


class TaskManager:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def add_task(self, title, description):
        if self.tasks:
            max_id = max(task.id for task in self.tasks)
            task_id = max_id + 1
        else:
            task_id = 1
        new_task = Task(title, description, task_id)
        self.tasks.append(new_task)

    def delete_task(self, id):
        task_to_remove = None
        for task in self.tasks:
            if task.id == id:
                task_to_remove = task
                break
        if task_to_remove is not None:
            self.tasks.remove(task_to_remove)

    def save_tasks(self):
        data = []
        for task in self.tasks:
            data.append(task.to_dict())
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_tasks(self):
        try:
            with open(self.filename, "r") as f:
                loaded_tasks = json.load(f)
            self.tasks = (
                []
            )  # On vide la liste actuelle pour éviter les doublons si on recharge
            for task in loaded_tasks:
                new_task = Task(
                    task["title"], task["description"], task["id"], task["status"]
                )
                self.tasks.append(new_task)
        except FileNotFoundError:
            print("Le Fichier n'existe pas")
