import json
import socket
import threading    
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

# Select new radio
def get_close_connect_get_new_radio():
    choice = input("""Would you like to continue with the radio station?
                    1. Yes
                    2. No
        """)
    return choice

while True:
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
        
        # Select whether to change the choice of station
        choice_close_or_retry = get_close_connect_get_new_radio()
        if choice_close_or_retry == '1':
            s.send(str.encode("Close"))
            
            # Start the Radio
            t1 = threading.Thread(target=audio_stream_UDP, args=(host, port))
            t1.start()
            
            break
        else:
            continue

    


