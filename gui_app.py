import PySimpleGUI as sg
import datetime
import os

# Define the layout of the form
layout = [
    [sg.Text('Title'), sg.InputText(key='title')],
    [sg.Text('Body'), sg.Multiline(size=(40, 10), key='body')],
    [sg.Text('Satisfaction (1-5)'), sg.Slider(range=(1, 5), orientation='h', size=(15, 20), key='satisfaction')],
    [sg.Submit(), sg.Cancel()]
]

# Create the window
window = sg.Window('Python学習日記アプリ', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    if event == 'Submit':
        title = values['title']
        body = values['body']
        satisfaction = values['satisfaction']

        # Get the current datetime
        now = datetime.datetime.now()

        # Generate the filename with a timestamp
        filename = now.strftime("%Y-%m-%d-%H%M%S") + ".txt"

        # Create the log directory if it doesn't exist
        if not os.path.exists('log'):
            os.makedirs('log')

        # Generate the file path
        filepath = os.path.join('log', filename)

        # Write the input values to the file
        with open(filepath, "w") as f:
            f.write(f"Title: {title}\n")
            f.write(f"Body:\n{body}\n")
            f.write(f"Satisfaction: {satisfaction}\n")

        sg.popup('Saved to', filepath)

window.close()
