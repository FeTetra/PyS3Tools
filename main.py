import sys

from PySide6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QToolBar, QStatusBar
)
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Test Window")

        label = QLabel("Test Label")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("Test ToolBar")
        self.addToolBar(toolbar)

        button_action = QAction(QIcon("./assets/images/test.png"), "Test Button", self)
        button_action.setStatusTip("This is a test button.")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        self.setStatusBar(QStatusBar(self))



    def onMyToolBarButtonClick(self, s):
        print("Test Click", s)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
