# TLS-tshark-and-Threat-Intel-Python

In this repository we will catch some fields on TLS traffic, and use Threat Intel to detect if the packets received may harm our network.

 

# Catch the needed field with tshark command

You can check this article to see how to install tshark https://www.peerlyst.com/posts/send-log-file-over-rsyslog-tls-hamza-m-hirsi?trk=profile_page_overview_panel_posts

 

we will use this command to captures the field needed:

#sudo tshark -i 1 -T fields -e ip.src -e ip.dst -e ssl.handshake.ciphersuites -e ssl.handshake.ciphersuite -e ssl.handshake.certificate -E header=n -E separator="|" >> /home/output.txt

 

- We can now use a simple python script to extract the needed fields from the file "output.txt"

 

# HEX2DES.py

This file will be used to transform the code in HEX of the cipher and we will transform it to DES, as the output of the cipher number in tshark is in DES.

 

# merge.py

This file will prepare a list of blacklisted IP collected from different platform of threat Intel that contain (c2 server, spyware and other malware).

Before executing the code we need to add a cron that will import the list of blacklisted fingerprint each 5min with the following command:

 

#sudo crontab -e

Add the following lines

*/5 * * * * cd && wget http://osint.bambenekconsulting.com/feeds/c2-ipmasterlist.txt

*/5 * * * * cd && wget https://myip.ms/files/blacklist/general/latest_blacklist.txt

*/5 * * * * cd && wget http://reputation.alienvault.com/reputation.data

*/5 * * * * cd && wget python ./merge.py

 

# IPtriage.py

In this file we will use the file generated of blacklisted ip with "merge.py", and check if the ip captures with "ip.dst and ip.src" are blacklisted or not.

 

# cipher2

This is a list of cipher used classed Modern, Intermediate, Old and Weak.

 

# TriagewithCipher.py

This file will detect the weakness of the cipher suites used during the TLS connection, the one proposed by the server "ssl.handshake.ciphersuites" and chose by the client "ssl.handshake.ciphersuite".

 

# certificatetriage.py

This file will take the caught Certificate with the field "ssl.handshake.certificate" with the tshark command, and check if he is black listed or not. Before executing the code we need to add a cron that will import the list of blacklisted fingerprint each 5min with the following command:

 

#sudo crontab -e

Add the following lines

*/5 * * * * cd && wget https://sslbl.abuse.ch/blacklist/sslblacklist.csv

