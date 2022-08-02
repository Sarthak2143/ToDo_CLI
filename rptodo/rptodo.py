"""
This module provides our app Model-Controller.
"""
from pathlib import Path
from typing import Any, Dict, NamedTuple, List
from rptodo.database import DataBaseHandler
from rptodo import DB_READ_ERROR

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
