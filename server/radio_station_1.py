from main_server_radio_multicast import audio_stream_UDP


# Use of different process as in real life there will be different stations
audio_stream_UDP('224.1.1.1', 9633, 5, 'main_radio_station_1_song_')
