import socket
import wave, time


def audio_stream_UDP(host_group, port_group, ttl):    
    # Initalize the UDP Socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    server_socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
    
    # Convert the data from chunks
    CHUNK = 10 * 1024
    while True:
        # Pointer to the audio file
        wf = wave.open("main.wav")
        
        # Debug Statment
        print('server multicasting at', (host_group, port_group), wf.getframerate())
    
        # Frame rate setting
        sample_rate = wf.getframerate()

        # Send the audio data in 10*1024 chunks
        while True:
            
            # Read data in chunks 
            data = wf.readframes(CHUNK)
            
            # Send data into chunks
            server_socket.sendto(data,(host_group, port_group))
            
            # Add delay to data
            time.sleep(0.8 * CHUNK / sample_rate)
