# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pansharpen_qgis.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys
sys.path.append("C:\\Users\\Avimar\\Desktop\\plugin_hernan\\repositorio\\qtplugin-pansharpen\\app\\scripts\\")
import gdalClass

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(433, 261)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 411, 241))
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setTitle("")
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.panImage = QgsFileWidget(self.groupBox)
        self.panImage.setGeometry(QtCore.QRect(210, 50, 171, 27))
        self.panImage.setAccessibleName("")
        self.panImage.setObjectName("panImage")
        self.multImage = QgsFileWidget(self.groupBox)
        self.multImage.setEnabled(True)
        self.multImage.setGeometry(QtCore.QRect(210, 100, 171, 27))
        self.multImage.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.multImage.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.multImage.setFileWidgetButtonVisible(True)
        self.multImage.setFullUrl(True)
        self.multImage.setFilter("")
        self.multImage.setDefaultRoot("")
        self.multImage.setObjectName("multImage")
        self.panImageLabel = QtWidgets.QLabel(self.groupBox)
        self.panImageLabel.setGeometry(QtCore.QRect(30, 50, 161, 20))
        self.panImageLabel.setObjectName("panImageLabel")
        self.multImageLabel = QtWidgets.QLabel(self.groupBox)
        self.multImageLabel.setEnabled(True)
        self.multImageLabel.setGeometry(QtCore.QRect(30, 100, 161, 20))
        self.multImageLabel.setAcceptDrops(False)
        self.multImageLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.multImageLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.multImageLabel.setLineWidth(1)
        self.multImageLabel.setWordWrap(False)
        self.multImageLabel.setObjectName("multImageLabel")
        self.btnPansharpen = QtWidgets.QPushButton(self.groupBox)
        self.btnPansharpen.setGeometry(QtCore.QRect(230, 160, 91, 31))
        self.btnPansharpen.setTabletTracking(False)
        self.btnPansharpen.setObjectName("btnPansharpen")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Qgis Pansharpen Plugin"))
        self.panImage.setDialogTitle(_translate("Dialog", "arquivo"))
        self.multImage.setDialogTitle(_translate("Dialog", "arquivo"))
        self.panImageLabel.setText(_translate("Dialog", "Panchromatic Image (.tiff)"))
        self.multImageLabel.setText(_translate("Dialog", "Multispectral Image (.tiff)"))
        self.btnPansharpen.setText(_translate("Dialog", "Pansharpen"))

    def panImageFile(self):
        return self.panImage.filePath()

    def multImageFile(self):
        return self.multImage.filePath()

    def GdalClass(self):
        return gdalClass.GdalClass()

    def onClick(self):
        print('botão funcionou')
        print(self.panImageFile())
        print(self.multImageFile())
        self.GdalClass().testando()
        nameOutput = os.path.basename(self.panImageFile()) + '-' + os.path.basename(self.multImageFile()) + '.tiff'
        output = os.path.join(os.path.dirname(self.panImageFile()),nameOutput)
        print(output)
        self.GdalClass().pansharpening(self.panImageFile(), self.multImageFile(), output)


from qgis.gui import QgsFileWidget

if __name__ == "__main__":
# if __name__ == "__console__":
#     print('Executed on console context.')
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    app.exec()
    ui.btnPansharpen.clicked.connect(ui.onClick)
    #sys.exit(app.exec_())

