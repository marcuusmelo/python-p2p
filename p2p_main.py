'''
Python P2P main script
'''

from constants import *
from client import Client
from server import Server


"""
    This class will take care of converting client to server
"""
class p2p:
    # make ourself the default peer
    peers = ['127.0.0.1']


def main():
    # if the server breks we try to make a client a new server

    msg = file_io.convert_to_bytes()
    while True:
        try:
            print("-" * 21 + "Trying to connect" + "-" * 21)
            # sleep a random time between 1 - 2 seconds
            time.sleep(randint(RAND_TIME_START,RAND_TIME_END))
            
            for peer in p2p.peers:
                # become the client
                try:
                    client = Client(peer)
                except KeyboardInterrupt:
                    sys.exit()
                except Exception as e:
                    print('Client Exception')
                    print(e)
                    pass


                # become the server
                try:
                    server = Server(msg)
                except KeyboardInterrupt:
                    sys.exit()
                except:
                    pass

        except KeyboardInterrupt as e:
            sys.exit(0)

if __name__ == "__main__":
    main()