class Todo:

    def __init__(self, code_id: int, title: str, description: str):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.tags: (list[str]) = []

    def mark_completed(self):
        self.completed = True

    def add_tag(self, tag: str):
        if tag in self.tags:
            return self.tags
        else:
            self.tags.append(tag)
        return tag


def __str__(self) -> str:
    return self.code_id and self.title


class TodoBook:
    def __init__(self):
        self.todos: dict = {}

    def add_todo(self, title: str, description: str) -> int:
        self.id = len(self.todos) + 1
        Todo.objeto()
        self.todos.append(object)
        return self.id