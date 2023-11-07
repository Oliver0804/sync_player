import sys
import socket
import subprocess
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, QTabWidget,
                             QInputDialog, QLineEdit, QFileDialog, QLabel, QCheckBox, QTextBrowser)
from PyQt5.QtCore import QUrl
import netifaces


from zeroconf import ServiceBrowser, Zeroconf, ServiceInfo



def get_local_ip():
    for interface in netifaces.interfaces():
        addrs = netifaces.ifaddresses(interface)
        if netifaces.AF_INET in addrs:
            for addr in addrs[netifaces.AF_INET]:
                ip = addr['addr']
                if ip.startswith("10.") or ip.startswith("192."):
                    return ip
    return "No appropriate local IP found."



def getIP(interface):
    if interface in netifaces.interfaces():
        addrs = netifaces.ifaddresses(interface)
        return addrs[netifaces.AF_INET][0]['addr']
    else:
        return "Interface not found"

class MyListener:
    def remove_service(self, zeroconf, type, name):
        print(f"Service {name} removed")

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        print(f"Service {name} added, service info: {info}")

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        self.tabs = QTabWidget()
        self.tabMaster = QWidget()
        self.tabSlave = QWidget()
        self.tabInstruction = QWidget()

        self.tabs.addTab(self.tabMaster, "Master")
        self.tabs.addTab(self.tabSlave, "Slave")
        self.tabs.addTab(self.tabInstruction, "使用說明")

        # Master tab
        self.masterLayout = QVBoxLayout(self.tabMaster)
        self.labelMasterIP = QLabel("服務器 IP: ")
        self.lineEditMasterIP = QLineEdit(self.getIP())
        self.btnMasterFile = QPushButton('選擇影片', self)
        self.btnMasterFile.clicked.connect(self.masterDialog)
        self.checkboxLoopMaster = QCheckBox("循環播放")
        self.checkboxMdns = QCheckBox("mDNS")
        self.masterLayout.addWidget(self.labelMasterIP)
        self.masterLayout.addWidget(self.lineEditMasterIP)
        self.masterLayout.addWidget(self.btnMasterFile)
        self.masterLayout.addWidget(self.checkboxLoopMaster)
        self.masterLayout.addWidget(self.checkboxMdns)

        # Slave tab
        self.slaveLayout = QVBoxLayout(self.tabSlave)
        self.btnSlaveIP = QPushButton('服務器 IP', self)
        self.btnSlaveFile = QPushButton('選擇影片', self)
        self.btnSlavePlay = QPushButton('播放影片', self)
        self.checkboxLoopSlave = QCheckBox("循環播放")
        self.btnSlaveIP.clicked.connect(self.slaveIPDialog)
        self.btnSlaveFile.clicked.connect(self.slaveFileDialog)
        self.btnSlavePlay.clicked.connect(self.slavePlay)
        self.btnSlaveFile.setEnabled(False)  # 禁用選擇影片按鈕
        self.btnSlavePlay.setEnabled(False)  # 禁用播放影片按鈕

        self.slaveLayout.addWidget(self.btnSlaveIP)
        self.slaveLayout.addWidget(self.btnSlaveFile)
        self.slaveLayout.addWidget(self.btnSlavePlay)
        self.slaveLayout.addWidget(self.checkboxLoopSlave)

        # Instruction tab
        self.instructionLayout = QVBoxLayout(self.tabInstruction)
        self.textBrowser = QTextBrowser()
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setHtml("""
使用方法：<br>
1. 開啟程式後，將會看到三個分頁：Master、Slave 和 使用說明。<br>
2. Master 分頁：<br>
   - 會顯示當前主機的 IP 地址。
   - 點擊 '選擇影片' 按鈕，選擇你要播放的影片檔案。
   - '循環播放' 的核取方塊：選擇影片並點擊播放後，將無法更改循環播放的設定。<br>
3. Slave 分頁：<br>
   - 點擊 '服務器 IP' 按鈕，輸入 Master 主機的 IP 地址。
   - 點擊 '選擇影片' 按鈕，選擇你要播放的影片檔案。
   - '播放影片' 按鈕：與 Master 主機同步並開始播放影片。
   - '循環播放' 的核取方塊：選擇影片並點擊播放後，將無法更改循環播放的設定。<br>
影片播放控制鍵：<br>
- 空白鍵：暫停/播放<br>
- 方向鍵左/右：快進/倒帶<br>
- F：全螢幕切換<br>
<a href='https://github.com/Oliver0804/sync_player'>程式碼連結</a>
        """)
        self.instructionLayout.addWidget(self.textBrowser)

        vbox.addWidget(self.tabs)
        self.setLayout(vbox)

        self.setWindowTitle('口丁 MPlayer Sync Controller v1.0')
        self.setGeometry(400, 300, 400, 200)
        self.show()
    

    def getIP(self):
        #return getIP("enp7s0")
        return get_local_ip()

    def masterDialog(self):
        fname = QFileDialog.getOpenFileName(self, '選擇影片', './videos')
        if fname[0]:
            loopCmd_1 = '-loop' if self.checkboxLoopMaster.isChecked() else ''
            loopCmd_2 = '0' if self.checkboxLoopMaster.isChecked() else ''
            server_ip = self.lineEditMasterIP.text()
            subprocess.Popen(['mplayer', '-udp-master', '-udp-ip', server_ip, str(fname[0]), loopCmd_1, loopCmd_2])
            self.checkboxLoopMaster.setEnabled(False)

    def slaveIPDialog(self):
        text, ok = QInputDialog.getText(self, '服務器 IP', 'Enter IP address:', QLineEdit.Normal)
        if ok and text != '127.0.0.1':
            self.btnSlaveFile.setEnabled(True)  # 禁用選擇影片按鈕
            self.slaveIP = str(text)

    def slaveFileDialog(self):
        fname = QFileDialog.getOpenFileName(self, '選擇影片', './videos')
        if fname[0]:
            self.btnSlavePlay.setEnabled(True)  # 禁用播放影片按鈕

            self.slaveFile = str(fname[0])

    def slavePlay(self):
        if hasattr(self, 'slaveIP') and hasattr(self, 'slaveFile'):
            loopCmd_1 = '-loop' if self.checkboxLoopSlave.isChecked() else ''
            loopCmd_2 = '0' if self.checkboxLoopSlave.isChecked() else ''
            subprocess.Popen(['mplayer', '-udp-slave', '-udp-ip', self.slaveIP, self.slaveFile, loopCmd_1, loopCmd_2])
            self.checkboxLoopSlave.setEnabled(False)
            
    def register_service(self):
        local_ip = socket.inet_aton(get_local_ip())
        service_name = "MyServiceName._http._tcp.local."
        service_port = 8000  # 您应用的端口号

        self.service_info = ServiceInfo(
            "_http._tcp.local.",
            service_name,
            addresses=[local_ip],
            port=service_port,
            properties={},
        )

        self.zeroconf = Zeroconf()
        self.zeroconf.register_service(self.service_info)

    def unregister_service(self):
        if hasattr(self, 'zeroconf'):
            self.zeroconf.unregister_service(self.service_info)
            self.zeroconf.close()

    def start_service_discovery(self):
        self.zeroconf = Zeroconf()
        self.listener = MyListener()
        self.browser = ServiceBrowser(self.zeroconf, "_http._tcp.local.", self.listener)
    
    def closeEvent(self, event):
        self.unregister_service()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    
    sys.exit(app.exec_())
