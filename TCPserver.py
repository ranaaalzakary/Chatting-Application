import socket
import threading

name= "test"
passw= "test"

def chatting(sock,add):

    username= sock.recv(2024)#The username is recieved from the client
    password= sock.recv(2024)#The password is recieved from the client
    password= password.decode("utf-8")#The password is decoded 
    username= username.decode("utf-8")#The username is decoded

    if username != name:#If the username isnt the same as the hardcoded name mentioned above
            sock.send(str.encode("Username is incorrect"))#It encodes the message "Username is incorrect" and sends it to the client
            sock.close()
    elif password != passw:#If the password isnt the same as the hardcoded passw mentioned above
            sock.send(str.encode("Password is incorrect"))#It encodes the message "Password is incorrect" and sends it to the client
            sock.close()
    else:
            sock.send(str.encode("Login Successful"))#If the username and the password is the same it sends the encoded message "Login Successful" to the client
            while True:
                questions = {"Fees":"New fee structure !! for our Undergraduate and Graduate programs we increased the fee by 10 percent and we are charging 860 AED  per lab course","Transport fee per semester":"AbuDhabi- 11,00 AED  --  Ajman- 7,920 AED -- Sharjah-6,600 AED","Health insurance":"Daman Insurance. for more information please visit our website --->  https://www.rit.edu/","Exams schedule":"Discrete Math 4:00-6:00 - Chemistry 1:40-3:40 -Probability and Statistics 4:00-6:00- Programming for information security 9:00-11:00- Gen&Analy Chem Lab 1 1:40-3:40"}#This contains the questions and the answers     
                print("Got a connection from %s" % str(add))#It prints if the connection is made
                question = sock.recv(2024)#It recieves the question from the client
                question = question.decode('utf-8')#It decodes the question that was received from the client
                print("The question is: ", question)#It prints what the question was 
                if question in questions.keys():#If questions is in the question dictionary key list
                        answer = questions[question]#It fetches the answer value
                        print("The answer is: ", answer)#It prints the asnwer on the server
                        sock.send(f"The answer is: {answer}".encode())#It encodes and sends the answer to the client
                        if question == "done":#If the question done is recieved 
                                print("client:%s has ended connection" %str(add))#It prints that the connection has ended
                break
    sock.close()

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
serversocket.bind((host, port))
serversocket.listen(5)

while True:
    clientsocket, addr = serversocket.accept()
    thread1 = threading.Thread(target=chatting, args=(clientsocket, addr))
    thread1.start()
