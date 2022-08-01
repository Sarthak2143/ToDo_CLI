"""
This module provides our app Model-Controller.
"""
from pathlib import Payh
from typing import Any, Dict, NamedTuple
from rptodo.database import DataBaseHandler

class CurrentTodo(NamedTuple):
    todo: Dict[str, Any]
    error: int

class Todoer:
    def __init__(self, db.path: Path) -> None:
        self._db_handler = DataBaseHandler(db_path)
