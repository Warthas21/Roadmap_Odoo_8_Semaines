class Task:

    def __init__(self, title, description, id, status="ToDo"):
        self.title = title
        self.description = description
        self.id = id
        self.status = status

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "id": self.id,
            "status": self.status,
        }
