import PySimpleGUI as sg
import datetime
import os
import csv

# Define the layout of the form
layout = [
    [sg.Text('Title', text_color='#FFFFFF', background_color='#669966')],
    [sg.InputText(key='title', size=(80, 1))],  # Adjusted width to match window width
    [sg.Text('Body', text_color='#FFFFFF', background_color='#669966')],
    [sg.Multiline(size=(80, 10), key='body')],  # Adjusted width to match window width
    [sg.Text('Satisfaction (1-5)', text_color='#FFFFFF', background_color='#669966')],
    [sg.Slider(range=(1, 5), orientation='h', size=(15, 20), key='satisfaction')],
    [sg.Submit(), sg.Button('閉じる')]
]

# Create the window with a width of 600 pixels, a height of 400 pixels, and a background color of #669966
window = sg.Window('Python学習日記アプリ', layout, size=(600, 400), background_color='#669966')

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, '閉じる'):
        break
    if event == 'Submit':
        title = values['title']
        body = values['body'].replace('\n', '\\n')
        satisfaction = int(values['satisfaction'])

        # Get the current datetime
        now = datetime.datetime.now()

        # Define the CSV file path
        csv_file = 'studylog.csv'

        # Check if the CSV file exists
        file_exists = os.path.isfile(csv_file)

        # Open the CSV file in append mode
        with open(csv_file, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            # If the file does not exist, write the header
            if not file_exists:
                writer.writerow(['datetime', 'title', 'body', 'satisfaction'])
            # Write the data
            writer.writerow([now.strftime("%Y-%m-%d %H:%M:%S"), title, body, satisfaction])

        sg.popup('Saved to', csv_file)

window.close()