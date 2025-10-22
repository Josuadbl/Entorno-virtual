import time
from utils import send_to_gemini

def temporizador(segundos):
    print(f"\n Temporizador iniciado por {segundos} segundos...")
    for i in range(segundos, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    print("¡Tiempo cumplido!")
    send_to_gemini(f"El temporizador de {segundos} segundos ha finalizado.")

if __name__ == "__main__":
    try:
        segundos = int(input("Ingresa la duración del temporizador en segundos: "))
        if segundos > 0:
            temporizador(segundos)
        else:
            print(" Por favor ingresa un número mayor a cero.")
    except ValueError:
        print(" Entrada inválida. Debes ingresar un número entero.")