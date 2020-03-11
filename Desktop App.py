from PyQt5.QtWidgets import QWidget , QApplication, QLabel, QLineEdit, QPushButton
import sys
import json
from web3 import Web3

class Display(QWidget):

    def __init__(self):
        super(Display,self).__init__()
        self.ll1 = QLabel(self)
        self.ll1.setGeometry(150, 30, 150, 30)
        self.ll1.setText("From Account")
        self.ll3 = QLabel(self)
        self.ll3.setGeometry(150, 130, 150, 30)
        self.ll3.setText("To Account")
        self.frameLine3 = QLineEdit(self)
        self.frameLine3.setPlaceholderText('Private Key')
        self.frameLine3.setGeometry(550, 30, 135, 30)
        self.frameLine = QLineEdit(self)
        self.frameLine.setPlaceholderText('Public key acc1')
        self.frameLine.setGeometry(265, 30, 135, 30)
        self.frameLine2 = QLineEdit(self)
        self.frameLine2.setPlaceholderText('Public Key acc2')
        self.frameLine2.setGeometry(265, 130, 135, 30)
        self.frameLine4 = QLineEdit(self)
        self.frameLine4.setPlaceholderText('Amount')
        self.frameLine4.setGeometry(500, 130, 135, 30)
        self.setButton = QPushButton('Set', self)
        self.setButton.setGeometry(300, 330, 100, 30)
        self.setButton.clicked.connect(self.input)
        self.ll2 = QLabel(self)
        self.ll2.setGeometry(150, 230, 150, 30)
        self.ll2.setText("Output")
        self.showMaximized()

    def input(self):
        acc1 = self.frameLine.text()
        p = str(self.frameLine3.text())
        acc2 = str(self.frameLine2.text())
        amount = int(self.frameLine4.text())
        url = "https://ropsten.infura.io/v3/13e428f26d884948a3c24c10d237bbca"
        web3 = Web3(Web3.HTTPProvider(url))
        print(web3.isConnected())
        abi = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"tokens","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"from","type":"address"},{"name":"to","type":"address"},{"name":"tokens","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"_totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"tokenOwner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"acceptOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeSub","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":false,"inputs":[{"name":"to","type":"address"},{"name":"tokens","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeDiv","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"tokens","type":"uint256"},{"name":"data","type":"bytes"}],"name":"approveAndCall","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeMul","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[],"name":"newOwner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"tokenAddress","type":"address"},{"name":"tokens","type":"uint256"}],"name":"transferAnyERC20Token","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"tokenOwner","type":"address"},{"name":"spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeAdd","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":false,"inputs":[{"name":"_newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"tokens","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"tokenOwner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"tokens","type":"uint256"}],"name":"Approval","type":"event"}]')
        address = Web3.toChecksumAddress('0x24d3f207d9a8071e806e189fa268fda56f05c5f7')
        contract = web3.eth.contract(address=address, abi=abi)
        balance1 = contract.functions.balanceOf(str(acc1)).call()
        balance2 = contract.functions.balanceOf(str(acc2)).call()
        print(web3.fromWei(balance1, 'ether'))
        print(web3.fromWei(balance2, 'ether'))
        nonce = web3.eth.getTransactionCount(acc1)
        tx = contract.functions.transfer(acc2, web3.toWei(amount,'ether'), ).buildTransaction({'nonce': nonce, 'value': web3.toWei(0, 'ether'), 'gas': 2000000, 'gasPrice': web3.toWei('50', 'gwei'), })
        signed_tx = web3.eth.account.signTransaction(tx, p)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print(tx_hash)
        balance1 = contract.functions.balanceOf(str(acc1)).call()
        balance2 = contract.functions.balanceOf(str(acc2)).call()
        print(web3.fromWei(balance1, 'ether'))
        print(web3.fromWei(balance2, 'ether'))

def main():
    app = QApplication(sys.argv)
    ex = Display()
    ex.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

