# python-p2p
P2P Application with Python


# Python-P2P Logic
P2P: all users are client and server

1. Tries to connect to a PEER (client mode)

+ IF connection is successful: listen to PEER (client mode)
+ IF connection is unsuccessful: become a server mode

2. Start server mode

3. Wait for a peer to connect (server mode)

4. Send data to peer (server mode)


# Usage

1. create a Python 3.7 virtualenv
`$ virtualenv --python=python3 env-p2p`

2. source virtualenv
`$ source env-p2p/bin/activate`

3. Install dependencies, if any
`$ pip install requirements.txt`

4. Execute p2p_main
`$ python p2p_main.py`


# Console Messages
1. Attempt to connect to a PEER (client mode)
- - - - - TRYING TO CONNECT

2. Starting server mode
- - - - - SERVER RUNNING

3. Receiving data from PEER (client mode)
- - - - - RECEIVING MESSAGE


Based on 
https://medium.com/@amannagpal4/how-to-create-your-own-decentralized-file-sharing-service-using-python-2e00005bdc4a
https://github.com/Ezi0aaudit0re/P2P-music-sharing
