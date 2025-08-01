# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QPlainTextEdit,
    QProgressBar, QPushButton, QRadioButton, QSizePolicy,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.textInput = QPlainTextEdit(Widget)
        self.textInput.setObjectName(u"textInput")
        self.textInput.setGeometry(QRect(90, 280, 591, 221))
        self.submit = QPushButton(Widget)
        self.submit.setObjectName(u"submit")
        self.submit.setGeometry(QRect(570, 550, 111, 31))
        self.noteTakingGroupBox = QGroupBox(Widget)
        self.noteTakingGroupBox.setObjectName(u"noteTakingGroupBox")
        self.noteTakingGroupBox.setGeometry(QRect(90, 50, 151, 171))
        self.mappingMethodButton = QRadioButton(self.noteTakingGroupBox)
        self.mappingMethodButton.setObjectName(u"mappingMethodButton")
        self.mappingMethodButton.setGeometry(QRect(10, 140, 131, 21))
        self.chartingMethodButton = QRadioButton(self.noteTakingGroupBox)
        self.chartingMethodButton.setObjectName(u"chartingMethodButton")
        self.chartingMethodButton.setGeometry(QRect(10, 110, 121, 21))
        self.cornellMethodButton = QRadioButton(self.noteTakingGroupBox)
        self.cornellMethodButton.setObjectName(u"cornellMethodButton")
        self.cornellMethodButton.setGeometry(QRect(10, 50, 111, 21))
        self.boxingMethodButton = QRadioButton(self.noteTakingGroupBox)
        self.boxingMethodButton.setObjectName(u"boxingMethodButton")
        self.boxingMethodButton.setGeometry(QRect(10, 80, 121, 21))
        self.outlineMethodButton = QRadioButton(self.noteTakingGroupBox)
        self.outlineMethodButton.setObjectName(u"outlineMethodButton")
        self.outlineMethodButton.setGeometry(QRect(10, 20, 121, 21))
        self.reset = QPushButton(Widget)
        self.reset.setObjectName(u"reset")
        self.reset.setGeometry(QRect(440, 550, 111, 31))
        self.textarea = QLabel(Widget)
        self.textarea.setObjectName(u"textarea")
        self.textarea.setGeometry(QRect(90, 250, 49, 16))
        self.progressBar = QProgressBar(Widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(440, 510, 241, 23))
        self.progressBar.setValue(0)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.submit.setText(QCoreApplication.translate("Widget", u"Create Notes", None))
        self.noteTakingGroupBox.setTitle(QCoreApplication.translate("Widget", u"Note Taking Method", None))
        self.mappingMethodButton.setText(QCoreApplication.translate("Widget", u"Mapping Method", None))
        self.chartingMethodButton.setText(QCoreApplication.translate("Widget", u"Charting Method", None))
        self.cornellMethodButton.setText(QCoreApplication.translate("Widget", u"Cornell Method", None))
        self.boxingMethodButton.setText(QCoreApplication.translate("Widget", u"Boxing Method", None))
        self.outlineMethodButton.setText(QCoreApplication.translate("Widget", u"Outline Method", None))
        self.reset.setText(QCoreApplication.translate("Widget", u"Reset", None))
        self.textarea.setText(QCoreApplication.translate("Widget", u"Text", None))
    # retranslateUi

