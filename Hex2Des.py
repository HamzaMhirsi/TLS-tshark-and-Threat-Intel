cipher=open("cipher","r")
cipher2=open("cipher2","w")

l=cipher.read().splitlines()
hex_list=[]

for i in l:
	hot=int(i[:8], 16)
	i += ","
	i += str(hot)
	i += ",weak \n"
	hex_list.append(i)

print hex_list

for i in hex_list:
	print i
	cipher2.write(i)
 


cipher2.close()
cipher.close()

