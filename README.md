# CLI ToDo Application

The application has a user-friendly CLI that allows you to set up the to-do database. Once there, you can add, remove, and complete to-dos using appropriate commands, arguments, and options. If you ever get stuck, then you can ask for help using the `--help` option with proper arguments.

## Usage

- Run the app as a module

```bash
python3 -m rptodo
```

```bash
Usage: rptodo [OPTIONS] COMMAND [ARGS]...
Try 'rptodo --help' for help.
```

- Basic commands:
    - -v or --version shows the current version and exits the application.
    - --help shows the global help message for the entire application.

- Regarding managing a to-do list, our application will provide commands to initialize the app, add and remove to-dos, and manage the to-do completion status:

| Command | Description |
| --- | --- |
| init | Initializes the application’s to-do database |
| `add` DESCRIPTION | Adds a new to-do to the database with a description |
| `list` | Lists all the to-dos in the database |
| `complete` **TODO_ID** | Completes a to-do by setting it as done using its ID |
| `remove` **TODO_ID** | Removes a to-do from the database using its ID |
| `clear` | Removes all the to-dos by clearing the database |

**Directory structre:**

```bash
.
│
├── rptodo/
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py
│   ├── config.py
│   ├── database.py
│   └── rptodo.py
│
├── tests/
│   ├── __init__.py
│   └── test_rptodo.py
│
├── README.md
└── requirements.txt
```
---

## Installation

1. Clone the repo

```bash
git clone https://github.com/Sarthak2143/ToDo_CLI
cd ToDo_CLI/
```

2. Activate Virtual Environment

```bash
python3 -m venv ./venv
source venv/bin/activate
```

3. Install required packages

```bash
pip3 install requirements.txt
```

## Testing

For this project we are using `pytest` for testing.

Run the tests:
```bash
python3 -m pytest tests/
```


For now, there are'nt much tests, but its in my todo.


## TODO

- [ ] Add support for dates and deadlines.
- [ ] Write more unit tests.

---
