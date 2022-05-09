import os
import struct
import keyboard
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
    mreq = struct.pack("=4sl", socket.inet_aton(host_group), socket.INADDR_ANY)
    client_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    # Get data from server and add it to queue
    def getAudioData():
        while True: 
            # Get the data
            try:
                frame = client_socket.recv(65536)
            except:
                os._exit(1)
            q.put(frame)
            print('Queue size...', q.qsize())

    # Threading for perfomance improvement
    t2 = threading.Thread(target=getAudioData, args=())
    t2.start()
    time.sleep(1)
    print('Now Playing...')
    
    # For playing the audio add the data to pyaudio stream from queue
    while True:
        try:
            # Press for pause
            if keyboard.is_pressed('P') or keyboard.is_pressed('p'):
                
                # Wait for restart
                while True:
                    q.get()

                    # Press for restart
                    if keyboard.is_pressed('R') or keyboard.is_pressed('r'):
                            break

                    # Press for close
                    elif keyboard.is_pressed('X') or keyboard.is_pressed('x'):
                            client_socket.close()
            
            # Press for close
            elif keyboard.is_pressed('X') or keyboard.is_pressed('x'):
                
                # Close the client socket
                try:
                    client_socket.close()
                except:
                    os._exit(1)
        except:
            continue 
        
        frame = q.get()
        stream.write(frame)
