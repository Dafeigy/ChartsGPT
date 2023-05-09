import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import uic

# 动态载入
class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # PyQt5
        self.ui=uic.loadUi("untitled.ui")
        # 这里与静态载入不同，使用 self.ui.show()
        # 如果使用 self.show(),会产生一个空白的 MainWindow
        self.ui.show()

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=mainwindow()
    sys.exit(app.exec_())