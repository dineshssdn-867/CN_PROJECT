import socket
import threading, wave, pyaudio, time, queue

# Initalzing the queue for storing audio data
q = queue.Queue(maxsize=2000)


def audio_stream_UDP(host_ip, port):
    # Initalize the buffer size
    BUFF_SIZE = 65536
    
    # Initalize the UDP Socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFF_SIZE)
    
    # Initalize pyaudio for pre-processing audio
    p = pyaudio.PyAudio()
    CHUNK = 10 * 1024
    stream = p.open(format=p.get_format_from_width(2),
                    channels=2,
                    rate=44100,
                    output=True,
                    frames_per_buffer=CHUNK)

    # Send message to UDP socket to get connection from server
    message = b'Hello Radio'
    client_socket.sendto(message, (host_ip, port))

    # Get data from server and add it to queue
    def getAudioData():
        while True:
            frame, _ = client_socket.recvfrom(BUFF_SIZE)
            q.put(frame)
            print('Queue size...', q.qsize())

    # Threading for perfomance improvement
    t1 = threading.Thread(target=getAudioData, args=())
    t1.start()
    time.sleep(1)
    print('Now Playing...')
    
    # For playing the audio add the data to pyaudio stream from queue
    while True:
        frame = q.get()
        stream.write(frame)

    client_socket.close()
    print('Audio closed')
    os._exit(1)
