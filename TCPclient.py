import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
s.connect((host, port))

username= input("Username: ")#Takes the username from the user
s.send(str.encode(username))#Encodes the username and sends it to the server
password= input("Password: ")#Takes the password from the user
s.send(str.encode(password))#Encodes the password and sends it to the server
response= s.recv(2024)#Recieves the response from the server 
response= response.decode()#Decodes the response 
print(response)#Prints the response


if response == "Login Successful":#If the response is Login Successful
    while True:
        msg=input("Enter your Question: ")#Asks the user to enter the question
        s.send(msg.encode("utf-8"))#Encodes the question and sends it to the server
        if msg=="done":
            break
        msg=s.recv(2024)
        print (msg.decode('utf-8'))
else:
    exit
