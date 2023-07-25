# Form implementation generated from reading ui file 'stat418.ui'
#
# Created by: PyQt6 UI code generator 6.4.2

import string
from PySide6 import QtCore, QtWidgets, QtGui, QtCore
from PyQt6.QtCore import *
from suggestion import Suggestion
from pandas import *
import traceback, sys


class WorkerSignals(QObject):
 
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)


class Worker(QRunnable):

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()


    @pyqtSlot()
    def run(self):
        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done




class Ui_SpellCheck(object):

    
    def setupUi(self, SpellCheck):
        f = read_csv("Words_frequencies.csv", dtype=str)
        f2 = read_csv("Bigram_frequencies.csv", dtype=str)
        self.mydictionary = f.set_index('word').to_dict()['count']
        self.words_list = f['word'].tolist()
        self.frequencies = f['count'].tolist()
        self.bigram_dict = dict(zip(zip(f2['first'], f2['second']), f2['count'].astype(float)))
        self.realCursorPosition = 0
        errors = open("spelling_error_rates.txt", "r")
        error_lines = errors.readlines()
        self.createMatrices(error_lines)
        self.grayTextFlag = False
        self.underlineFlag = False
        self.cursorFlag = False
        self.previousTextBox = ""
        SpellCheck.setObjectName("SpellCheck")
        SpellCheck.resize(900, 520)
        SpellCheck.setMinimumSize(QtCore.QSize(950, 520))
        self.centralwidget = QtWidgets.QWidget(parent=SpellCheck)
        self.centralwidget.setMinimumSize(QtCore.QSize(950, 520))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(19, 24, 887, 465))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textEdit = QtWidgets.QTextEdit(parent=self.verticalLayoutWidget)
        self.textEdit.setMaximumSize(QtCore.QSize(519, 53))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.textChanged.connect(self.textEntered)
        self.textEdit.cursorPositionChanged.connect(self.cursorPos)
        self.verticalLayout_3.addWidget(self.textEdit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_3.addItem(spacerItem)
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        #self.verticalLayout_3.addWidget(self.buttonPrint)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_3.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_3.addItem(spacerItem2)
        #=self.horizontalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        
        #self.label_3 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        #self.label_3.setObjectName("label_3")
        self.question = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.question.setObjectName("question1")
        self.question.setText("?")
        self.question.setStyleSheet("border: 1px; border-radius: 3px; background-color: rgb(190, 190, 190)" )
        self.question.setGeometry(250,140,20,20)
        self.bigramToggle = QtWidgets.QCheckBox("Bigram Probabilities")
        self.bigramToggle.clicked.connect(self.setCurrentWord)
        self.verticalLayout_3.addWidget(self.bigramToggle)
        self.bigramToggle.setChecked(True)
        self.realToggle = QtWidgets.QCheckBox("Real-word Errors")
        self.realToggle.clicked.connect(self.setCurrentWord)
        self.verticalLayout_3.addWidget(self.realToggle)
        self.realToggle.setChecked(True)
        #self.verticalLayout_3.addWidget(self.horizontalLayout)
        
        self.tableWidget = QtWidgets.QTableWidget(parent=self.verticalLayoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(8)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        self.verticalLayout_3.addWidget(self.tableWidget)
        SpellCheck.setCentralWidget(self.centralwidget)

        self.retranslateUi(SpellCheck)
        QtCore.QMetaObject.connectSlotsByName(SpellCheck)
        self.grayTextFlag = True
        self.tableWidget.setFocus()

        self.threadpool = QThreadPool() 

        
    def retranslateUi(self, SpellCheck):
        _translate = QtCore.QCoreApplication.translate
        SpellCheck.setWindowTitle(_translate("SpellCheck", "SpellCheck"))
        self.textEdit.setHtml(_translate("SpellCheck", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; color:gray; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enter a sentence here</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("SpellCheck", "Current Word: here"))
        self.label_2.setText(_translate("SpellCheck", "Dictionary match"))
        #self.label_3.setText(_translate("SpellCheck", "Use Bigram Probabilities"))
        #self.buttonPrint.setText("Print")
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("SpellCheck", "Suggestion 1"))
        item.setSelected(True)
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("SpellCheck", "Suggestion 2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("SpellCheck", "Suggestion 3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("SpellCheck", "Suggestion 4 "))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("SpellCheck", "Suggestion 5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("SpellCheck", "Suggestion 6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("SpellCheck", "Suggestion 7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("SpellCheck", "Suggestion 8"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("SpellCheck", "Error Type"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("SpellCheck", "Correct Letter"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("SpellCheck", "Error Letter"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("SpellCheck", "Position"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("SpellCheck", "n * P(X|W)"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("SpellCheck", "n * P(W)"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("SpellCheck", "Bigram"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("SpellCheck", "n * P(W|X)"))

        
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

    

    def textEntered(self):
        #about all words
        
        newestCharPos = self.textEdit.textCursor().position()-1
        newestCharPos = 0 if newestCharPos < 0 else newestCharPos
        newestChar = ""
        if self.textEdit.toPlainText() != None and len(self.textEdit.toPlainText()) > newestCharPos:
            newestChar = self.textEdit.toPlainText()[newestCharPos] 

        if(newestChar in string.punctuation or newestChar in string.whitespace or (not self.textEdit.textCursor().atEnd())):

            if(self.underlineFlag):
        
                
                inputWords = self.textEdit.toPlainText().translate(str.maketrans('','',string.punctuation)).split()
                newString = self.textEdit.toPlainText()

                startPos = 0
                for i in inputWords:
                    inDictionary =  i in self.words_list
                    if(not inDictionary):
                        pos = newString.find(i, startPos)
                        #newString = newString[0:pos] + "<u style='color:red;'>" + str(i) + "</u>" + newString[pos+len(i):len(newString)]
                        newString = newString[0:pos] + "<u style='text-decoration: underline;text-decoration-color: blue;'>" + str(i) + "</u>" + newString[pos+len(i):len(newString)]
                        startPos = pos+len(i)

                self.underlineFlag = False
                self.cursorFlag = True
                self.realCursorPosition = self.textEdit.textCursor().position()
                self.textEdit.setText(newString)          
                #self.textEdit.setFontPointSize(8)
                
            
                #about the current word 
                if self.textEdit.textCursor().atEnd():
                    self.setCurrentWord()

        self.underlineFlag = True


    def printbutton(self):
        print(self.textEdit.toHtml())
       # print(self.textEdit.toPlainText().translate(str.maketrans('','',string.punctuation)))
        
    def setCurrentWord(self):
        _translate = QtCore.QCoreApplication.translate
        if self.bigramToggle.isChecked():
            self.realToggle.setEnabled(True)
        else:
            self.realToggle.setEnabled(False)
    
        endOfWord = self.textEdit.toPlainText().find(" ", self.textEdit.textCursor().position())
        myString = self.textEdit.toPlainText()[0:endOfWord]
        noPunctuation = myString.strip().translate(str.maketrans('','',string.punctuation))

        currentWord = noPunctuation.rpartition(" ")[2]
        previousWord = noPunctuation.rpartition(" ")[0].rpartition(" ")[2]
        nextWord = ""
        endOfNext = self.textEdit.toPlainText().find(" ", endOfWord+1)
        if endOfNext != -1:
            nextWord = self.textEdit.toPlainText()[endOfWord:endOfNext].strip()
        
        inDictionary = currentWord in self.words_list
        self.label.setText(_translate("SpellCheck", "Current word: " + currentWord))
        self.label_2.setText(_translate("SpellCheck", "Dictionary Match" if inDictionary else "No Dictionary Match"))

        if(not inDictionary) or self.realToggle.isChecked():
            self.suggestions = []

            worker = Worker(self.findCorrections, currentWord, previousWord, nextWord)
            self.threadpool.start(worker)
            #self.coroutine.send(currentWord)     


    def findCorrections(self, currentWord, previous, next):
        
        for x in range(len(self.words_list)): 
            potentialWord = self.words_list[x]
            if(type(potentialWord) == float):
                potentialWord = "nan"
            if(len(potentialWord) == (len(currentWord)-1)): #checking for insertion
                for i in range(len(currentWord)):                        
                    check = currentWord[0:i] + currentWord[i+1:len(currentWord)]
                    if(check == potentialWord):
                        probability = 0
                        if i > 0:
                            letterX = ord(potentialWord[i-1])-97
                            letterY = ord(currentWord[i]) - 97

                            probability = self.ins[letterX][letterY] if i > 0 else 0
                        else: 
                            letterX = ord(potentialWord[i])-97
                            letterY = ord(currentWord[i]) - 97
                            probability = self.ins[letterX][letterY]
                        
                        countP = self.bigram_dict.get((previous,self.words_list[x]))
                        if countP == None:
                            countP = 50000
                        countN = self.bigram_dict.get((self.words_list[x],next))
                        if countN == None:
                            countN = 50000
                        newSuggestion = Suggestion("Insertion", x, "", currentWord[i], i, probability,countP*countN,self.frequencies[x])
                        self.suggestions.append( newSuggestion)
            if(len(potentialWord) == (len(currentWord)+1) and len(currentWord)>0): #check for deletion
                for i in range(len(potentialWord)):
                    check = potentialWord[0:i] + potentialWord[i+1: len(potentialWord)]
                    if(check == currentWord):
                        probability = 0
                        if i > 0:
                            letterX = ord(currentWord[i-1])-97 
                            letterY = ord(potentialWord[i]) - 97
                            probability = self.dele[letterX][letterY] 
                        else:
                            letterX = ord(potentialWord[i])-97
                            letterY = ord(currentWord[i]) - 97
                            probability = self.dele[letterX][letterY]
                            
                        countP = self.bigram_dict.get((previous,self.words_list[x]))
                        if countP == None:
                            countP = 50000
                        countN = self.bigram_dict.get((self.words_list[x],next))
                        if countN == None:
                            countN = 50000
    
                        newSuggestion = Suggestion("Deletion", x, potentialWord[i], "", i, probability,countP*countN,self.frequencies[x] )
                        self.suggestions.append( newSuggestion)
            if(len(potentialWord) == len(currentWord)): #substitution and transposition
                for i in range(len(potentialWord) -1):
                    letterA = potentialWord[i]
                    letterB = currentWord[i+1]
                    if(letterA == letterB):
                        letterA = potentialWord[i+1]
                        letterB = currentWord[i]
                        if(letterB == letterA ):
                            checkA = potentialWord[0:i] + potentialWord[i+2: len(potentialWord)]
                            checkB = currentWord[0:i] + currentWord[i+2:len(currentWord)]
                            if(checkA == checkB):
                                letterX = ord(potentialWord[i])-97
                                letterY = ord(currentWord[i]) - 97
                                probability = self.trans[letterX][letterY]

                                countP = self.bigram_dict.get((previous,self.words_list[x]))
                                if countP == None:
                                    countP = 50000
                                countN = self.bigram_dict.get((self.words_list[x],next))
                                if countN == None:
                                    countN = 50000
    
                                newSuggestion = Suggestion("Transposition", x, potentialWord[i:i+1], currentWord[i:i+1], i, probability,countP*countN,self.frequencies[x])
                                self.suggestions.append( newSuggestion)

                for i in range(len(potentialWord)):
                    checkA = potentialWord[0:i] + potentialWord[i+1: len(potentialWord)]
                    checkB = currentWord[0:i] + currentWord[i+1:len(currentWord)]
                    if(checkA == checkB):
                        letterX = ord(potentialWord[i])-97
                        letterY = ord(currentWord[i]) - 97
                        probability = self.sub[letterX][letterY]

                        countP = self.bigram_dict.get((previous,self.words_list[x]))
                        if countP == None:
                            countP = 50000
                        countN = self.bigram_dict.get((self.words_list[x],next))
                        if countN == None:
                            countN = 50000
    
                        newSuggestion = Suggestion("Substition", x, potentialWord[i], currentWord[i], i, probability, countP*countN,self.frequencies[x])
                        self.suggestions.append( newSuggestion)
        self.suggestions.sort(key=self.sortSuggestions, reverse=True)

        for i in range(8):
            if len(self.suggestions) > i:
                correct = self.suggestions[i]
                item = QtWidgets.QTableWidgetItem( correct.type )
                self.tableWidget.setItem(i, 0, item)
                item = QtWidgets.QTableWidgetItem(self.words_list[correct.wordIndex])
                self.tableWidget.setVerticalHeaderItem(i,item)
                item = QtWidgets.QTableWidgetItem( correct.goodLetter )
                self.tableWidget.setItem(i, 1, item)
                item = QtWidgets.QTableWidgetItem( correct.badLetter )
                self.tableWidget.setItem(i, 2, item)
                item = QtWidgets.QTableWidgetItem( str(correct.position) )
                self.tableWidget.setItem(i, 3, item)
                item = QtWidgets.QTableWidgetItem( self.scientific(correct.probability) )
                self.tableWidget.setItem(i, 4, item)
                item = QtWidgets.QTableWidgetItem(self.scientific(correct.frequency) )
                self.tableWidget.setItem(i, 5, item)
                conditional = correct.probability * float(self.frequencies[correct.wordIndex])
                if(self.bigramToggle.isChecked()):
                    conditional *= correct.bigram
                    item = QtWidgets.QTableWidgetItem(self.scientific(correct.bigram))
                    self.tableWidget.setItem(i, 6, item)
                else:
                    item = QtWidgets.QTableWidgetItem("N\A")
                    self.tableWidget.setItem(i, 6, item)
                item = QtWidgets.QTableWidgetItem(self.scientific(conditional))
                self.tableWidget.setItem(i, 7, item)
            else:
                
                item = QtWidgets.QTableWidgetItem( "" )
                self.tableWidget.setItem(i, 0, item)
                item = QtWidgets.QTableWidgetItem( "" )
                self.tableWidget.setVerticalHeaderItem(i,item)
                item = QtWidgets.QTableWidgetItem( "" )
                self.tableWidget.setItem(i, 1, item)
                item = QtWidgets.QTableWidgetItem( "" )
                self.tableWidget.setItem(i, 2, item)
                item = QtWidgets.QTableWidgetItem( "" )
                self.tableWidget.setItem(i, 3, item)
                item = QtWidgets.QTableWidgetItem( "" )
                self.tableWidget.setItem(i, 4, item)
                item = QtWidgets.QTableWidgetItem( "" )
                self.tableWidget.setItem(i, 5, item)
                item = QtWidgets.QTableWidgetItem( "" )
                self.tableWidget.setItem(i, 6, item)
                item = QtWidgets.QTableWidgetItem( "" )
                self.tableWidget.setItem(i, 7, item)

        return

    def sortSuggestions(self, suggestion):
        bigram = 1
        if self.bigramToggle.isChecked():
            bigram = float(suggestion.bigram)
        return float(suggestion.frequency) * float(suggestion.probability) * bigram
    
    def scientific(self, the_float):
        eSci = "{:e}".format(float(the_float))
        e = eSci.find("e")
        return eSci[0:4] + " * 10^" + eSci[e+1:]

    def createMatrices(self, error_lines):
        
        self.dele = [[1 for x in range(26)] for y in range(26)] 
        self.sub = [[1 for x in range(26)] for y in range(26)] 
        self.trans = [[1 for x in range(26)] for y in range(26)] 
        self.ins = [[1 for x in range(26)] for y in range(26)] 
        self.correctLetter = [1 for x in range(26)]

        for line in error_lines:
            pipe = line.find("|")
            wrong = line[0:pipe]
            if len(wrong) == 1 and wrong in string.ascii_lowercase and line[pipe+1] in string.ascii_lowercase:
                if line[pipe+2] in string.ascii_lowercase in string.ascii_lowercase: #delete
                    right = line[pipe+1:pipe+3]
                    letterX = ord(wrong) - 97
                    letterY = ord(right[1]) - 97
                    frequency = 0.1 * float(line[pipe+3:len(line)] )
                    self.dele[letterX][letterY] = frequency
                else:   #substitute
                    right = line[pipe+1]
                    letterX = ord(right) - 97
                    letterY = ord(wrong) - 97
                    frequency = 0.1 * float(line[pipe+3:len(line)] )
                    
                    self.sub[letterX][letterY] = frequency

            if len(wrong) ==2 and wrong[0] in string.ascii_lowercase and wrong[1] in string.ascii_lowercase and line[pipe+1] in string.ascii_lowercase:
                if line[pipe+2] in string.ascii_lowercase in string.ascii_lowercase: #transposition
                    right = line[pipe+1:pipe+3]
                    letterX = ord(right[0]) - 97
                    letterY = ord(wrong[0]) - 97
                    frequency = 0.1 * float(line[pipe+3:len(line)] )

                    self.trans[letterX][letterY] = frequency
                else:       #insertion
                    right = line[pipe+1]
                    letterX = ord(wrong[0]) - 97
                    letterY = ord(right[0]) - 97
                    frequency = 0.1 * float(line[pipe+3:len(line)] )
                    self.ins[letterX][letterY] = frequency
        for i in range(26):
            frequency = 0
            for j in range(26):
                frequency += self.dele[i][j] + self.trans[i][j] + self.ins[i][j] + self.sub[i][j]
            print("frequency of " + chr(i+97) + " is " + str(frequency)) 


    def cursorPos(self):
        
      #  self.cursorFlag = False
        if(self.cursorFlag):
            myCursor = self.textEdit.textCursor()
            myCursor.setPosition(self.realCursorPosition, QtGui.QTextCursor.MoveMode.MoveAnchor)
            self.textEdit.setTextCursor (myCursor)
            self.cursorFlag = False
        if(self.grayTextFlag):
            _translate = QtCore.QCoreApplication.translate
            self.grayTextFlag = False
            self.textEdit.setTextColor("black")
            self.textEdit.setText("")
        if not self.textEdit.textCursor().atEnd():
            self.setCurrentWord()

