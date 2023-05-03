import socket

target_host = input("Enter the target host: ")
target_port = input("Enter the target port(s) separated by comma: ")

# Split target ports by comma
target_ports = target_port.split(',')

# Loop over target ports
for port in target_ports:
    try:
        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set a timeout of 1 second
        client_socket.settimeout(1)

        # Connect to the target host and port
        client_socket.connect((target_host, int(port)))

        # Print the port is open
        print("Port {} is open".format(port))

        # Close the socket
        client_socket.close()

    except socket.timeout:
        # Print a timeout message
        print("Port {} timed out".format(port))

    except ConnectionRefusedError:
        # Print a connection refused message
        print("Port {} is closed".format(port))
