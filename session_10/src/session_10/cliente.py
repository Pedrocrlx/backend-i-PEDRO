import socket

# Configurar o socket do servidor
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('localhost', 8080))
servidor.listen(5)
print("Servidor ativo no endpoint localhost:8080")


def processar_cliente(conn):
    # Receber a mensagem do cliente
    dados = conn.recv(1024).decode('utf-8')

    if dados == "endpoint1":
        resposta = "Você acessou o endpoint lógico 1!"
    elif dados == "endpoint2":
        resposta = "Você acessou o endpoint lógico 2!"
    else:
        resposta = "Endpoint desconhecido!"

    # Enviar a resposta ao cliente
    conn.sendall(resposta.encode('utf-8'))


# Aceitar conexões
while True:
    client_connection, client_address = servidor.accept()
    with client_connection:
        # Receive the request data (limit to 1024 bytes for simplicity)
        request_data = client_connection.recv(1024).decode('utf-8')
        print("Received request:")
        print(request_data)

        # Construct a simple HTTP response
        http_response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html; charset=utf-8\r\n"
            "\r\n"
            f"<html><body><h1>{request_data}Hello, HTTP!</h1></body></html>"
        )

        # Send the HTTP response back to the client
        client_connection.sendall(http_response.encode('utf-8'))
