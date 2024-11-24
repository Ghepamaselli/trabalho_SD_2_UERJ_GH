import socket
class Binder:
    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.procedure_list =dict()

    def register_procedure(procedure_name,adress,port):
        server_socket= socket.socket()
        server_socket.connect((adress,port))
        return
    
    def lookup_procedure(self,procedure_name):
        if(procedure_name in self.procedure_list.keys()):
            return True
        return False
    

