class RPC:
    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.client_list = dict()
        self.chat_room_list=dict()
        pass
    
    def create_room(self,room_name):
        if room_name in self.chat_room_list:
            print("sala existe")
            return None
        else:
            self.chat_room_list[f"{room_name}"] = Chatroom(room_name)
    
    def join_room(self,username,room_name:str):
        self.chat_room_list[f'{room_name}']
        if(username in self.chat_room_list[f"{room_name}"]):
            return None
        else:
            chat.user_list[f"{username}"]
        
    
    def send_message(self,username,room_name,message,recipient=None):
        pass
    def receive_message(self,username,room_name):
        pass
    def list_room(self):
        print(self.chat_room_list.keys())
    
    def list_clients(self,room_name):
        print(self.client_list)
        pass

class Chatroom:
    def __init__(self,room_name):
        self.room_name = room_name
        self.user_list = dict()
        pass
    def print_users(self):
        print(self.user_list.keys())

rpc = RPC(10,10)
rpc.create_room("sala_1")
rpc.create_room("sala_1")
rpc.list_room()
rpc.join_room("tiago","sala_1")
print(rpc.chat_room_list['sala_1'].print_users())