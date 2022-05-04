import socket
import threading, wave, time

# Defining basic variables
host_ip = '127.0.0.1'
port = 9633


def audio_stream_UDP():
    # Initalize the buffer size
    BUFF_SIZE = 65536
    
    # Initalize the UDP Socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFF_SIZE)

    # Bind the socket with the address
    server_socket.bind((host_ip, port))
    
    # Convert the data from chunks
    CHUNK = 10 * 1024
   
    # Pointer to the audio file
    wf = wave.open("temp.wav")
    
    # Debug Statment
    print('server listening at', (host_ip, port), wf.getframerate())
 
    # Frame rate setting
    sample_rate = wf.getframerate()

    while True:
        # Recieve Connection Request
        msg, client_addr = server_socket.recvfrom(BUFF_SIZE)
        print('GOT connection from ', client_addr, msg)

        # Send the audio data in 10*1024 chunks
        while True:
            
            # Read data from chunks 
            data = wf.readframes(CHUNK)
            
            # Send data into chunks
            server_socket.sendto(data, client_addr)
            
            # Add delay to data
            time.sleep(0.8 * CHUNK / sample_rate)


# Use of threading for conncurency sending of data
t1 = threading.Thread(target=audio_stream_UDP, args=())
t1.start()
