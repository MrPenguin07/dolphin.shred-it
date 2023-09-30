#!/usr/bin/env python3

import os
import subprocess
import sys
from pathlib import Path
from typing import List

from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import notify2

def shred_files(files: List[str], shred_iterations: int = 5):
    for file in files:
        subprocess.run(['shred', '-u', '-n', str(shred_iterations), file], check=True)

def shred_directory(directory: str, shred_iterations: int = 5):
    for root, dirs, files in reversed(list(os.walk(directory))):
        shred_files([os.path.join(root, file) for file in files], shred_iterations)
        for dir in dirs:
            os.rmdir(os.path.join(root, dir))
    os.rmdir(directory)

def shred_path(path: str, shred_iterations: int = 5):
    if os.path.isfile(path):
        dialog = QMessageBox()
        dialog.setIconPixmap(QIcon("/usr/share/kio/servicemenus/shredder.png").pixmap(64, 64))
        dialog.setWindowTitle("Question")
        dialog.setText("Are you sure you want to shred the file?")
        dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dialog.setDefaultButton(QMessageBox.Yes)
        response = dialog.exec_()
        if response == QMessageBox.Yes:
            shred_files([path], shred_iterations)
            notify2.Notification('Shred', f'Finished shredding {path}', 'dialog-information').show()
    elif os.path.isdir(path):
        dialog = QMessageBox()
        dialog.setIconPixmap(QIcon("/usr/share/kio/servicemenus/shredder.png").pixmap(64, 64))
        dialog.setWindowTitle("Question")
        dialog.setText("Are you sure you want to shred the directory and all its contents?")
        dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dialog.setDefaultButton(QMessageBox.Yes)
        response = dialog.exec_()
        if response == QMessageBox.Yes:
            shred_directory(path, shred_iterations)
            notify2.Notification('Shred', f'Finished shredding {path}', 'dialog-information').show()

if __name__ == '__main__':
    notify2.init('Shred')
    app = QApplication(sys.argv)

    for path in sys.argv[1:]:
        path = Path(path).resolve()
        shred_path(str(path))

    sys.exit(0)
