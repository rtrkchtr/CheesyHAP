# USE pyuic5 to convert the mainwindow.ui to a mainwindow.py file:
#pyuic5 mainwindow.ui -o mainwindow.py

import sys, os

from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QPushButton, QLabel
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QPixmap
from ui.mainwindow import Ui_MainWindow
import subprocess, os


#-----Drag and Drop Files class -------
class ListBox(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(1000, 1000)
        self.setAcceptDrops(True)
        self.filepaths = []

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, e):
        if e.mimeData().hasUrls():
            e.setDropAction(Qt.CopyAction)
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()

            filepaths_local_variable = []

            for url in event.mimeData().urls():
                if url.isLocalFile():
                    filepaths_local_variable.append(str(url.toLocalFile()))

            self.addItems(filepaths_local_variable)
            self.filepaths = filepaths_local_variable

        else:
            event.ignore()

    def get_filepaths(self):
        return self.filepaths


# ----------------------- inherited modified Main Window Class -------------------------

class modifiedMainWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()

# ----------------------- MAIN CODE ------------------------------
class Mainframe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = modifiedMainWindow()
        self.ui.setupUi(self)
        self.ui.exportbutton.clicked.connect(self.run_export)
        self.ui.bx = ListBox(self.ui.filelist)
        pixmap = QPixmap('ressources/kaese2.png')
        self.ui.pixmap_label_7.setPixmap(pixmap)

    def get_number_of_urls(self, urls):
        kazoo = len(urls)
        print("total number of urls: " + str(kazoo))
        return kazoo

    def getSelectedItem(self):
        item = QListWidgetItem(self.listView.currentItem())
        return item.text()

    def set_outputdir(self):
        path = 'C:/Users/kecht/Desktop/output_test/'
        return path

    def get_output_directory(self):
        outputfilepath = self.ui.Output_dir_textEdit.toPlainText()
        if os.path.isdir(outputfilepath):
            return outputfilepath
            print(outputfilepath)
        else:
            print("this box should contain only directories. This not a directory!")

    def get_filepaths(self):
        files = self.ui.bx.get_filepaths()
        if files == []:
            print("feed me some files please! ")
        else:
            for file in self.checkPaths(files):
                print(file)
                return(self.checkPaths(files))

    # check if paths are files or directories:
    def checkPaths(self, filepaths):
        total_filepaths = []
        for file in filepaths:
            if os.path.isfile(file):
                total_filepaths.append(file)
            if os.path.isdir(file):
                print("dir: " + file)
                dir = os.listdir(file)
                for file in dir:
                    total_filepaths.append(file)
        self.get_number_of_urls(total_filepaths)
        return total_filepaths

    # This method takes the radiobutton input from the ui and returns Users input
    def get_format_to_convert_to(self):
        selection = None
        if self.ui.radioButton_Hap.isChecked():
            selection = "hap"
            print("hap format selected")
        if self.ui.radioButton_HapAlpha.isChecked():
            selection = "hap -format hap_alpha"
        if self.ui.radioButton_HapQ.isChecked():
            selection = "hap -format hap_q"
        if self.ui.radioButton_Mjpeg.isChecked():
            selection = "mjpeg -q:v 3"
        if selection == None:
            print("pleasy specify format")
        print(format)
        return selection

    def get_resolutions(self):
        state = self.ui.orig_resolution_checkBox.isChecked()
        if self.ui.orig_resolution_checkBox.isChecked():
            resolution = None
        else:
            resolution = self.ui.resolution_comboBox.currentText()
        print("selected resoution: " + str(resolution))
        return str(resolution)

    def check_parameter(self):
        pass

    def get_strings_to_remove(self):
        toErase = self.ui.removeInput.toPlainText()
        eraselist = toErase.split(";")
        print(eraselist)
        return eraselist

    def get_prefix(self):
        prefix = self.ui.prefixInput.toPlainText()
        if prefix == "":
            return None
        else:
            prefix = self.ui.prefixInput.toPlainText()
        return prefix


    def set_statusbar(self, maxValue, index):
        self.ui.progressBar.setStyleSheet("QProgressBar::chunk { background-image: url(ressources/cardboard_texture.jpg); }")
        process_percentage_Value = 100 / maxValue * index
        self.ui.progressBar.setValue(process_percentage_Value)

    def run_export(self):
        # this method will contain tests in the future
        # this is a littlebit redundant.....
        paths = self.get_filepaths()
        #outdir = self.get_output_directory()
        outdir = self.set_outputdir()
        format = self.get_format_to_convert_to()
        to_erase = self.get_strings_to_remove()
        resolution = self.get_resolutions()
        prefix = self.get_prefix()


        # Here we call the method
        self.run(paths, outdir, format, resolution, to_erase, prefix)

    def run(self, pathlist, outdirectory, format, resolution, eraselist, prefix):
        for path in pathlist:
            ffmpeg_object = ffmpeg_converter(path, outdirectory, format, resolution, eraselist, prefix) # creates a object
            cmd = ffmpeg_object.command_concat()
            ffmpeg_object.subprocess_run(cmd)        # Heres where the subprocess should start
            # self.set_statusbar(size, i)            # Will for the interactive UI
            continue

class ffmpeg_converter():
    def __init__(self, input, output, format, resolution, toErase, prefix):
        self.fileinputpath = input
        self.fileoutputpath = output
        self.outresolution = resolution
        self.fileformat = format
        self.outprefix = prefix
        self.toEraseList = toErase
        print("ffmpeg_object ínitialised. inputfile: " + str(self.fileinputpath))
        print("outputpath: "+ str(self.fileoutputpath))
        print("format: "+ str(self.fileformat))
        print("prefix: "+ str(self.outprefix))
        print("Eraselist: "+ str(self.toEraseList))

    def rename(self):
        if self.toEraseList != []:
            list_of_strings = self.toEraseList.split(";")
            filename = os.path.basename(self.inputpath)
            for string in list_of_strings:
                if string in filename:
                    del filename[string]
            print(filename)
            return filename

    def command_concat(self):
        filename = os.path.basename(self.fileinputpath)
        br = ' '
        command = 'ffmpeg -i' + br + str(self.fileinputpath) + br + '-c:v' + br + str(self.fileformat) + br + str(self.fileoutputpath + filename)
        return command

    def subprocess_run(self, cmd):
        subprocess.Popen(cmd).communicate()


    def get_inputfilepath(self):
        return self.fileinputpath

    def get_outputfilepath(self):
        return self.fileoutputpath

    def set_outputfilepath(self, outpath):
            self.fileoutputpathutput = outpath

    def get_prefix(self):
        return self.prefix

app = QApplication(sys.argv)
QtApp = Mainframe()
QtApp.show()
sys.exit(app.exec_())