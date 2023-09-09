import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("game.ui", self)  # Make sure to place your actual UI file here

        self.player = 'X'
        self.first.clicked.connect(lambda: self.options(self.first))
        self.second.clicked.connect(lambda: self.options(self.second))
        self.third.clicked.connect(lambda: self.options(self.third))
        self.fourth.clicked.connect(lambda: self.options(self.fourth))
        self.fifth.clicked.connect(lambda: self.options(self.fifth))
        self.sixth.clicked.connect(lambda: self.options(self.sixth))
        self.seventh.clicked.connect(lambda: self.options(self.seventh))
        self.eight.clicked.connect(lambda: self.options(self.eight))
        self.nine.clicked.connect(lambda: self.options(self.nine))
        self.reset.clicked.connect(self.replay)


    def disable(self):
        self.first.setDisabled(True)
        self.second.setDisabled(True)
        self.third.setDisabled(True)
        self.fourth.setDisabled(True)
        self.fifth.setDisabled(True)
        self.sixth.setDisabled(True)
        self.seventh.setDisabled(True)
        self.eight.setDisabled(True)
        self.nine.setDisabled(True)
    
    
    def replay(self):
        self.first.setEnabled(True)
        self.second.setEnabled(True)
        self.third.setEnabled(True)
        self.fourth.setEnabled(True)
        self.fifth.setEnabled(True)
        self.sixth.setEnabled(True)
        self.seventh.setEnabled(True)
        self.eight.setEnabled(True)
        self.nine.setEnabled(True)

        self.first.setText('')
        self.second.setText('')
        self.third.setText('')
        self.fourth.setText('')
        self.fifth.setText('')
        self.sixth.setText('')
        self.seventh.setText('')
        self.eight.setText('')
        self.nine.setText('')
        self.label.setText(f"{self.player}'s Turn")


    def switch_player(self):
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'

    def update_btn(self):
        self.btn_1 = self.first.text()
        self.btn_2 = self.second.text()
        self.btn_3 = self.third.text()
        self.btn_4 = self.fourth.text()
        self.btn_5 = self.fifth.text()
        self.btn_6 = self.sixth.text()
        self.btn_7 = self.seventh.text()
        self.btn_8 = self.eight.text()
        self.btn_9 = self.nine.text()

    def win_check(self):
        # self.update_btn()
        if self.btn_1 == self.btn_2 == self.btn_3 != "":
            self.disable()
            self.label.setText(f"{self.player} won")
        elif self.btn_4 == self.btn_5 == self.btn_6 != "":
            self.disable()
            self.label.setText(f"{self.player} won")
        elif self.btn_7 == self.btn_8 == self.btn_9 != "":
            self.disable()
            self.label.setText(f"{self.player} won")

        elif self.btn_1 == self.btn_4 == self.btn_7 != "":
            self.disable()
            self.label.setText(f"{self.player} won")
        elif self.btn_2 == self.btn_5 == self.btn_8 != "":
            self.disable()
            self.label.setText(f"{self.player} won")
        elif self.btn_3 == self.btn_6 == self.btn_9 != "":
            self.disable()
            self.label.setText(f"{self.player} won")

        elif self.btn_1 == self.btn_5 == self.btn_9 != "":
            self.disable()
            self.label.setText(f"{self.player} won")
        elif self.btn_3 == self.btn_7 == self.btn_5 != "":
            self.disable()
            self.label.setText(f"{self.player} won")

        elif self.btn_1 != '' and self.btn_2 != '' and self.btn_3 != '' and self.btn_4 != '' and self.btn_5 != '' and self.btn_6 != '' and self.btn_7 != '' and self.btn_8 != '' and self.btn_9 != '':
            self.label.setText('Draw')

        
    def options(self, player):
        player.setDisabled(True)
        player.setText(self.player)
        self.update_btn()
        self.win_check()
        self.switch_player()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
