import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(now * 2)
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:].capitalize()

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            index = str(index + 1)
            print(f"{index}-{item}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            newTodo = input("Enter new todo ").capitalize()
            todos[number] = newTodo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Invalid input")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            todo_to_remove = todos[number - 1].strip('\n')
            todos.pop(number - 1)

            functions.write_todos(todos)

            message = f"{todo_to_remove} completed successfully"
            print(message)

        except IndexError:
            print("Invalid input for complete")
    elif "exit" in user_action:
        break
    else:
        print("Invalid input")
