import pyttsx3, sys, datetime
from PyQt5.QtCore import pyqtRemoveInputHook
from PyQt5.QtWidgets import QListWidgetItem, QFileDialog
from PyQt5 import  QtWidgets
from GUI import Ui_Stasyan
from gtts import gTTS
from tqdm import tqdm
from  time import  sleep
from MsgsEngine import  Messages
MSG=Messages()

#Default settings
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', 'ru')

#выводит все голоса
def ShowVoices():
    global  engine
    global  voices
    for voice in voices:
        text=str(voice.name)
        QListWidgetItem(text, ui.listWidget)

#устанавливает голос
def SetVoice(item):
    global  engine
    global  voices
    for voice in voices:
        if voice.name==item.text():
            engine.setProperty('voice', voice.id)
            MSG.small_Messages("Голос установлен!", "Установлен голос "+voice.name, "Inf")

def SetText():
    dialog = QFileDialog()
    dialog.setFileMode(QFileDialog.ExistingFile)
    filePath=dialog.getOpenFileName()
    filePath=filePath[0]
    file=open(filePath, 'r', encoding='utf-8')
    text=file.read()
    ui.textEdit.setText(text)


#читает текст
def ListenText():
    global  engine
    global  voices
    text=ui.textEdit.toPlainText()
    if text!='':
        engine.say(text)
        engine.runAndWait()
    else:
        MSG.small_Messages("Зочем?", "Нету текста, что ты слушать собрался?", "Warn")

# сохраняет
def Save():
    global  engine
    global  voices
    text = ui.textEdit.toPlainText()
    if text != '':
        today = datetime.datetime.today()
        name = 'Writed Voice  '+today.strftime("%Y-%m-%d-%H.%M.%S") + '.mp3'
        engine.save_to_file(text, 'Saves\\'+name, 'ru')
        engine.runAndWait()
        MSG.small_Messages("Уррррра!", "Файл сохранен в директории с программой в папке 'Saves' под именем '"+name+"'", "Inf")
    else:
        MSG.small_Messages("Зочем?", "Нету текста, что ты слушать собрался?", "Warn")

pyqtRemoveInputHook()
app = QtWidgets.QApplication(sys.argv)
Stasyan = QtWidgets.QMainWindow()
ui = Ui_Stasyan()
ui.setupUi(Stasyan)
Stasyan.show()

ShowVoices()
ui.listWidget.itemClicked.connect(SetVoice)
ui.ListenBtt.clicked.connect(ListenText)
ui.SaveBtt.clicked.connect(Save)
ui.GetTextBtt.clicked.connect(SetText)

sys.exit(app.exec_())