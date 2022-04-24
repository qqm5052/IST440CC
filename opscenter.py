# pip install pysimplegui
# pip3 install pysimplegui

# Reference: https://pysimplegui.readthedocs.io/en/latest/

import PySimpleGUI as sg
from log import Log



headings = ['Puzzle','Team 1', 'Team 2', 'Team 3','Team 4']  # the text of the headings

sg.theme('Dark Blue 1')
layout = [
    [sg.Text('Moon Alpha Control Center', font='_ 28', justification='c', expand_x=True)],
    [sg.Text(' ', size=(0,3))],
    [sg.Text(h, size=(10,1), font='_ 18') for h in headings],

    # Should only have to make edits below for your puzzles
    [sg.Text('Puzzle 1', size=(16,1)), sg.Text('      '), sg.Checkbox('Checkbox', size=(13,1)), sg.Text('              '), sg.Checkbox('Light', size=(14,1), text_color='Red', key='chk_light'), sg.Checkbox('Checkbox', size=(13,1)), sg.Text('      '), sg.Checkbox('Rover Access', size=(0,1), text_color='Red', key='chk_rover')],
    [sg.Text('Puzzle 2', size=(16,1)), sg.Text('      '), sg.Checkbox('Checkbox', size=(13,1)), sg.Text('              '), sg.Checkbox('Water', size=(14,1), text_color='Red', key='chk_water'),  sg.Checkbox('Checkbox', size=(13,1)), sg.Text('      '), sg.Checkbox('Gate Access', size=(0,1), text_color='Red', key='chk_gate')],
    [sg.Text('Puzzle 3', size=(16,1)), sg.Text('      '), sg.Checkbox('Checkbox', size=(13,1)), sg.Text('              '), sg.Checkbox('Fire', size=(14,1), text_color='Red', key='chk_fire'),  sg.Checkbox('Checkbox', size=(13,1)), sg.Text('      '), sg.Checkbox('Mission Complete', size=(0,1), text_color='Red', key='chk_mission')],
     
    [sg.Button('Refresh', size=(81,2))]
]

# Used to update the Checkbox from false to true
# Will then change the text from red to green
def updatechkbox(chkkey:str):
    window[chkkey].Update(value=True)    
    window[chkkey].Update(text_color="Green")


# Create the window
window = sg.Window("Demo", layout, margins=(200,100))

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window
    if event == sg.WIN_CLOSED:
        break
    
    # This is where we start looking for puzzle completion messages
    # How to get values of a box: values['chk_light']
    data = Log.getstatus_json()    #Is updated on Refresh; wont need this unless eve server is up
    for i in data["_items"]:    # Will crash if no connection to eve
        if(i["message"] == "Water Puzzle Completed"):
            updatechkbox('chk_water')
        if(i["message"] == "Light Puzzle Completed"):
            updatechkbox('chk_light')
        if(i["message"] == "Fire Puzzle Completed"):
            updatechkbox('chk_fire')
        if(i["message"] == "Rover Puzzle Completed"):
            updatechkbox('chk_rover')
        if(i["message"] == "Numpad Puzzle Completed"):
            updatechkbox('chk_gate')
        if(i["message"] == "Mission Completed"):
            updatechkbox('chk_mission')
window.close()