# todo-list
A simple console-based to-do list built with Python

To use, simply run `main.py`.

This program uses JSON files to store tasks, giving each list a file and each task an object within the file. It was designed to function like a shell, having some commands. This is the output of the command `help` for example:
```
List commands: create <list name>, select <list name>, lists, open <list name>, save <list name>
Task commansds: add <task name> [weight], delete <task number>, tasks, complete <task number>
Other commands: help, exit
```
As this program uses a shell-like input, you must put any text inputs (such as names) in quotes if they contain spaces. For example,
`add laundry 5` would work, but `add fold laundry 5` would have to be written as `add "fold laundry" 5`.

Tasks have three properties: a name, a weight, and a status (complete/incomplete). Weight can describe a number of things, but to me it means how much mental energy a task will take.

List names are always converted to lower-case, and are thus not case-sensitive. Task names are case-sensitive, but no commands use task names as an argument.

The `exit` command will automatically save all of the lists before ending the program. Lists are saved to the same directory as `main.py`