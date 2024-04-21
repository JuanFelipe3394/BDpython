# Aluno: Elohim Felipe Santiago da Silva

import socket
import threading

HOST = 'localhost' # endereço ip
PORT = 50000
# criando (instância) um objeto do tipo socket
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Ligando o socket a porta
servidor.bind((HOST, PORT))
# Definindo o máximo de conexões que deverão estar enfileiradas
servidor.listen(5)
print("[*] SERVIDOR ESCUTANDO %s:%d" %(HOST, PORT))

# Necessário para que na primeira mensagem, o programa não encerre.
while True:
    cliente, address = servidor.accept()
    print("[*] Conexão aceita de: %s:%d" %(address[0], address[1]))
    # Buffer de 1024 bytes / o decode está transformando de bytes p/ string
    mensagem = cliente.socket.recv(2048).decode()
    # para enviar o arquivo ao cliente
    # o open vai abrir o arquivo, caso tenha erro, o with garante que
    # o arquivo seja fechado para não haver encher a memória.
    # o open recebe string e não bytes, por isso foi necessário o decode
    with open('mensagem', 'rb') as file:
        # readlines vai ler o arquivo e enviar para o cliente 
        for data in file.readlines():
            # para enviar o dado 
            cliente.send(data)
        print('O pedido foi enviado!!! :)')
