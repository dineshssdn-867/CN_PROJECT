import struct
import socket
import threading, pyaudio, time, queue

# Initalzing the queue for storing audio data
q = queue.Queue(maxsize=2000)


def audio_stream_UDP(host_group, port_group):    
    # Initalize the UDP Socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Initalize pyaudio for pre-processing audio
    p = pyaudio.PyAudio()
    CHUNK = 10 * 1024
    stream = p.open(format=p.get_format_from_width(2),
                    channels=2,
                    rate=44100,
                    output=True,
                    frames_per_buffer=CHUNK)

    client_socket.bind(("", port_group))
    mreq = struct.pack("4sl", socket.inet_aton(host_group), socket.INADDR_ANY)
    client_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    # Get data from server and add it to queue
    def getAudioData():
        while True:
            frame = client_socket.recv(65536)
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
