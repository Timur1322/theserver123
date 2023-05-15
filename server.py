# import socket


# server = '10.0.1.12'
# sport = 9999

# server_socket = socket.socket()
# connect = server_socket.bind((server, sport))
# server_socket.listen(1)
# while True:
#         client_socket, addr = server_socket.accept()
#         print 'Connection established from: ', addr

#         data = client_socket.recv(1)
#         print 'Received data: ', data[:100]
        
#         # Vulnerable code - no bounds checking on received data
#         response = 'Hello, ' + data.decode()
#         client_socket.send(response.encode())

#         client_socket.close()

import socket

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to a specific IP address and port
    server_address = (socket.gethostbyname_ex(socket.gethostname())[-1][-1], 9999)
    server_socket.bind(server_address)
    
    # Listen for incoming connections
    server_socket.listen(1)
    print 'Server is listening on {}:{}'.format(*server_address)
    
    while True:
        # Wait for a client to connect
        print 'Waiting for a connection...'
        client_socket, client_address = server_socket.accept()
        print 'Connected to {}:{}'.format(*client_address)
        
        # Receive and process data from the client
        data = client_socket.recv(300000000)
        if data:
            # Print the received data
            print 'Received data:', data
            
            # Send a response back to the client
            response = 'Server received your message: {}'.format(data)
            client_socket.sendall(response)
            
        # Close the connection with the client
        client_socket.close()
        print 'Connection with {}:{} closed'.format(*client_address)

# Start the server
start_server()

