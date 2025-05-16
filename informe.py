import yfinance
import time
import pyautogui
import pyperclip
import webbrowser
from time import sleep

# obtencion de datos
tiket = input("Ingrese el codigo de la accion: ")
datos = yfinance.Ticker(tiket).history ("6mo")
cierre = datos['Close']

# valores a obtener
valor_maximo_cierre= round(cierre.max(),2)
valor_minimo_cierre= round(cierre.min(),2)
valor_medio_cierre= round(cierre.mean(),2)

# contenidos para correo
Destinatario = "aur*****@gmail.com"
Asunto = "Informe de cirre de acciones de los ultimos 6 meses"

Cuerpo = f"""
Buen día, 

A continuación se presenta el informe de cierre de la acción. {tiket} 
del periodo solicitado.

Valor máximo de cierre: USD {valor_maximo_cierre}
Valor mínimo de cierre: USD {valor_minimo_cierre}
Valor medio de cierre: USD {valor_medio_cierre}

Reciba un cordial saludo.
Auria.
"""
# establecimiento de pausa ente cada paso
pyautogui.PAUSE = 3 

# direccionando al navegador
webbrowser.open("https:milogin.outlook.com")
sleep(3)

# click en boton de nuevo mensaje
pyautogui.click(x=201, y=232)

# proceso de llenado en destinatario
pyperclip.copy(Destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")
pyautogui.click(x=381, y=424)

# proceso de llenado en asunto
pyperclip.copy(Asunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")
pyautogui.click(x=434, y=517)

#proceso de llenado en cuerpo del mensaje
pyperclip.copy(Cuerpo)
pyautogui.hotkey("ctrl", "v")

# click en boton de enviar
pyautogui.click(x=427, y=289)

# click en cerrar ventana
pyautogui.click(x=1403, y=1055)

print("¡el e-mail se ha enviado exitosamente!!")