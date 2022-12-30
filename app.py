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
      
      
      window["tabuada"].print( f'A tabuada de {const_num} é \n {const_num} x 0 = {0 * const_num} \n {const_num} x 1 = {1 * const_num} \n {const_num} x 2 = {2 * const_num} \n {const_num} x 3 = {3 * const_num} \n {const_num} x 4 = {4 * const_num} \n {const_num} x 5 = {5 * const_num} \n {const_num} x 6 = {6 * const_num} \n {const_num} x 7 = {7 * const_num} \n {const_num} x 8 = {8 * const_num} \n {const_num} x 9 = {9 * const_num} \n {const_num} x 10 = {10 * const_num} \n' )
      window.refresh()





 

    
   


