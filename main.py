import json
import shlex

class todo_list():
    def __init__(self):
        self.commands = {
            "add": self.add_task,
            "delete": self.delete_task,
            "lists": self.list_lists,
            "tasks": self.list_tasks,
            "complete": self.mark_task_complete,
            "open": self.get_json,
            "create": self.create_list,
            "select": self.select_list,
            "save": self.save_json,
            "help": lambda: print("List commands: create <list name>, select <list name>, lists, open <list name>, save <list name> \n"
                                  "Task commansds: add <task name> [weight], delete <task number>, tasks, complete <task number> \n"
                                  "Other commands: help, exit")

        }
        self.lists = {}
        self.active_list = None

        self.main()

    # Main loop. Takes input and calls other functions until exit
    def main(self):
        print("Welcome to the todo list program! Type 'help' for a list of commands.")
        while True:
            console_input = input(f"Selected list: {self.active_list} \n \n")   # Gets user input
            phrases = shlex.split(console_input)   # Splits input into phrases based on spaces using shlex to allow for quoted phrases, such as task names
            command = phrases[0].lower()      # First phrase is the command, rest are arguments
            args = phrases[1:]        # (e.g. "add buy milk tomorrow" -> command = "add", args = ["buy", "milk", "tomorrow"])
            print("\n")
            if command in self.commands:
                try:
                    self.commands[command](*args)
                except TypeError:
                    print("Incorrect number of arguments for command. Use 'help' to see correct usage!")
            elif command == "exit":   # Exits the program, saving the active list if there is one. Not a standard command as 'break' cannot be used outside of the loop
                for list_name in self.lists.keys():
                    self.save_json(list_name)
                break
            else:
                print("Unknown command")

    
    # List handling functions
    def create_list(self, list_name):    
        # Creates a new list with the given name, if it doesn't already exist
        if(list_name in self.lists):
            print("List already exists. Making it the active list.")
        else:
            self.lists[list_name] = []
            print(f"Created and selected list \"{list_name}\" \n")

        self.active_list = list_name
        self.list_lists()
    
    def select_list(self, list_name):
        # Checks if the desired list exists, and if so, sets it as the active list. If not, prompts to create it
        if(list_name in self.lists):
            self.active_list = list_name
        else:
            if(input("List does not exist. Would you like to create it? (y/n)").lower() == "y"):
                self.create_list(list_name)
                self.active_list = list_name
        print(f"Selected list \"{list_name}\" \n")
        self.list_lists()

    def list_lists(self):
        # Lists all existing lists
        for list_name in self.lists.keys():
            if(list_name == self.active_list):
                print(f"{list_name} <--")
            else:
                print(list_name)
            
    def get_json(self, list_name):
        # Retrieves data from a JSON file and loads it into the lists dictionary
        try:
            with open(f"{list_name}.json", "r") as f:
                data = json.load(f)
                self.lists[list_name] = data
        except FileNotFoundError:
            if(input("List does not exist. Would you like to create it? (y/n)").lower() == "y"):
                self.create_list(list_name)
        self.active_list = list_name

        print(f"Imported list \"{list_name}\" \n")
        self.list_lists()

    def save_json(self, list_name):
        # Writes the named list to a JSON file
        with open(f"{list_name}.json", "w") as f:
            json.dump(self.lists[list_name], f)
        
        print(f"Saved list \"{list_name}\" to file \"{list_name}.json\" \n")
    
    # Task handling functions
    def add_task(self, task_name, weight=None):
        # Adds a task to the active list, with parameters for the name and 'weight,' measuring importance or how demanding the task is)
        self.lists[self.active_list].append({"name": task_name, "weight": weight, "complete": False})

        print(f"Added task \"{task_name}\" to list \"{self.active_list}\" \n")
        self.list_tasks()
    
    def delete_task(self, task_number):
        task_index = task_number - 1
        try:
            self.lists[self.active_list].pop(task_index)
        except IndexError:
            print(f"No task with that number on list \"{self.active_list}\" \n")

        print(f"Removed task {task_number} from list \"{self.active_list}\" \n")
        self.list_tasks()

    def list_tasks(self):
        for i, task in enumerate(self.lists[self.active_list]):
            status = "✓" if task["complete"] else "✗"
            if(task["weight"] is None):
                print(f"{i+1}. [{status}] {task['name']}")
            else:
                print(f"{i+1}. [{status}] {task['name']} (Weight: {task['weight']})")
        print("\n")

    def mark_task_complete(self, task_number):
        if not task_number.isdigit():
            print("Please enter the task number, not the task name! Use the 'tasks' command to see task numbers.")
            return
        task_index = int(task_number) - 1
        try:
            self.lists[self.active_list][task_index]["complete"] = True
        except IndexError:
            print(f"No task with that number on list \"{self.active_list}\"")

        print(f"Marked task {task_number} as complete on list \"{self.active_list}\" \n")
        self.list_tasks()

todo_list()