printable="Google Inc,Google Internet Authority G2,GeoTrust Inc.,GeoTrust Global CA,Google Inc,Google Internet Authority G2,Equifax,Equifax Secure Certificate Authority,GeoTrust Inc.,GeoTrust Global CA" 
#printable="Google Trust Services,Google Internet Authority G3,GlobalSign Root CA - R2,GlobalSign,GlobalSign,Google Trust Services,Google Internet Authority G3"
d="19-03-26,19-06-18,17-06-15,21-12-15,17-06-15,21-12-15"
date=d.split(',')
printable_string=printable.split(',')

compte = {}.fromkeys(printable_string,0)
for valeur in printable_string:
	compte[valeur] += 1

print compte
redandance=0
for key, value in compte.iteritems():
	if value==2:
		redandance+=1
		
if redandance>=4 and len(date)==6:
	print "chain of the three certificate is verified"
elif redandance>=2 and len(date)==4:
	print "chain of the both certificate is verified"
else:
	print "chain of certificate is not verified"