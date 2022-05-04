import socket
from radio import radio_select

# Defining basic variables
HOST = '192.168.1.107'
PORT = 9633

Radio = """
        1. Rj Khan
        2. Rj Desai
        3. Rj Stepwell
        
        Pls send channel numbers to listen the stream
"""


# Create a Socket
def create_socket():
    try:
        tcp_socket = socket.socket()
        return tcp_socket
    except socket.error as msg:
        print("Socket Creation error" + str(msg))


# Binding the socket and listening for connections
def bind_socket(s):
    try:
        print("Binding the Port: " + str(PORT))

        s.bind((HOST, PORT))
        s.listen(5)

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()


# Send data to client
def send_data(conn, s):
    try:
        conn.send(str.encode(Radio))
        while True:
            client_response = conn.recv(1024)
            client_response = str(client_response, 'utf-8')
            select_choice = client_response[len(client_response) - 1]
            if select_choice is None or select_choice == '\n':
                continue
            radio_select(select_choice, conn)
            if client_response == "Close":
                break
        conn.close()
    except KeyboardInterrupt:
        exit()


# Establish connection with a client (socket must be listening)
def socket_accept(s):
    conn, address = s.accept()
    print("Connection has been established! |" + " IP: " + address[0] + " | Port: " + str(address[1]))
    send_data(conn, s)


main_socket = create_socket()
bind_socket(main_socket)
socket_accept(main_socket)
