import json

radio_details_2 = {'ip':'127.0.0.1', 'port':9633}
radio_details_none = {'ip':'', 'port':0}


def radio_select(choice, conn):
    if choice == '1':
        conn.send(str.encode("Welcome to Radio Station 1"))
        conn.send(str.encode(json.dumps(radio_details_2)))
    elif choice == '2':
        conn.send(str.encode("Welcome to Radio Station 2"))
        conn.send(str.encode(json.dumps(radio_details_2)))
    elif choice == '3':
        conn.send(str.encode("Welcome to Radio Station 3"))
        conn.send(str.encode(json.dumps(radio_details_2)))
    else:
        conn.send(str.encode("Please select the appropriate Station"))
        conn.send(str.encode(json.dumps(radio_details_none)))
