import socket
import threading
import msvcrt

# Define the message to the server
# bytesToSend = str.encode(msgFromClient)
# Buffer size for receiving the datagrams from server
bufferSize = 1024
# Server IP address and Port number
serverAddressPort = ("127.0.0.1", 9999)
# Connect2Server forms the thread - for each connection made to the serve
#Create a socket instance - A datagram socket
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
def Connect2Server():
   while True:

      msgFromClient = input()
      #while not msvcrt.kbhit():
      # msgFromClient = msvcrt.getch()
      bytesToSend = str.encode(msgFromClient)
      # bytesToSend = msgFromClient
      # Send message to server using created UDP socket
      UDPClientSocket.sendto(bytesToSend, serverAddressPort)
      
      # Receive message from the server
      msgFromServer = UDPClientSocket.recvfrom(bufferSize)
      msg = "Message from Server {}".format(msgFromServer[0])
      print(msg)

def recevefromserver():
   while True:
      # Receive message from the server
      msgFromServer = UDPClientSocket.recv(bufferSize)
      msg = "Message from Server {}".format(msgFromServer[0])
      print(msg)

print("Client - Main thread started")  
# ThreadList  = []
# ThreadCount = 20
# Create as many connections as defined by ThreadCount
# for index in range(ThreadCount):
# ThreadInstance = threading.Thread(target=Connect2Server())
# ThreadList.append(ThreadInstance)

threadReceive = threading.Thread(target=recevefromserver())
# ThreadList.append(threadReceive)

# ThreadInstance.start()
threadReceive.start()
# Main thread to wait till all connection threads are complete
# for index in range(2):
#     ThreadList[index].join()