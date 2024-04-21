import socket

# Definir qual é o host e qual é a porta
HOST = 'localhost'
PORT = 50000
# Criando o socket TCP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Estabelecendo conexão com um socket a um destindo
cliente.connect((HOST, PORT))

print("Para sair use: \y12\n")

namefile = str(input("O que você deseja?: "))
cliente.send(namefile.encode())
# recebendo os dados do servidor!
with open(namefile, 'wb') as file:
    while 1:
        data = cliente.recv(1000000)
        # Se não receber o arquivo, ele vai parar
        if not data: break
        file.write(data)
print(f"{namefile} O arquivo foi recebido!!!")       

