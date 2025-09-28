
# Console-Based To-Do List

This is a simple, interactive console-based to-do list application written in Python. It allows users to manage tasks directly from the terminal, with persistent storage using JSON files.

## Features

- Add new tasks with a versatile "weight" property for priority or cost
- List all tasks
- Mark tasks as completed
- Remove tasks
- Persistent storage in JSON format
- Simple command interface with support for quoted phrases

## Getting Started

### Prerequisites

- Python 3.7 or higher

### Installation

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run the program:
	```
	python main.py
	```

## Usage

When running, enter commands at the prompt. Supported commands include:

- `add "task description" [weight]` — Add a new task. Example: `add "Buy milk" 2`
- `delete [task number]` — Remove a task
- `tasks` — Show all tasks
- `complete [task number]` — Mark a task as completed
- `create <list name>` — Create a new list
- `select <list name>` — Select a list
- `lists` — Show all lists
- `open <list name>` — Open a list from a file
- `save <list name>` — Save a list to a file
- `help` — Show help
- `exit` — Exit the program

Quoted phrases are supported for multi-word task descriptions.

## Data Storage

Tasks are stored in JSON files in the project directory. Each task includes:

- `name`: Task description
- `weight`: Task weight (optional)
- `status`: Complete/incomplete

## Author

Created by noahhodge04 with help from GitHub Copilot.