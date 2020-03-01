from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.myButton = QtWidgets.QPushButton(self)
        self.myButton.setObjectName("myButton")
        self.myButton.setText("Test")
        self.myButton.clicked.connect(self.msg)

    def msg(self):


        fileName1, filetype = QFileDialog.getOpenFileName(self,
                                                          "选取文件",

                                                          )  # 设置文件扩展名过滤,注意用双分号间隔
        print(fileName1, filetype)

        fileName2, ok2 = QFileDialog.getSaveFileName(self,
                                                     "文件保存")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()
    sys.exit(app.exec_())