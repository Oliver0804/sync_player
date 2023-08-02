import sys
import socket
import subprocess
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, QTabWidget,
                             QInputDialog, QLineEdit, QFileDialog, QLabel)
import netifaces

def getIP(interface):
    if interface in netifaces.interfaces():
        addrs = netifaces.ifaddresses(interface)
        return addrs[netifaces.AF_INET][0]['addr']
    else:
        return "Interface not found"

print()  # 你可以更換 "eth0" 為你的目標網路介面名稱


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        self.tabs = QTabWidget()
        self.tabMaster = QWidget()
        self.tabSlave = QWidget()
        self.tabs.resize(300, 200)

        self.tabs.addTab(self.tabMaster,"Master")
        self.tabs.addTab(self.tabSlave,"Slave")

        self.masterLayout = QVBoxLayout()
        self.labelMasterIP = QLabel("服務器 IP: " + self.getIP())
        self.btnMasterFile = QPushButton('選擇影片', self)
        self.btnMasterFile.clicked.connect(self.masterDialog)
        self.masterLayout.addWidget(self.labelMasterIP)
        self.masterLayout.addWidget(self.btnMasterFile)
        self.tabMaster.setLayout(self.masterLayout)

        self.slaveLayout = QVBoxLayout()
        self.btnSlaveIP = QPushButton('服務器IP', self)
        self.btnSlaveFile = QPushButton('選擇影片', self)
        self.btnSlavePlay = QPushButton('Play Slave Video', self)
        self.btnSlaveIP.clicked.connect(self.slaveIPDialog)
        self.btnSlaveFile.clicked.connect(self.slaveFileDialog)
        self.btnSlavePlay.clicked.connect(self.slavePlay)
        self.slaveLayout.addWidget(self.btnSlaveIP)
        self.slaveLayout.addWidget(self.btnSlaveFile)
        self.slaveLayout.addWidget(self.btnSlavePlay)
        self.tabSlave.setLayout(self.slaveLayout)

        vbox.addWidget(self.tabs)
        self.setLayout(vbox)

        self.setWindowTitle('MPlayer Sync Controller')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def getIP(self):
        
        return getIP("enp7s0")

    def masterDialog(self):
        fname = QFileDialog.getOpenFileName(self, '選擇影片', './')
        if fname[0]:
            subprocess.Popen(['mplayer', '-udp-master', '-udp-ip', '192.168.0.255', str(fname[0])])

    def slaveIPDialog(self):
        text, ok = QInputDialog.getText(self, '服務器 IP', 'Enter IP address:', QLineEdit.Normal)
        if ok and text != '':
            self.slaveIP = str(text)

    def slaveFileDialog(self):
        fname = QFileDialog.getOpenFileName(self, '選擇影片', './')
        if fname[0]:
            self.slaveFile = str(fname[0])

    def slavePlay(self):
        if hasattr(self, 'slaveIP') and hasattr(self, 'slaveFile'):
            subprocess.Popen(['mplayer', '-udp-slave', '-udp-ip', self.slaveIP, self.slaveFile])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
