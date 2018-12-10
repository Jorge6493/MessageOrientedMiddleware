import socketserver
import threading
import socket
# Create a tuple with IP Address and Port Number
ServerAddress = ("127.0.0.1", 9999)
# Subclass the DatagramRequestHandler
client_list = {""}
client_list.clear()
# elinput = 
class MyUDPRequestHandler(socketserver.DatagramRequestHandler):
    # Override the handle() method
    def handle(self):
        # Receive and print the datagram received from client
        
        client_list.add(self.client_address)
        print("Recieved one request from {}:{}".format(self.client_address[0],self.client_address[1]))
        datagram = self.rfile.readline().strip()
        print("Datagram Recieved from client is:".format(datagram))
        print(datagram)  
        # Print the name of the thread
        print("Thread Name:{}".format(threading.current_thread().name))
        # Send a message to the client
        self.wfile.write(datagram)
        print("count client_list")
        print(len(client_list))
        for x in client_list:
            print(x)
        
        # if elinput == "1":
        #     self.wfile.write("hihowareya")
        

        # data = self.request[0].strip()
        # socket = self.request[1]
        # print("{}:{} wrote:".format(self.client_address[0],self.client_address[1]))
        # print(data)
        # socket.sendto(data.upper(), self.client_address)

# Create a Server Instance
# UDPServerObject = socketserver.ThreadingUDPServer(ThreadingMixIn, UDPServer)
def sendmessage():
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    while True:
       msg = input()
       for x in client_list:
           sock.sendto(str.encode(msg),  x)

if __name__ == "__main__":
    
    UDPServerObject = socketserver.ThreadingUDPServer(ServerAddress,MyUDPRequestHandler,True)
    # UDPServerObject.allow_reuse_address
    with UDPServerObject:
        server_thread = threading.Thread(target=UDPServerObject.serve_forever)
        server_thread.daemon = True
        server_thread.start()
        message_thread = threading.Thread(target=sendmessage)
        message_thread.start()
        server_thread.join()
    # Make the server wait forever serving connections
    # UDPServerObject.serve_forever()
  