# TLS-tshark-and-Threat-Intel-Python
In this repository we will catch some fields on TLS traffic, and use Threat Intel to detect if the packets received may harm our network 

# Catch the needed filed with tshark command
You can check this article to see how to install tshark https://www.peerlyst.com/posts/send-log-file-over-rsyslog-tls-hamza-m-hirsi?trk=profile_page_overview_panel_posts

we will use this command to cpatures the filed needed:
#sudo tshark -i 1 -T fields -e ip.src -e ip.dst -e ssl.handshake.ciphersuites -e ssl.handshake.ciphersuite -e ssl.handshake.certificate -E header=n -E separator="|" >> /home/output.txt

- We can now use a simple python script to extract the needed fileds from the file "output.txt"

# HEX2DES.py
This file will be used to transform the code in HEX of the cipher and we wll transform it to DES, as the output of the cipher number in tshark is in DES.

# merge.py
This file will prepare a list of blacklisted IP collected from different platfomr of threat Intel that contain (c2 server, spyware and other malware).

# IPtriage.py
In this file we will use the file generated of blacklisted ip with "merge.py", and check if the ip captures with "ip.dst and ip.src" are blacklisted or not.

# 

# TriagewithCipher.py
This file will detect the weakness of the ciphersuites used during the TLS connection, the one proposed by the server "ssl.handshake.ciphersuites" and choosed by the client "ssl.handshake.ciphersuite".

# certificatetriage.py
