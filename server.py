from socket  import *
from constCS import * #-
import math
import time

def calcular_raiz(comando):
    """Calcula a raiz quadrada: 'RAIZ 25' -> 5.0"""
    try:
        valor = float(comando.split()[1])
        if valor < 0: return "Erro: Não existe raiz de número negativo."
        resultado = math.sqrt(valor)
        return f"A raiz quadrada de {valor} é {resultado}"
    except:
        return "Erro: Use RAIZ <numero>"
        
def inverter_texto(dados):
    # Exemplo: cliente envia "INVERTE ola mundo"
    # Pega tudo após a palavra 'INVERTE '
    texto = dados[8:] 
    return f"Texto invertido: {texto[::-1]}"

s = socket(AF_INET, SOCK_STREAM) 
s.bind(('0.0.0.0', PORT))  #-
s.listen(1)           #-
(conn, addr) = s.accept()  # returns new socket and addr. client 
print(f"Conectado com: {addr[0]}")
while True:                # forever
	data = conn.recv(1024)   # receive data from client
	if not data: break       # stop if client stopped
	comando = data.decode().strip()
	time.sleep(2)
	if comando.startswith("RAIZ"):
		resposta = calcular_raiz(comando)
	elif comando.startswith("INVERTE"):
		resposta = inverter_texto(comando)
	else:
		resposta = "Comando não reconhecido. Use RAIZ ou INVERTE."
	#print(bytes.decode(data))
	conn.send(f"{resposta}\n".encode())
	#conn.send(str.encode(bytes.decode(data)+"*")) # return sent data plus an "*"
conn.close()               # close the connection
