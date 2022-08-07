"""
This module provides our app Model-Controller.
"""
from pathlib import Path
from typing import Any, Dict, NamedTuple, List
from rptodo.database import DataBaseHandler
from rptodo import DB_READ_ERROR, ID_ERROR

class CurrentTodo(NamedTuple):
    todo: Dict[str, Any]
    error: int

class Todoer:
    def __init__(self, db_path: Path) -> None:
        self._db_handler = DataBaseHandler(db_path)

    def add(self, description: List[str], priority: int = 2) -> CurrentTodo:
        """Add a new to-do to the database."""
        desc_text = " ".join(description)
        if not desc_text.endswith("."):
            desc_text += "."
        todo = {
            "Description": desc_text,
            "Priority": priority,
            "Done": False,
        }
        read = self._db_handler.read_todos()
        if read.error == DB_READ_ERROR:
            return CurrentTodo(todo, read.error)
        read.todo_list.append(todo)
        write = self._db_handler.write_todos(read.todo_list)
        return CurrentTodo(todo, write.error)

    def get_todo_list(self) -> List[Dict[str, Any]]:
        """Returns the current to-do list."""
        read = self._db_handler.read_todos()
        return read.todo_list

    def set_done(self, todo_id: int) -> CurrentTodo:
        """Set a todo as done"""
        read = self._db_handler.read_todos()
        if read.error:
            return CurrentTodo({}, read.error)
        try:
            todo = read.todo_list[todo_id - 1]
        except IndexError:
            return CurrentTodo({}, ID_ERROR)
        todo["Done"] = True
        write = self._db_handler.write_todos(read.todo_list)
        return CurrentTodo(todo, write.error)

    def remove(self, todo_id: int) -> CurrentTodo:
        """Remove a todo from the database using its ID or index"""
        read = self._db_handler.read_todos()
        if read.error:
            return CurrentTodo({}, read.error)
        try:
            todo = read.todo_list.pop(todo_id - 1)
        except IndexError:
            return CurrentTodo({}, ID_ERROR)
        write = self._db_handler.write_todos(read.todo_list)
        return CurrentTodo(todo, write.error)

    def remove_all(self) -> CurrentTodo:
        """Clears the list i.e removes all to-dos."""
        write = self._db_handler([])
        return CurrentTodo({}, write.error)
