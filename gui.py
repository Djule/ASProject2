import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter Name")
input_box2 = sg.InputText(tooltip="Enter Address")
add_button = sg.Button("Add")

window = sg.Window("My Todo App", layout=[[label], [input_box], [input_box2 ,add_button]])
window.read()
window.close()