import threading
from main_server_radio_multicast import audio_stream_UDP


# Use of threading for conncurency sending of data
t1 = threading.Thread(target=audio_stream_UDP, args=('224.1.1.1', 9633, 5))
t1.start()
