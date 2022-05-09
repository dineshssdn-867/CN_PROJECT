import socket
import wave, time


def audio_stream_UDP(host_group, port_group, ttl):    
    # Initalize the UDP Socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    server_socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
    
    # Convert the data from chunks
    CHUNK = 10 * 1024
    iterator = 1
    while True:
        song_name_current = 'main_radio_station_1_song_'+str(iterator)
        song_name_next = 'main_radio_station_1_song_'+str(iterator+1)
        
        # Pointer to the audio file
        wf = wave.open(song_name_current+'.wav')
        
        # Debug Statment
        print('server multicasting at', (host_group, port_group), wf.getframerate())
    
        # Frame rate setting
        sample_rate = wf.getframerate()

        server_socket.sendto(str.encode("The current song is " + song_name_current),(host_group, port_group))
        server_socket.sendto(str.encode("The next song is" + song_name_next),(host_group, port_group))
        
        
        # Send the audio data in 10*1024 chunks
        while True:
            
            # Read data in chunks 
            data = wf.readframes(CHUNK)

            if len(data) == 0:
                iterator += 1
                if iterator > 2:
                    iterator = 1
                break
            
            # Send data into chunks
            server_socket.sendto(data,(host_group, port_group))
            
            # Add delay to data
            time.sleep(0.8 * CHUNK / sample_rate)
