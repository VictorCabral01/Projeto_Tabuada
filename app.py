import PySimpleGUI as sg


sg.theme('black')

layout=[
    [sg.Text("Digite um número"), sg.Input("", key="numero"), sg.Button("Calcular"), sg.Button("Calcelar")],
    [sg.Text("", key="tabuada")]
]


window = sg.Window("Tabuada", layout)


while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED  or event == "Calcelar":
        break

    if event == "Calcular":
     
      const_num = int(values["numero"])
      window["tabuada"].print(f'A Tabuada de {const_num} é :')
      for x in range(11):
        n = window["tabuada"].print(f'{const_num} x {x} = {x*const_num}')
      
      window.refresh()





 

    
   


