import PySimpleGUI as sg
import csv
import os

# Define the layout of the form
layout = [
    [sg.Text('Satisfaction (1-5)')],
    [sg.Text('', key='satisfaction')],
    [sg.Text('Title')],
    [sg.Text('', key='title')],
    [sg.Text('Body')],
    [sg.Multiline('', key='body', size=(40, 10), disabled=True, autoscroll=True)],
    [sg.Button('<'), sg.Button('>')],
    [sg.Button('Close')]
]

# Create the window and set finalize=True
window = sg.Window('Study Log Viewer', layout, finalize=True)

def read_csv(file_path):
    data = []
    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            for row in reader:
                row[2] = row[2].replace('\\n', '\n')  # Convert \n back to newlines
                data.append(row)
    return data

def update_form(window, data, index):
    if data:
        window['title'].update(data[index][1])
        window['body'].update(data[index][2])
        window['satisfaction'].update('★' * int(data[index][3]))

# Read the CSV data
data = read_csv('studylog.csv')
current_index = 0

# Initialize the form with the first entry
if data:
    update_form(window, data, current_index)

# Main event loop
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Close'):
        break
    if event == '<' and current_index > 0:
        current_index -= 1
        update_form(window, data, current_index)
    if event == '>' and current_index < len(data) - 1:
        current_index += 1
        update_form(window, data, current_index)

window.close()