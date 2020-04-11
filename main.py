# USE pyuic5 to convert the mainwindow.ui to a mainwindow.py file:
#pyuic5 mainwindow.ui -o mainwindow.py

import sys, os

from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QTextEdit, QLabel
from PyQt5.QtCore import Qt, QRunnable, pyqtSlot, QThreadPool, pyqtSignal, QObject
from PyQt5.QtGui import QPixmap
from ui.mainwindow import Ui_MainWindow
import subprocess, os
import check




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


class modQTestEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setGeometry(10,40,271,31)



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
        self.ui.set_output_directory = modQTestEdit(self.ui.Output_dir_textEdit)
        self.ui.label_warning_big.hide()
        self.ui.label_warning_small.hide()
        self.ui.textEdit_custom_resolution_height.setDisabled(True)
        self.ui.textEdit_custom_resolution_width.setDisabled(True)
        if check.check.check_if_ffmpeg_is_installed() == False:
            self.ui.label_warning_big.show()
            self.ui.label_warning_small.show()





    def PopUp(self):
                self.lbl = QLabel("ffmpeg is missing on this machine.\nPlease Download here:\nwww.ffmpeg.org")
                self.close()
                self.lbl.show()

    def get_number_of_urls(self, urls):
        url_len = len(urls) # Renamed variable from 'kazoo' to a more meaningful name ;)
        print("total number of urls: " + str(url_len))
        return url_len

    def getSelectedItem(self):
        item = QListWidgetItem(self.listView.currentItem())
        return item.text()


    def get_output_directory(self):
        outputfilepath = self.ui.Output_dir_textEdit.toPlainText()
        print(outputfilepath)
        # if 'file:///' in outputfilepath:
        #     index_remove = outputfilepath.find('file:///')
        #     outputfilepath = [index_remove+len('file:///'):]
        outputfilepath = outputfilepath.replace('file:///', '')
        print(outputfilepath)

        if os.path.isdir(outputfilepath):
            return outputfilepath
        else:
            print("this box should contain only directories. This not a directory!")

        # Renamed this from 'set_ouputdir' to 'output_dir' since it doesn't change any variables.
    def output_dir(self):
        # Changed this to be OS and user independent :)
        # return os.path.join(os.path.expanduser("~/Desktop/"+str(self.get_output_directory())))
        return os.path.join(os.path.expanduser(str(self.get_output_directory()+"/")))

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
        # I would simplifed this to prevent accidental fall-though behavior with ifs.
        if self.ui.radioButton_Hap.isChecked():
            print("hap format selected")
            return "hap"
        if self.ui.radioButton_HapAlpha.isChecked():
            return "hap -format hap_alpha"
        if self.ui.radioButton_HapQ.isChecked():
            return "hap -format hap_q"
        if self.ui.radioButton_Mjpeg.isChecked():
            return "mjpeg -q:v 3"
        print("please specify format")

    def get_resolutions(self):
        # I don't think 'state' is used anywhere else, so it can be removed. :)
        # state = self.ui.orig_resolution_checkBox.isChecked()
        if self.ui.orig_resolution_checkBox.isChecked():
            resolution = ''
        if self.ui.custom_resolution_checkBox.isChecked():
            custom_resolution_width = self.ui.textEdit_custom_resolution_width.toPlainText()
            custom_resolution_height = self.ui.textEdit_custom_resolution_height.toPlainText()
            resolution = str(custom_resolution_width) + 'x' + str(custom_resolution_height)
        else:
            resolution = self.ui.resolution_comboBox.currentText()
        print("selected resoution: " + str(resolution))
        return str(resolution)

    def check_parameter(self):
        pass

    @property
    def strings_to_remove(self):
         toErase = self.ui.removeInput.toPlainText()
         eraselist = toErase.split(";")
         index = 0
         for element in eraselist:
             if ' ' in eraselist[index]:
                 eraselist[index] = element.replace(' ', '')
             index += 1
         print(eraselist)
         return eraselist

    def get_prefix(self):
        prefix = self.ui.prefixInput.toPlainText()
        if prefix == "":
            return None
        return self.ui.prefixInput.toPlainText() # Just shortened these lines, no else necessary since the 'if' returns before


    def set_statusbar(self, maxValue, index):
        self.ui.progressBar.setStyleSheet("QProgressBar::chunk { background-image: url(ressources/cardboard_texture.jpg); }")
        process_percentage_Value = 100 / maxValue * index
        self.ui.progressBar.setValue(process_percentage_Value)

    def run_export(self):
        # this method will contain tests in the future
        # this is a littlebit redundant.....
        paths = self.get_filepaths()
        outdir = self.output_dir()
        format = self.get_format_to_convert_to()
        to_erase = self.strings_to_remove
        resolution = self.get_resolutions()
        prefix = self.get_prefix()


        # Here we call the method
        self.run(paths, outdir, format, resolution, to_erase, prefix)

    def run(self, pathlist, outdirectory, format, resolution, eraselist, prefix):     
        # These variables need to be referenced across multiple file conversions, so I just store it on the 'Mainframe' object
        self.size = len(pathlist)
        self.outdirectory = outdirectory
        self.format = format
        self.resolution = resolution
        self.eraselist = eraselist
        self.prefix = prefix
        self.counter = 0
        
        # This constructs a pool of workers to help you easily multi-thread UIs
        self.threadpool = QThreadPool() 
        
        # Basic checks to make sure we have at-least 1 path available     
        self.path_list = pathlist
        if self.path_list:
            path = self.path_list.pop()
        if not path:
            return
            
        file = ffmpeg_converter(path, self.outdirectory, self.format, self.resolution, self.eraselist, self.prefix)
        worker = Worker(self.initialized_worker, file)
        worker.signals.finished.connect(self.inc_status_bar) # When the worker sends off a 'finished' signal, the we call the 'inc_status_bar' function
        self.threadpool.start(worker)
    
    # This function lets the main object update the status bar, then it starts the next worker (if one exists).
    def inc_status_bar(self):
        self.counter += 1
        self.set_statusbar(self.size, self.counter)
        if self.path_list:
            path = self.path_list.pop()
            file = ffmpeg_converter(path, self.outdirectory, self.format, self.resolution, self.eraselist, self.prefix)
            worker = Worker(self.initialized_worker, file) # we setup the worker to use 'initialzed_worker' as a callback function, we also supply a 'file' object to the worker
            worker.signals.finished.connect(self.inc_status_bar)
            self.threadpool.start(worker)
    
    def initialized_worker(self):
        print('initialized worker')            

