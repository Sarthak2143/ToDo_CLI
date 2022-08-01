"""
This module provides our app Model-Controller.
"""

from typing import Any, Dict, NamedTuple

class CurrentTodo(NamedTuple):
    todo: Dict[str, Any]
    error: int
