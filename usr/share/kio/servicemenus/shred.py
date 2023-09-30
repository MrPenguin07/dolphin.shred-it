#!/usr/bin/env python3

import os
import subprocess
import sys
import time
import tqdm
from pathlib import Path
from typing import List

import notify2
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def shred_files(files: List[str], shred_iterations: int = 5):
    for file in tqdm.tqdm(files, desc='Shredding files'):
        subprocess.run(['shred', '-u', '-n', str(shred_iterations), file], check=True)

def shred_directory(directory: str, shred_iterations: int = 5):
    for root, dirs, files in reversed(list(os.walk(directory))):
        shred_files([os.path.join(root, file) for file in files], shred_iterations)
        for dir in dirs:
            os.rmdir(os.path.join(root, dir))
    os.rmdir(directory)

def shred_path(path: str, shred_iterations: int = 5):
    if os.path.isfile(path):
        dialog = Gtk.MessageDialog(
            parent=None,
            flags=0,
            message_type=Gtk.MessageType.QUESTION,
            buttons=Gtk.ButtonsType.YES_NO,
            text="Are you sure you want to shred the file?"
        )
        response = dialog.run()
        if response == Gtk.ResponseType.YES:
            shred_files([path], shred_iterations)
        dialog.destroy()
    elif os.path.isdir(path):
        dialog = Gtk.MessageDialog(
            parent=None,
            flags=0,
            message_type=Gtk.MessageType.QUESTION,
            buttons=Gtk.ButtonsType.YES_NO,
            text="Are you sure you want to shred the directory and all its contents?"
        )
        response = dialog.run()
        if response == Gtk.ResponseType.YES:
            shred_directory(path, shred_iterations)
        dialog.destroy()

if __name__ == '__main__':
    notify2.init('Shred')
    for path in sys.argv[1:]:
        path = Path(path).resolve()
        shred_path(str(path))
        notify2.Notification('Shred', f'Finished shredding {path}', 'dialog-information').show()
