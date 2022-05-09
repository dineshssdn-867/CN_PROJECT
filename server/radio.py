import json

radio_details_1 = {'ip':'224.1.1.1', 'port':9633, 'name':'Rj Khan', 'description':'We are khan studios'}
radio_details_2 = {'ip':'224.1.1.2', 'port':9633, 'name':'Rj Desai', 'description':'We are desai studios'}
radio_details_3 = {'ip':'224.1.1.3', 'port':9633, 'name':'Rj Stepwell', 'description':'We are stepwell studios'}
radio_details_none = {'ip':'', 'port':0}


def radio_select(choice, conn):
    if choice == '1':
        conn.send(str.encode("Welcome to Radio Station 1"))
        conn.send(str.encode(json.dumps(radio_details_1)))
    elif choice == '2':
        conn.send(str.encode("Welcome to Radio Station 2"))
        conn.send(str.encode(json.dumps(radio_details_2)))
    elif choice == '3':
        conn.send(str.encode("Welcome to Radio Station 3"))
        conn.send(str.encode(json.dumps(radio_details_3)))
    else:
        conn.send(str.encode("Please select the appropriate Station"))
        conn.send(str.encode(json.dumps(radio_details_none)))
