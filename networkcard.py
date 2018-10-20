import os

class NetworkCard:
    def __init__(self):
        self.listNetworks(os.listdir('/sys/class/net'))

    def listNetworks(self, networkcardsArr):
        for i in networkcardsArr:
            print(i)


if __name__ == '__main__':
    NetworkCard();
