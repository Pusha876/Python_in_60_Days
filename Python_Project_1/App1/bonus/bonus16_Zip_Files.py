# This snippet is a simple GUI that allows the user to select files
# and a destination folder.

import FreeSimpleGUI as zf
from bonus17_zip_creator import make_archive

label1 = zf.Text("Select files to compress: ")
input1 = zf.Input()
choose_button1 = zf.FilesBrowse("Choose", key="files")

label2 = zf.Text("Select destination folder: ")
input2 = zf.Input()
choose_button2 = zf.FolderBrowse("Choose", key="folder")

compress_button = zf.Button("Compress")
output_label = zf.Text(key="output")

window = zf.Window("File Compressor", layout=[
    [label1, input1, choose_button1],
    [label2, input2, choose_button2],
    [compress_button, output_label]])

while True:
    event, values = window.read()
    if event == zf.WIN_CLOSED or event == "Exit":
        break
    if values:
        filepaths = values.get("files", "").split(";")
        folder = values.get("folder", "")
        if filepaths and folder:
            make_archive(filepaths, folder)
            window["output"].update(value="Files compressed successfully.")

window.read()
window.close()
