import FreeSimpleGUI as sg
import functions

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
show_button = sg.Button("Show")

window = sg.Window("My Todo App",
                   layout=[[label], [input_box ,add_button], [show_button]],
                   font=("Helvetica", 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"]  + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

        case "Show":
            todos = functions.get_todos()

            for item in todos:
                item = item.strip("\n")
                print(item)

        case sg.WIN_CLOSED:
            break

window.close()

