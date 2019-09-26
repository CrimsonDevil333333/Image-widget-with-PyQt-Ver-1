import os, random
from PyQt5 import QtCore, QtGui, QtWidgets
from Image_Directory import *
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(404, 298)
        Form.setFocusPolicy(QtCore.Qt.ClickFocus)
        Form.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        Form.setWindowOpacity(1.0)
        Form.setAutoFillBackground(True)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-6, -1, 411, 301))
        self.label.setFrameShape(QtWidgets.QFrame.Panel)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("GUI/ad.jpg"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.next = QtWidgets.QPushButton(Form)
        self.next.setGeometry(QtCore.QRect(340, 270, 71, 31))
        self.next.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.next.setShortcut("")
        self.next.setObjectName("next")
        self.back = QtWidgets.QPushButton(Form)
        self.back.setGeometry(QtCore.QRect(0, 270, 71, 31))
        self.back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back.setAutoFillBackground(False)
        self.back.setShortcut("")
        self.back.setObjectName("back")

        self.next.clicked.connect(self.next_pn)
        self.back.clicked.connect(self.prev_pn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Anime Widget"))
        self.next.setText(_translate("Form", "Next"))
        self.back.setText(_translate("Form", "Back"))

    def next_pn(self):
        self.label.setPixmap(QtGui.QPixmap(random_images_for_widget()))
    def prev_pn(self):
        self.label.setPixmap(QtGui.QPixmap(random_images_for_widget()))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
