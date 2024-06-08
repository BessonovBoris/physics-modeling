import sys, os
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog
import platform
import locale, ctypes
from glob import glob

results = glob(os.getcwd() + "/**/", recursive=True)
for result in results:
    if result[-2] != "_":
        sys.path.insert(1, result)

import source.interference_main_window as main_window

app = QApplication(sys.argv)
window_Interference = QMainWindow()
dialog = QDialog()

systeme_exploitation = platform.system()
if systeme_exploitation == 'Windows':
    langwin = ctypes.windll.kernel32
    langue_sys = locale.windows_locale[langwin.GetUserDefaultUILanguage()]
elif systeme_exploitation == 'Darwin' or 'Linux':
    langue_sys = locale.getdefaultlocale()[0]
langue_sys = langue_sys[0:2]
translator = QtCore.QTranslator()
directory = "locales"
if langue_sys == "fr":
    langue = "fr_CA"
else:
    langue = "en_CA"
translator.load(langue, directory)
app.installTranslator(translator)

ui_Interference = main_window.Ui_MainWindow()

ui_Interference.setupUi(window_Interference, dialog, None)

window_Interference.show()
sys.exit(app.exec())
