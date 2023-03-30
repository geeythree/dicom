import gdcm
import socket

def c_echo(remote_host, remote_port):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the remote host and port
    server_address = (remote_host, remote_port)
    sock.connect(server_address)

    # Create a GDCM network object
    network = gdcm.Network()

    # Create a CEcho object
    echo = gdcm.CEcho()

    # Set the transfer syntax to use
    echo.SetTransferSyntax(gdcm.TransferSyntax.ImplicitVRLittleEndian)

    # Send the C-ECHO request and wait for the response
    response = network.CEcho(echo, sock)

    # Close the socket
    sock.close()

    # Check if the C-ECHO was successful
    if response.GetCEchoStatus() == gdcm.CEchoStatus.Success:
        print("C-ECHO successful!")
    else:
        print("C-ECHO failed!")

def c_find(remote_host, remote_port, query):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the remote host and port
    server_address = (remote_host, remote_port)
    sock.connect(server_address)

    # Create a GDCM network object
    network = gdcm.Network()

    # Create a CFind object
    find = gdcm.CFind()

    # Set the transfer syntax to use
    find.SetTransferSyntax(gdcm.TransferSyntax.ExplicitVRLittleEndian)

    # Set the query
    find.SetQuery(query)

    # Send the C-FIND request and iterate over the responses
    responses = network.CFind(find, sock)
    for response in responses:
        if response.GetCFindStatus() == gdcm.CFindStatus.Pending:
            continue
        elif response.GetCFindStatus() == gdcm.CFindStatus.Success:
            # Process the response
            dataset = response.GetDataSet()
            print("Received response:")
            for tag in dataset.GetKeys():
                element = dataset.GetDataElement(tag)
                print("{}: {}".format(tag, element.GetByteValue()))
        else:
            print("C-FIND failed!")

    # Close the socket
    sock.close()

if __name__ == '_main__':
    remote_host = '127.0.0.1'
    remote_port = 104
    
    c_echo(remote_host, remote_port)

    query = gdcm.DataSet()
    query.Insert(gdcm.Tag(0x0008, 0x0052), gdcm.DataElement(gdcm.Tag(0x0008, 0x0052)))
    
    c_find(remote_host, remote_port, query)