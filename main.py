import sys 

class Wifi:
    def __init__(self, argv):
        if len(argv)==2:
            print(argv[1])
        else:
            sys.stderr.write("Usage: {0} <name>\n".format(argv[0])) 

    def speak(self):
        print("Hello from {0}".format(__name__))

import subprocess
class Network:

    def __init__(self):
        self.wifiList = []
        self.activeInterface = ''

        self.getActiveWirelessInterface() 
        self.scanForNetworks()

    def getActiveWirelessInterface(self):
        wirelesscardInterfaceLog = subprocess.run(['iw', 'dev'], stdout=subprocess.PIPE)
        for textRow in wirelesscardInterfaceLog.stdout.decode('utf-8').split('\n'):
            if "Interface" in textRow:
                self.activeInterface = textRow.split(' ')[1]

    def scanForNetworks(self):
        scanResult = subprocess.run(['sudo', 'iw', 'dev', self.activeInterface, 'scan'], stdout=subprocess.PIPE)
        decodedBytecode = scanResult.stdout.decode('utf-8')
        for row  in decodedBytecode.split('\n'):
            if "SSID:" in row:
                self.wifiList.append(row.split(':')[1])

    def connectToWifi(self):
        pass

if __name__ == "__main__":
    network = Network()
    print(network.activeInterface)
