#!/usr/bin/python

cipher=open("cipher2","r")
server_offer='4865,4867,4866,49195,49199,52393,52392,49196,49200,49162,49161,49171,49172,51,57,47,53,10'
client_choice='49199'

def server_cipher_offer(,server_offer):
	# list the cipher and his strength
	cipher=open("cipher2","r")
	for line in cipher:
	    l=line.split(",")
	    li=server_offer.split(",")
	    for i in li:
		    if i==l[8]:
		    	print "server offer: " + l[1] + " is " + l[9]
	cipher.close()

def client_cipher_choice(,client_choice):
	# list the cipher and his strength
	cipher=open("cipher2","r")
	for line in cipher:
	    l=line.split(",")
	    if client_choice==l[8]:
	    	print "client choose: " + l[1] + " is " + l[9] 
	cipher.close()

server_cipher_offer(cipher,server_offer)
client_cipher_choice(cipher,client_choice)
