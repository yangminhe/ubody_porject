import sys
from PyQt5.QtGui import QIcon, QFont

from PyQt5.QtWidgets import QWidget, QApplication, QToolTip, QPushButton, QHBoxLayout

class IconClass(QWidget):
    def __init__(self,parent=None):
         super(IconClass,self).__init__(parent)
         self.initUI()

    def initUI(self):
         self.btn=QPushButton("BTN")
        # 设置气泡提示信息
         self.setToolTip('This is a <b>QWidget</b> widget')
         QToolTip.setFont(QFont('OldEnglish', 10))

         self.setGeometry(200,200,200,200)#坐标，宽高
         self.setWindowTitle("显示图标的窗口")
         self.setWindowIcon(QIcon('cloud.ico'))#设置窗体图标

         # 布局
         layout = QHBoxLayout()
         layout.addWidget(self.btn)
         self.setLayout(layout)


if __name__=="__main__":
     app=QApplication(sys.argv)
     icon=IconClass()
     icon.show()
     sys.exit(app.exec_())