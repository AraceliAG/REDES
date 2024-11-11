#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print("Welcome, this is a simple nmap automation tool")
print("<----------------------------------------------------->")

ip_addr = input("Please enter the IP address you want to scan: ")
print("The IP you entered is: ", ip_addr)

# Solicitar tipo de escaneo
resp = input("""\nPlease enter the type of scan you want to run
                1)SYN ACK Scan
                2)UDP Scan
                3)Comprehensive Scan \n""")
print("You have selected option: ", resp)

# Definir un diccionario para las opciones de escaneo
resp_dict = {'1': ['-v -sS', 'tcp'], '2': ['-v -sU', 'udp'], '3': ['-v -sS -sV -sC -A -O', 'tcp']}

# Verificar si la opción seleccionada es válida
if resp not in resp_dict.keys():
    print("Enter a valid option")
else:
    # Imprimir la versión de Nmap
    print("Nmap version: ", scanner.nmap_version())

    # Realizar el escaneo
    scanner.scan(ip_addr, "1-1024", resp_dict[resp][0])  # Escanear el rango de puertos 1-1024 con el tipo de escaneo

    # Mostrar la información del escaneo
    print(scanner.scaninfo())

    # Verificar si el host está activo
    if scanner[ip_addr].state() == 'up':
        print("Scanner Status: ", scanner[ip_addr].state())
        print("Protocols: ", scanner[ip_addr].all_protocols())
        print("Open Ports: ", scanner[ip_addr][resp_dict[resp][1]].keys())  # Mostrar puertos abiertos
    else:
        print("The host is down or unreachable.")
