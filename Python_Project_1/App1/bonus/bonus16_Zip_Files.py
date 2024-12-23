# This snippet is a simple GUI that allows the user to select files
# and a destination folder.

import FreeSimpleGUI as zf

label1 = zf.Text("Select files to compress: ")
input1 = zf.Input()
choose_button1 = zf.FileBrowse("Choose")

label2 = zf.Text("Select destination folder: ")
input2 = zf.Input()
choose_button2 = zf.FolderBrowse("Choose")

compress_button = zf.Button("Compress")

window = zf.Window("File Compressor", layout=[
    [label1, input1, choose_button1],
    [label2, input2, choose_button2],
    [compress_button]
])

window.read()
window.close()
