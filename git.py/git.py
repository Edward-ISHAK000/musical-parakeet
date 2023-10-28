#создай приложение для запоминания информац
from PyQt5.QCore import Qt
from PyQt5.QWidgets import (QAppllcation,Qwidget,QBoxLayout,QGroupox,Qadlayout,QPushButton,Qlabel)
app= QApplication([])
window = QWidget()
window = setWindowTitle('Menu Card')
'''Интерфейс приложения memor card'''
btn_OK=QPusbutton('Ответить')
lb_Qestion = Qlabel('В каком году была основана Москва?')

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1=QRadioButton('1147')
rbtn_2=QRadioButton('1242')
rbtn_3=QRadioButton('1861')
rbtn_4=QRadioButton('1943')

Layout_ans1 = QHBoxLayout()
Layout_ans2 = QHBoxLayout()
Layout_ans3 = QHBoxLayout()
Layout_ans2 = QHBoxLayout(rbtn_1)
Layout_ans2 = QHBoxLayout(rbtn_2)
Layout_ans3 = QHBoxLayout(rbtn_3)
Layout_ans3 = QHBoxLayout(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.SetLayout(Layout_ans1)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

RadioGroupBox.setLayout(layout_ans1)

Layout_line1 = QHBoxLayout()
Layout_line2 = QHBoxLayout()
Layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Qestion,aligment=(Qt.alignHCenter / Qt.AlignvCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line3.addStretch(1)
layout.card.addlayout(layout_line3, stretch=1)
layout_card.SetSpacing(5)

window.setLayout(layout_card)
window.show()
app.exec()