import json
import pytest
from typer.testing import CliRunner
from rptodo import (
    __app_name__,
    __version__,
    DB_READ_ERROR,
    SUCCESS,
    cli,
    rptodo,
)

runner = CliRunner()

def test_version():
    result = runner.invoke(cli.app, ["--version"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}\n" in result.stdout


"""
To test .add(), we must create a Todoer instance with a proper JSON file as the target database. To provide that file, we’ll use a pytest fixture.
"""

@pytest.fixture
def mock_json_file(tmp_path):
    todo = [{"Description": "Work on flexbox", "Priority": 2, "Done": False}]
    db_file = tmp_path / "todo.json"
    with db_file.open("w") as db:
        json.dump(todo, db, indent=4)
    return db_file

## Tests

test_data1 = {
    "description": ["Make", "a", "game"],
    "priority": 1,
    "todo": {
        "Description": "Make a game.",
        "Priority": 1,
        "Done": False,
    },
}

test_data2 = {
    "description": ["Wash", "the", "car"],
    "priority": 2,
    "todo": {
        "Description": "Wash the car.",
        "Priority": 2,
        "Done": False,
    },
}

"""
The @pytest.mark.parametrize() decorator marks test_add() for parametrization. When pytest runs this test, it calls test_add() two times.
"""

@pytest.mark.parametrize(
    "description, priority, expected",
    [
        pytest.param(
            test_data1["description"],
            test_data1["priority"],
            (test_data1["todo"], SUCCESS),
        ),
        pytest.param(
            test_data2["description"],
            test_data2["priority"],
            (test_data2["todo"], SUCCESS),
        ),
    ],
)
def test_add(mock_json_file, description, priority, expected):
    todoer = rptodo.Todoer(mock_json_file)
    assert todoer.add(description, priority) == expected
    read = todoer._db_handler.read_todos()
    assert len(read.todo_list) == 2

