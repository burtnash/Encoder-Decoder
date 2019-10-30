import Encoder, Decoder, sys
sys.path.append('PySimpleGUI-master')
import PySimpleGUI as sg

while True:
    layout = [[sg.Text('Enter Your Message:', size=(15, 1)), sg.InputText()],           
            [sg.Button("Encode"), sg.Button("Decode"),
             sg.Button("Double Encode"), sg.Button("Double Decode"),
             sg.Button("Close")]]      
    window = sg.Window('Message Entry', layout)  
    event, values = window.Read()   
    window.Close()

    if event == 'Encode':
        result = Encoder.encode(values[0])
    elif event == 'Decode':
        result = Decoder.decode(values[0])
    elif event == 'Double Encode':
        result = Encoder.double_encode(values[0])
    elif event == 'Double Decode':
        result = Decoder.double_decode(values[0])
    else:
        break
    
    layout2 = [[sg.Multiline(result)], [sg.Button("OK"), sg.Button("Close")]]
    window = sg.Window('Result', layout2)
    event = window.Read()
    window.Close()
    if event[0] == "Close":
        break
