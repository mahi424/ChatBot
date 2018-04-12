import aiml
import os
# import socketserver
import SocketServer

kernel = aiml.Kernel()
path = os.path.dirname(os.path.realpath(__file__))
if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
	kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")#add your files with learn
	kernel.saveBrain("bot_brain.brn")


HOST, PORT = "localhost", 9998

# class MyTCPHandler(socketserver.BaseRequestHandler):
class MyTCPHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        self.data = str(self.request.recv(1024).strip().decode())
        print("From "+str(self.client_address[0])+":");
        print("Query    : "+str(self.data));
        message=self.data;
        if message == "save":
            bot_response="Saved";
            kernel.saveBrain("bot_brain.brn")
        else:
            bot_response = kernel.respond(message)
        print("Response : "+str(bot_response));
        print("=====================");
        self.request.sendall(bot_response.encode())


# setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server = SocketServer.TCPServer((HOST,PORT ), MyTCPHandler)
server.serve_forever()
