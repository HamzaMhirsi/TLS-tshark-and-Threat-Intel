#!/usr/bin/python

# For selfsigned certificates: we will have always one certificate in the path:
# We suppose that we have only one certificate

# x509sat_uTF8String is the rdnSequence captured with tshark

x509sat_uTF8String='KAR,BAN,SMSC,QA,BAWMASHBIJ.corp.smsc.com,KAR,BAN,SMSC,QA,BAWMASHBIJ.corp.smsc.com'

def selfsigned():
	check=x509sat_uTF8String.split(',')
	number=len(check)
	i=0
	selfsigned=True
	while i < number/2:
		if check[i] != check[number/2+i]:
			selfsigned=False
		i +=1
	print selfsigned
	return selfsigned

selfsigned()