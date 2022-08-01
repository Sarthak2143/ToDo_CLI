"""
This module provides our app database functionality.
"""

import configparser
from path import Path
from rptodo import DB_WRITE_ERROR, SUCCESS

DEFAULT_DB_FILE_PATH = Path.home().joinpath(
    "." + Path.home().stem + "_todo.json"
)

def get_database_path(config_file: Path) -> Path:
    '''Returns the current path to the to-do db.'''
    config_parser = configparser.ConfigParser()
    config_parser.read(config_file)
    return Path(config_parser["General"]["database"])

def init_database(db_path: Path) -> int:
    '''Create the to-do db.'''
    try:
        db_path.write_text("[]") # empty to-do list
        return SUCCESS
    except OSError:
        return DB_WRITE_ERROR