class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        
        self.fn = fn
        self.file = args[0] # we pull out the file for later use
        self.args = args # Save any unnamed args (not used right now, but could hold additional information)
        self.kwargs = kwargs # Save any named args (not used right now, but could hold additional information)
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        cmd = self.file.command_concat()
        self.file.subprocess_run(cmd)
        
        # Example code to simulate tasks
        # import time
        # import random
        # sleep_time = random.randint(1,5)
        # time.sleep(sleep_time)
        # print("Thread complete")

        self.signals.finished.emit() # Send the signal that the worker has finished

class WorkerSignals(QObject):
    finished = pyqtSignal()

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


    def rename(self, eraselist, filename, prefix):
        if eraselist != []:
            for string in eraselist:
                if string in filename:
                    print("old filename: " + filename)
                    filename = filename.replace(string, '')
                    print("new filename: " + filename)
            print("removed: "+string)

            if prefix != '':
                filename = str(prefix)+filename
            return filename


    def command_concat(self):
        filename = os.path.basename(self.fileinputpath)
        new_filename = self.rename(self.toEraseList, filename, self.outprefix)
        br = ' '
        if self.outresolution == '':
            command = 'ffmpeg -i' + br + str(self.fileinputpath) + br + '-c:v' + br + str(self.fileformat) + br + str(self.fileoutputpath + new_filename)
        if self.outresolution != '':
            resolution = self.outresolution.split("x")
            print(resolution)
            scaling = '-vf scale=w='+ resolution[0] + ':' + 'h=' + resolution[1]
            command = 'ffmpeg -i' + br + str(self.fileinputpath) + br + '-c:v' + br + str(self.fileformat) + br + scaling + br + str(
                self.fileoutputpath + new_filename)
        print(command)
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


    #