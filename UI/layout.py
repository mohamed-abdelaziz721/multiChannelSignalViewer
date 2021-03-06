# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI3.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from pyqtgraph import PlotWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import GraphicsLayoutWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1012, 849)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\Images/MainIcon.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.showChannels = QtWidgets.QHBoxLayout()
        self.showChannels.setObjectName("showChannels")
        self.showChannel1 = QtWidgets.QCheckBox(self.centralwidget)
        self.showChannel1.setMinimumSize(QtCore.QSize(327, 20))
        self.showChannel1.setObjectName("showChannel1")
        self.showChannels.addWidget(self.showChannel1)
        self.showChannel2 = QtWidgets.QCheckBox(self.centralwidget)
        self.showChannel2.setMinimumSize(QtCore.QSize(326, 20))
        self.showChannel2.setObjectName("showChannel2")
        self.showChannels.addWidget(self.showChannel2)
        self.showChannel3 = QtWidgets.QCheckBox(self.centralwidget)
        self.showChannel3.setMinimumSize(QtCore.QSize(327, 20))
        self.showChannel3.setObjectName("showChannel3")
        self.showChannels.addWidget(self.showChannel3)
        self.verticalLayout.addLayout(self.showChannels)
        self.channel1 = QtWidgets.QFrame()
        self.Channel1Components = QtWidgets.QHBoxLayout()
        self.channel1.setLayout(self.Channel1Components)
        self.verticalLayout.addWidget(self.channel1)
        self.Channel1Components.setObjectName("Channel1Components")
        self.signal1Graph = PlotWidget(self.centralwidget)
        # self.signal1Graph.setBackground('w')
        self.signal1Graph.plotItem.showGrid(True, True)
        self.signal1Graph.setMinimumSize(QtCore.QSize(470, 227))
        self.signal1Graph.setObjectName("signal1Graph")
        self.Channel1Components.addWidget(self.signal1Graph)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.Channel1Components.addWidget(self.line_4)
        self.spectrogram1Graph = GraphicsLayoutWidget(self.centralwidget)
        # self.spectrogram1Graph.setBackground('w')
        self.spectrogram1Graph.setMinimumSize(QtCore.QSize(470, 227))
        self.spectrogram1Graph.setObjectName("spectrogram1Graph")
        self.Channel1Components.addWidget(self.spectrogram1Graph)
        self.controls1 = QtWidgets.QVBoxLayout()
        self.controls1.setObjectName("controls1")
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.controls1.addItem(spacerItem)
        self.playBtn1 = QtWidgets.QPushButton(self.centralwidget)
        self.playBtn1.setEnabled(True)
        self.playBtn1.setMinimumSize(QtCore.QSize(29, 28))
        self.playBtn1.setMaximumSize(QtCore.QSize(50, 16777215))
        self.playBtn1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\Images/play.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playBtn1.setIcon(icon1)
        self.playBtn1.setObjectName("playBtn1")
        self.controls1.addWidget(self.playBtn1)
        self.pauseBtn1 = QtWidgets.QPushButton(self.centralwidget)
        self.pauseBtn1.setMinimumSize(QtCore.QSize(29, 28))
        self.pauseBtn1.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pauseBtn1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\Images/pause.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pauseBtn1.setIcon(icon2)
        self.pauseBtn1.setObjectName("pauseBtn1")
        self.controls1.addWidget(self.pauseBtn1)
        self.focusBtn1 = QtWidgets.QPushButton(self.centralwidget)
        self.focusBtn1.setMinimumSize(QtCore.QSize(29, 28))
        self.focusBtn1.setMaximumSize(QtCore.QSize(50, 16777215))
        self.focusBtn1.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\Images/focus.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.focusBtn1.setIcon(icon3)
        self.focusBtn1.setObjectName("focusBtn1")
        self.controls1.addWidget(self.focusBtn1)
        self.zoomInBtn1 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomInBtn1.setMinimumSize(QtCore.QSize(29, 28))
        self.zoomInBtn1.setMaximumSize(QtCore.QSize(50, 16777215))
        self.zoomInBtn1.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(".\\Images/zoom-in.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoomInBtn1.setIcon(icon4)
        self.zoomInBtn1.setObjectName("zoomInBtn1")
        self.controls1.addWidget(self.zoomInBtn1)
        self.zoomOutBtn1 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomOutBtn1.setMinimumSize(QtCore.QSize(29, 28))
        self.zoomOutBtn1.setMaximumSize(QtCore.QSize(50, 16777215))
        self.zoomOutBtn1.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(".\\Images/zoom-out.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoomOutBtn1.setIcon(icon5)
        self.zoomOutBtn1.setObjectName("zoomOutBtn1")
        self.controls1.addWidget(self.zoomOutBtn1)
        self.clearBtn1 = QtWidgets.QPushButton(self.centralwidget)
        self.clearBtn1.setMinimumSize(QtCore.QSize(29, 28))
        self.clearBtn1.setMaximumSize(QtCore.QSize(50, 16777215))
        self.clearBtn1.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(".\\Images/delete.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clearBtn1.setIcon(icon6)
        self.clearBtn1.setObjectName("clearBtn1")
        self.controls1.addWidget(self.clearBtn1)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.controls1.addItem(spacerItem1)
        self.Channel1Components.addLayout(self.controls1)
        self.verticalLayout.addLayout(self.Channel1Components)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.channel2 = QtWidgets.QFrame()
        self.Channel2Components = QtWidgets.QHBoxLayout()
        self.channel2.setLayout(self.Channel2Components)
        self.verticalLayout.addWidget(self.channel2)
        self.Channel2Components.setObjectName("Channel2Components")
        self.signal2Graph = PlotWidget(self.centralwidget)
        self.signal2Graph.plotItem.showGrid(True, True)
        # self.signal2Graph.setBackground('w')
        self.signal2Graph.setMinimumSize(QtCore.QSize(470, 226))
        self.signal2Graph.setObjectName("signal2Graph")
        self.Channel2Components.addWidget(self.signal2Graph)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.Channel2Components.addWidget(self.line_3)
        self.spectrogram2Graph = GraphicsLayoutWidget(self.centralwidget)
        # self.spectrogram2Graph.setBackground('w')
        self.spectrogram2Graph.setMinimumSize(QtCore.QSize(470, 226))
        self.spectrogram2Graph.setObjectName("spectrogram2Graph")
        self.Channel2Components.addWidget(self.spectrogram2Graph)
        self.controls2 = QtWidgets.QVBoxLayout()
        self.controls2.setObjectName("controls2")
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.controls2.addItem(spacerItem2)
        self.playBtn2 = QtWidgets.QPushButton(self.centralwidget)
        self.playBtn2.setEnabled(True)
        self.playBtn2.setMinimumSize(QtCore.QSize(29, 28))
        self.playBtn2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.playBtn2.setText("")
        self.playBtn2.setIcon(icon1)
        self.playBtn2.setObjectName("playBtn2")
        self.controls2.addWidget(self.playBtn2)
        self.pauseBtn2 = QtWidgets.QPushButton(self.centralwidget)
        self.pauseBtn2.setMinimumSize(QtCore.QSize(29, 28))
        self.pauseBtn2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pauseBtn2.setText("")
        self.pauseBtn2.setIcon(icon2)
        self.pauseBtn2.setObjectName("pauseBtn2")
        self.controls2.addWidget(self.pauseBtn2)
        self.focusBtn2 = QtWidgets.QPushButton(self.centralwidget)
        self.focusBtn2.setMinimumSize(QtCore.QSize(29, 28))
        self.focusBtn2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.focusBtn2.setText("")
        self.focusBtn2.setIcon(icon3)
        self.focusBtn2.setObjectName("focusBtn2")
        self.controls2.addWidget(self.focusBtn2)
        self.zoomInBtn2 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomInBtn2.setMinimumSize(QtCore.QSize(29, 28))
        self.zoomInBtn2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.zoomInBtn2.setText("")
        self.zoomInBtn2.setIcon(icon4)
        self.zoomInBtn2.setObjectName("zoomInBtn2")
        self.controls2.addWidget(self.zoomInBtn2)
        self.zoomOutBtn2 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomOutBtn2.setMinimumSize(QtCore.QSize(29, 28))
        self.zoomOutBtn2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.zoomOutBtn2.setText("")
        self.zoomOutBtn2.setIcon(icon5)
        self.zoomOutBtn2.setObjectName("zoomOutBtn2")
        self.controls2.addWidget(self.zoomOutBtn2)
        self.clearBtn2 = QtWidgets.QPushButton(self.centralwidget)
        self.clearBtn2.setMinimumSize(QtCore.QSize(29, 28))
        self.clearBtn2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.clearBtn2.setText("")
        self.clearBtn2.setIcon(icon6)
        self.clearBtn2.setObjectName("clearBtn2")
        self.controls2.addWidget(self.clearBtn2)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.controls2.addItem(spacerItem3)
        self.Channel2Components.addLayout(self.controls2)
        self.verticalLayout.addLayout(self.Channel2Components)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.channel3 = QtWidgets.QFrame()
        self.Channel3Components = QtWidgets.QHBoxLayout()
        self.channel3.setLayout(self.Channel3Components)
        self.verticalLayout.addWidget(self.channel3)
        self.Channel3Components.setObjectName("Channel3Components")
        self.signal3Graph = PlotWidget(self.centralwidget)
        self.signal3Graph.plotItem.showGrid(True, True)
        # self.signal3Graph.setBackground('w')
        self.signal3Graph.setMinimumSize(QtCore.QSize(470, 227))
        self.signal3Graph.setObjectName("signal3Graph")
        self.Channel3Components.addWidget(self.signal3Graph)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.Channel3Components.addWidget(self.line_5)
        self.spectrogram3Graph = GraphicsLayoutWidget(self.centralwidget)
        # self.spectrogram3Graph.setBackground('w')
        self.spectrogram3Graph.setMinimumSize(QtCore.QSize(470, 227))
        self.spectrogram3Graph.setObjectName("spectrogram3Graph")
        self.Channel3Components.addWidget(self.spectrogram3Graph)
        self.controls3 = QtWidgets.QVBoxLayout()
        self.controls3.setObjectName("controls3")
        spacerItem4 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.controls3.addItem(spacerItem4)
        self.playBtn3 = QtWidgets.QPushButton(self.centralwidget)
        self.playBtn3.setEnabled(True)
        self.playBtn3.setMinimumSize(QtCore.QSize(29, 28))
        self.playBtn3.setMaximumSize(QtCore.QSize(50, 16777215))
        self.playBtn3.setText("")
        self.playBtn3.setIcon(icon1)
        self.playBtn3.setObjectName("playBtn3")
        self.controls3.addWidget(self.playBtn3)
        self.pauseBtn3 = QtWidgets.QPushButton(self.centralwidget)
        self.pauseBtn3.setMinimumSize(QtCore.QSize(29, 28))
        self.pauseBtn3.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pauseBtn3.setText("")
        self.pauseBtn3.setIcon(icon2)
        self.pauseBtn3.setObjectName("pauseBtn3")
        self.controls3.addWidget(self.pauseBtn3)
        self.focusBtn3 = QtWidgets.QPushButton(self.centralwidget)
        self.focusBtn3.setMinimumSize(QtCore.QSize(29, 28))
        self.focusBtn3.setMaximumSize(QtCore.QSize(50, 16777215))
        self.focusBtn3.setText("")
        self.focusBtn3.setIcon(icon3)
        self.focusBtn3.setObjectName("focusBtn3")
        self.controls3.addWidget(self.focusBtn3)
        self.zoomInBtn3 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomInBtn3.setMinimumSize(QtCore.QSize(29, 28))
        self.zoomInBtn3.setMaximumSize(QtCore.QSize(50, 16777215))
        self.zoomInBtn3.setText("")
        self.zoomInBtn3.setIcon(icon4)
        self.zoomInBtn3.setObjectName("zoomInBtn3")
        self.controls3.addWidget(self.zoomInBtn3)
        self.zoomOutBtn3 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomOutBtn3.setMinimumSize(QtCore.QSize(29, 28))
        self.zoomOutBtn3.setMaximumSize(QtCore.QSize(50, 16777215))
        self.zoomOutBtn3.setText("")
        self.zoomOutBtn3.setIcon(icon5)
        self.zoomOutBtn3.setObjectName("zoomOutBtn3")
        self.controls3.addWidget(self.zoomOutBtn3)
        self.clearBtn3 = QtWidgets.QPushButton(self.centralwidget)
        self.clearBtn3.setMinimumSize(QtCore.QSize(29, 28))
        self.clearBtn3.setMaximumSize(QtCore.QSize(50, 16777215))
        self.clearBtn3.setText("")
        self.clearBtn3.setIcon(icon6)
        self.clearBtn3.setObjectName("clearBtn3")
        self.controls3.addWidget(self.clearBtn3)
        spacerItem5 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.controls3.addItem(spacerItem5)
        self.Channel3Components.addLayout(self.controls3)
        self.verticalLayout.addLayout(self.Channel3Components)
        self.generatePDFComponent = QtWidgets.QHBoxLayout()
        self.generatePDFComponent.setObjectName("generatePDFComponent")
        spacerItem6 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.generatePDFComponent.addItem(spacerItem6)
        self.generatePDF = QtWidgets.QPushButton(self.centralwidget)
        self.generatePDF.setMinimumSize(QtCore.QSize(93, 28))
        self.generatePDF.setObjectName("generatePDF")
        self.generatePDFComponent.addWidget(self.generatePDF)
        spacerItem7 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.generatePDFComponent.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.generatePDFComponent)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1012, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOpen = QtWidgets.QMenu(self.menuFile)
        self.menuOpen.setObjectName("menuOpen")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionGenerate_PDF = QtWidgets.QAction(MainWindow)
        self.actionGenerate_PDF.setObjectName("actionGenerate_PDF")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionOpenChannel1 = QtWidgets.QAction(MainWindow)
        self.actionOpenChannel1.setObjectName("actionOpenChannel1")
        self.actionOpenChannel2 = QtWidgets.QAction(MainWindow)
        self.actionOpenChannel2.setObjectName("actionOpenChannel2")
        self.actionOpenChannel3 = QtWidgets.QAction(MainWindow)
        self.actionOpenChannel3.setObjectName("actionOpenChannel3")
        self.menuOpen.addAction(self.actionOpenChannel1)
        self.menuOpen.addAction(self.actionOpenChannel2)
        self.menuOpen.addAction(self.actionOpenChannel3)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.menuOpen.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.timer1 = QtCore.QTimer()
        self.timer2 = QtCore.QTimer()
        self.timer3 = QtCore.QTimer()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "SBME - Signal Viewer"))
        self.showChannel1.setText(_translate("MainWindow", "CH1"))
        self.showChannel1.setShortcut(_translate("MainWindow", "Alt+1"))
        self.showChannel2.setText(_translate("MainWindow", "CH2"))
        self.showChannel2.setShortcut(_translate("MainWindow", "Alt+2"))
        self.showChannel3.setText(_translate("MainWindow", "CH3"))
        self.showChannel3.setShortcut(_translate("MainWindow", "Alt+3"))
        self.playBtn1.setShortcut(_translate("MainWindow", "Ctrl+P, Ctrl+1"))
        self.generatePDF.setText(_translate("MainWindow", "Generate PDF"))
        self.generatePDF.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOpen.setTitle(_translate("MainWindow", "Open"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionGenerate_PDF.setText(
            _translate("MainWindow", "Generate PDF"))
        self.actionGenerate_PDF.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionAbout.setShortcut(_translate("MainWindow", "F1"))
        self.actionOpenChannel1.setText(_translate("MainWindow", "Channel 1"))
        self.actionOpenChannel1.setShortcut(_translate("MainWindow", "Ctrl+1"))
        self.actionOpenChannel2.setText(_translate("MainWindow", "Channel 2"))
        self.actionOpenChannel2.setShortcut(_translate("MainWindow", "Ctrl+2"))
        self.actionOpenChannel3.setText(_translate("MainWindow", "Channel 3"))
        self.actionOpenChannel3.setShortcut(_translate("MainWindow", "Ctrl+3"))
