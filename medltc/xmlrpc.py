import xmlrpclib

def get_server_proxy():
    return xmlrpclib.ServerProxy("http://192.168.1.99:13333")
