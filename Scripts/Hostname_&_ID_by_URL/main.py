import socket

def get_hostname_IP():
    hostname = input("Введите адрес сайта(без https://): ")
    try:
        print (f'Имя хостинга: {hostname}')
        print (f'IP: {socket.gethostbyname(hostname)}')
    except socket.gaierror as error:
        print (f'Неверный адрес - {error}')

get_hostname_IP()