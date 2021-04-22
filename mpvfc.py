import PySimpleGUI as sg
import os

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [[sg.T('Video File Location')],
          [sg.In(), sg.FileBrowse(target=(1, 0))],
          [sg.T('   ')],
          [sg.T('1st Subtitle File')],
          [sg.In(), sg.FileBrowse(target=(4, 0))],
          [sg.T('   ')],
          [sg.T('2nd Subtitle File')],
          [sg.In(), sg.FileBrowse(target=(7, 0))],
          [sg.T('   ')],
          [sg.T('Secondary Subtitle Index')],
          [sg.In(default_text = "2")],
          [sg.OK()]
         ]

# Create the Window
window = sg.Window('Dual Subtitle With MPV', icon='vid-icon.ico').Layout(layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    
    for i in values:
        print(i, values[i])
    
    print('mpv "' + values[0] + '" --sub-file="' + values[1] + '" --sub-file="' + values[2] + '" --secondary-sid=' + values[3])
    os.popen('mpv "' + values[0] + '" --sub-file="' + values[1] + '" --sub-file="' + values[2] + '" --secondary-sid=' + values[3])
    
    break

window.close()