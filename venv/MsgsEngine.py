from PyQt5.QtWidgets import QMessageBox
from GUI import Ui_Stasyan
class Messages(Ui_Stasyan):
    def small_Messages(self, TITLE, TEXT,  ICON):
        msg=QMessageBox()
        msg.setWindowTitle(TITLE)
        msg.setText(TEXT)
        if ICON=="Crit":
            msg.setIcon(QMessageBox.Critical)
        elif ICON=="Quest":
            msg.setIcon(QMessageBox.Question)
        elif ICON=="Inf":
            msg.setIcon(QMessageBox.Information)
        elif ICON=="Warn":
            msg.setIcon(QMessageBox.Warning)

        x=msg.exec_()