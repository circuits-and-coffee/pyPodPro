# File: main.py

from models.main_window import MainWindow
import sys
from PySide6 import QtWidgets, QtUiTools
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt, QFile, QIODevice
from PySide6.QtWidgets import QApplication, QListView, QLabel, QMainWindow, QWidget, QVBoxLayout, QAbstractItemView, QStackedWidget
from PySide6.QtGui import QStandardItemModel, QStandardItem
from pathlib import Path

# # You need one (and only one) QApplication instance per application.
# # Pass in sys.argv to allow command line arguments for your app.
# # If you know you won't use command line arguments QApplication([]) works too.
# app = QApplication(sys.argv)

# Helper function, returns element (could be widget, mainwindow, etc.) loaded from .ui file




#########################################################
# Main function
#########################################################

    
def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())



# This will eventually show the appropriate page in the stack
# Not sure how to do that yet
def show_local_music():
    print("Show Local Music")


def show_online_music():
    print("Show Online Music")
    
def show_photos():
    print("Show Photos")
    
def show_videos():
    print("Show Videos")
    
def show_settings():
    print("Show Settings")



def quit_app():
    QApplication.quit()







if __name__ == "__main__":
    main()