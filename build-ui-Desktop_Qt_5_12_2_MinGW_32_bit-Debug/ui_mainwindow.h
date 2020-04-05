/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.12.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QLabel>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QProgressBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionSIMPLE_HAP_BATCH_EXPORTER;
    QWidget *centralwidget;
    QPushButton *exportbutton;
    QGroupBox *FileInputBox;
    QListWidget *filelist;
    QGroupBox *OptionsBox;
    QRadioButton *radioButton_Hap;
    QRadioButton *radioButton_HapQ;
    QRadioButton *radioButton_HapAlpha;
    QRadioButton *radioButton_Mjpeg;
    QGroupBox *RenamingBox;
    QTextEdit *removeInput;
    QLabel *label_3;
    QLabel *label_4;
    QLabel *label_5;
    QTextEdit *prefixInput;
    QGroupBox *OutputBox;
    QTextEdit *Output_dir_textEdit;
    QLabel *label_6;
    QComboBox *resolution_comboBox;
    QRadioButton *predefined_radioButton;
    QCheckBox *orig_resolution_checkBox;
    QLabel *label;
    QProgressBar *progressBar;
    QLabel *title_cheesy;
    QLabel *pixmap_label_7;
    QMenuBar *menubar;
    QMenu *menuAbout;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(1146, 586);
        QPalette palette;
        QBrush brush(QColor(255, 255, 255, 255));
        brush.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Active, QPalette::Light, brush);
        palette.setBrush(QPalette::Active, QPalette::Base, brush);
        QBrush brush1(QColor(255, 164, 68, 255));
        brush1.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Active, QPalette::Window, brush1);
        palette.setBrush(QPalette::Active, QPalette::NoRole, brush);
        palette.setBrush(QPalette::Inactive, QPalette::Light, brush);
        palette.setBrush(QPalette::Inactive, QPalette::Base, brush);
        palette.setBrush(QPalette::Inactive, QPalette::Window, brush1);
        palette.setBrush(QPalette::Inactive, QPalette::NoRole, brush);
        palette.setBrush(QPalette::Disabled, QPalette::Light, brush);
        palette.setBrush(QPalette::Disabled, QPalette::Base, brush1);
        palette.setBrush(QPalette::Disabled, QPalette::Window, brush1);
        palette.setBrush(QPalette::Disabled, QPalette::NoRole, brush);
        MainWindow->setPalette(palette);
        actionSIMPLE_HAP_BATCH_EXPORTER = new QAction(MainWindow);
        actionSIMPLE_HAP_BATCH_EXPORTER->setObjectName(QString::fromUtf8("actionSIMPLE_HAP_BATCH_EXPORTER"));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        exportbutton = new QPushButton(centralwidget);
        exportbutton->setObjectName(QString::fromUtf8("exportbutton"));
        exportbutton->setGeometry(QRect(920, 420, 181, 51));
        FileInputBox = new QGroupBox(centralwidget);
        FileInputBox->setObjectName(QString::fromUtf8("FileInputBox"));
        FileInputBox->setGeometry(QRect(10, 70, 261, 261));
        filelist = new QListWidget(FileInputBox);
        filelist->setObjectName(QString::fromUtf8("filelist"));
        filelist->setGeometry(QRect(5, 20, 251, 231));
        filelist->setInputMethodHints(Qt::ImhNone);
        OptionsBox = new QGroupBox(centralwidget);
        OptionsBox->setObjectName(QString::fromUtf8("OptionsBox"));
        OptionsBox->setGeometry(QRect(280, 70, 261, 261));
        radioButton_Hap = new QRadioButton(OptionsBox);
        radioButton_Hap->setObjectName(QString::fromUtf8("radioButton_Hap"));
        radioButton_Hap->setGeometry(QRect(20, 30, 51, 20));
        radioButton_HapQ = new QRadioButton(OptionsBox);
        radioButton_HapQ->setObjectName(QString::fromUtf8("radioButton_HapQ"));
        radioButton_HapQ->setGeometry(QRect(20, 140, 71, 20));
        radioButton_HapAlpha = new QRadioButton(OptionsBox);
        radioButton_HapAlpha->setObjectName(QString::fromUtf8("radioButton_HapAlpha"));
        radioButton_HapAlpha->setGeometry(QRect(20, 90, 101, 20));
        radioButton_Mjpeg = new QRadioButton(OptionsBox);
        radioButton_Mjpeg->setObjectName(QString::fromUtf8("radioButton_Mjpeg"));
        radioButton_Mjpeg->setGeometry(QRect(20, 190, 61, 20));
        RenamingBox = new QGroupBox(centralwidget);
        RenamingBox->setObjectName(QString::fromUtf8("RenamingBox"));
        RenamingBox->setGeometry(QRect(550, 70, 261, 261));
        removeInput = new QTextEdit(RenamingBox);
        removeInput->setObjectName(QString::fromUtf8("removeInput"));
        removeInput->setGeometry(QRect(10, 70, 231, 51));
        QFont font;
        font.setPointSize(12);
        removeInput->setFont(font);
        label_3 = new QLabel(RenamingBox);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setGeometry(QRect(10, 30, 171, 21));
        label_4 = new QLabel(RenamingBox);
        label_4->setObjectName(QString::fromUtf8("label_4"));
        label_4->setGeometry(QRect(10, 50, 221, 20));
        label_5 = new QLabel(RenamingBox);
        label_5->setObjectName(QString::fromUtf8("label_5"));
        label_5->setGeometry(QRect(10, 140, 221, 16));
        prefixInput = new QTextEdit(RenamingBox);
        prefixInput->setObjectName(QString::fromUtf8("prefixInput"));
        prefixInput->setGeometry(QRect(10, 170, 231, 51));
        OutputBox = new QGroupBox(centralwidget);
        OutputBox->setObjectName(QString::fromUtf8("OutputBox"));
        OutputBox->setGeometry(QRect(820, 70, 301, 261));
        Output_dir_textEdit = new QTextEdit(OutputBox);
        Output_dir_textEdit->setObjectName(QString::fromUtf8("Output_dir_textEdit"));
        Output_dir_textEdit->setGeometry(QRect(10, 40, 271, 23));
        label_6 = new QLabel(OutputBox);
        label_6->setObjectName(QString::fromUtf8("label_6"));
        label_6->setGeometry(QRect(10, 20, 171, 21));
        resolution_comboBox = new QComboBox(OutputBox);
        resolution_comboBox->addItem(QString());
        resolution_comboBox->setObjectName(QString::fromUtf8("resolution_comboBox"));
        resolution_comboBox->setGeometry(QRect(10, 180, 201, 22));
        predefined_radioButton = new QRadioButton(OutputBox);
        predefined_radioButton->setObjectName(QString::fromUtf8("predefined_radioButton"));
        predefined_radioButton->setGeometry(QRect(10, 150, 191, 20));
        orig_resolution_checkBox = new QCheckBox(OutputBox);
        orig_resolution_checkBox->setObjectName(QString::fromUtf8("orig_resolution_checkBox"));
        orig_resolution_checkBox->setGeometry(QRect(10, 130, 201, 20));
        label = new QLabel(centralwidget);
        label->setObjectName(QString::fromUtf8("label"));
        label->setGeometry(QRect(10, 520, 821, 16));
        progressBar = new QProgressBar(centralwidget);
        progressBar->setObjectName(QString::fromUtf8("progressBar"));
        progressBar->setGeometry(QRect(10, 490, 1131, 23));
        progressBar->setValue(0);
        title_cheesy = new QLabel(centralwidget);
        title_cheesy->setObjectName(QString::fromUtf8("title_cheesy"));
        title_cheesy->setGeometry(QRect(14, 15, 531, 41));
        title_cheesy->setFont(font);
        pixmap_label_7 = new QLabel(centralwidget);
        pixmap_label_7->setObjectName(QString::fromUtf8("pixmap_label_7"));
        pixmap_label_7->setGeometry(QRect(130, 10, 71, 61));
        pixmap_label_7->setAcceptDrops(true);
        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 1146, 21));
        menuAbout = new QMenu(menubar);
        menuAbout->setObjectName(QString::fromUtf8("menuAbout"));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        MainWindow->setStatusBar(statusbar);

        menubar->addAction(menuAbout->menuAction());

        retranslateUi(MainWindow);
        QObject::connect(orig_resolution_checkBox, SIGNAL(toggled(bool)), resolution_comboBox, SLOT(setDisabled(bool)));

        filelist->setCurrentRow(-1);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", nullptr));
        actionSIMPLE_HAP_BATCH_EXPORTER->setText(QApplication::translate("MainWindow", "SIMPLE HAP BATCH EXPORTER", nullptr));
        exportbutton->setText(QApplication::translate("MainWindow", "Export!", nullptr));
        FileInputBox->setTitle(QApplication::translate("MainWindow", "Files", nullptr));
        OptionsBox->setTitle(QApplication::translate("MainWindow", "Options", nullptr));
        radioButton_Hap->setText(QApplication::translate("MainWindow", "HAP ", nullptr));
        radioButton_HapQ->setText(QApplication::translate("MainWindow", "HAP  Q", nullptr));
        radioButton_HapAlpha->setText(QApplication::translate("MainWindow", "HAP + Alpha", nullptr));
        radioButton_Mjpeg->setText(QApplication::translate("MainWindow", "MJPEG", nullptr));
        RenamingBox->setTitle(QApplication::translate("MainWindow", "Renaming Options", nullptr));
        label_3->setText(QApplication::translate("MainWindow", "Remove Strings in Filenames", nullptr));
        label_4->setText(QApplication::translate("MainWindow", "seperate through \";\"", nullptr));
        label_5->setText(QApplication::translate("MainWindow", "add Prefix:", nullptr));
        OutputBox->setTitle(QApplication::translate("MainWindow", "Output", nullptr));
        Output_dir_textEdit->setHtml(QApplication::translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", nullptr));
        label_6->setText(QApplication::translate("MainWindow", "Output Directory: ", nullptr));
        resolution_comboBox->setItemText(0, QApplication::translate("MainWindow", "1920x1080", nullptr));

        predefined_radioButton->setText(QApplication::translate("MainWindow", "Use predefined resolution", nullptr));
        orig_resolution_checkBox->setText(QApplication::translate("MainWindow", "Use source original resolution", nullptr));
        label->setText(QApplication::translate("MainWindow", "CheesyHAP Batch Hap Converter/Exporter v 0.1 by Artur Kechter, based on ffmpeg", nullptr));
        title_cheesy->setText(QApplication::translate("MainWindow", "CheesyHAP", nullptr));
        pixmap_label_7->setText(QApplication::translate("MainWindow", "Cheese Place", nullptr));
        menuAbout->setTitle(QApplication::translate("MainWindow", "About", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
