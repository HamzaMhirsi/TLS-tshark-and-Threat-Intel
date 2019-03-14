#!/usr/bin/python

"""
As usual we need to add the following command on the cron that will download the IP file each 5min
# sudo crontab -e
Add the following lines
*/5 * * * * cd  && wget http://osint.bambenekconsulting.com/feeds/c2-ipmasterlist.txt
*/5 * * * * cd  && wget reputation.alienvault.com/reputation.data
*/5 * * * * cd  && wget https://myip.ms/files/blacklist/general/latest_blacklist.txt
"""

c2=open("c2-ipmasterlist.txt","r")
bl=open("latest_blacklist.txt","r")
reputation=open("reputation.data","a")

for line in c2:
	ip = line.split(',')
	reputation.write(ip[0]+ ",c2\n")

for line in bl:
	ip = line.split()
	try:
		reputation.write(ip[0]+ "\n")
	except:
		pass
