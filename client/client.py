import json
import socket
from audio_client_radio import audio_stream_UDP


# Defining basic variables
s = socket.socket()
host = '192.168.1.107'
port = 9633 

# Connect a Socket
s.connect((host, port))
data = s.recv(1024)

# Get the input of radio
def get_details_radio():
    choice = input("Please select the radio station: ")
    return choice

def get_tcp_server_info_start_udp():
    if len(data) > 0:
        # Print the details of radio station
        print(str(data, "utf-8"))

        # Get the choice of radio stations
        choice_radio_station = get_details_radio()
        
        # Sending the choice 
        s.send(str.encode(choice_radio_station))
        
        # get the welcome message and radio details 
        radio_welcome_message = s.recv(1024)
        radio_ip_details = s.recv(1024)
        
        # Json formatting of data
        radio_ip_details = str(radio_ip_details, "utf-8")
        radio_ip_details = json.loads(radio_ip_details)
        host, port = radio_ip_details['ip'], radio_ip_details['port']
        s.send(str.encode("Close"))

        # Start the Radio
        audio_stream_UDP(host, port)


while True:
    # Play infinite song
    get_tcp_server_info_start_udp()


    


