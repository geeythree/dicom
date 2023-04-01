import gdcm

def c_echo(remote_host, remote_port, ae_title):

    

    network = gdcm.CompositeNetworkFunctions()#
    connect = network.CEcho('127.0.0.1', 4242)
    print(connect)

def c_find(remote_host, remote_port, query):
    pass