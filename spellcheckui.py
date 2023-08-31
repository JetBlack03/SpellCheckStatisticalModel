# Form implementation generated from reading ui file 'stat418.ui'
#
# Created by: PyQt6 UI code generator 6.4.2

import string
from PySide6 import QtCore, QtWidgets, QtGui, QtCore
from PyQt6.QtCore import *
from suggestion import Suggestion, WordSuggestionPair
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
        #this sets the height of the table
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(19, 24, 887, 473))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textEdit = QtWidgets.QTextEdit(parent=self.verticalLayoutWidget)
        self.textEdit.setMaximumSize(QtCore.QSize(519, 53))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.textChanged.connect(self.textEntered)
        self.textEdit.cursorPositionChanged.connect(self.cursorPos)
        self.textEdit.selectionChanged.connect(self.newHighlight)
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
        
        self.bigramToggle = QtWidgets.QCheckBox("Context-Aware Correcting")
        self.bigramToggle.clicked.connect(self.setCurrentWord)
        self.verticalLayout_3.addWidget(self.bigramToggle)
        self.bigramToggle.setChecked(True)
        self.realToggle = QtWidgets.QCheckBox("Real-word Errors")
        self.realToggle.clicked.connect(self.setCurrentWord)
        self.verticalLayout_3.addWidget(self.realToggle)
        self.realToggle.setChecked(True)
        #self.verticalLayout_3.addWidget(self.horizontalLayout)
        self.info = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.info.setObjectName("info")
        self.info.setGeometry(800,0,80,80)
        self.info.clicked.connect(self.showWelcomeScreen)
        self.info.setIcon(QtGui.QIcon('info.png'))
        self.info.setIconSize(QtCore.QSize(75,75))
        self.infoText = open("welcome.txt").read()


        self.question = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.question.setObjectName("question1")
        self.question.setText("?")
        self.question.setGeometry(180,155,16,16)
        self.question.clicked.connect(self.showDialogBigram)

        self.question2 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.question2.setObjectName("question2")
        self.question2.setText("?")
        self.question2.clicked.connect(self.showDialogReal)
        self.question2.setGeometry(180,180,16,16)
        
        self.tableWidget = QtWidgets.QTableWidget(parent=self.verticalLayoutWidget)
        self.tableWidget.cellDoubleClicked.connect(self.tableSelected)
        self.tableWidget.itemClicked.connect(self.headerSelected)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(8)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        #self.tableWidget.horizontalHeader().setFixedWidth()
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.horizontalHeader().sectionClicked.connect(self.headerSelected)
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

        self.welcomeBox = QtWidgets.QMessageBox()
        self.msgBox = QtWidgets.QMessageBox()
        self.msgBox2 = QtWidgets.QMessageBox()
        self.msgBoxProb = QtWidgets.QMessageBox()

        self.retranslateUi(SpellCheck)
        QtCore.QMetaObject.connectSlotsByName(SpellCheck)
        self.grayTextFlag = True
        self.tableWidget.setFocus()

        self.threadpool = QThreadPool() 

        self.input_list = []


        
    def inputs(self):
        print(self.ins[0][1])

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
        item.setText(_translate("SpellCheck", "P(X|W)"))
        item.setToolTip("This is the odds of me doing your mom")
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("SpellCheck", "Unigram P(W)"))
        item.setStatusTip("this is the odds of your mom doing me")
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("SpellCheck", "Bigram P(W)"))
        item.setWhatsThis("whats this? oh its me doing your mom")
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("SpellCheck", "P(W|X)"))
        

        
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)


    def newHighlight(self):
        pass
        # print(str(self.textEdit.textCursor().selectionStart()) + " to " + str(self.textEdit.textCursor().selectionEnd()))

    def showWelcomeScreen(self):
        self.welcomeBox.setWindowTitle("Noisy Channel Model for Spellchecking and Autocorrect")
        self.welcomeBox.setWindowIconText("Welcome")
        self.welcomeBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.welcomeBox.setFixedSize(500,500)
        self.welcomeBox.setTextFormat(QtCore.Qt.TextFormat.RichText)
        opening = "Welcome! This program demonstrates the noisy-channel model used for autocorrect. This statistical model ranks potential corrections and displays the most probable ones to the user."
        link = "\n This application is based on the following <a href='https://web.stanford.edu/~jurafsky/slp3/B.pdf'>Stanford paper.<\a>"
        
        self.welcomeBox.setText(opening + link)
        self.welcomeBox.setInformativeText(self.infoText)


        self.welcomeBox.exec()

    def showDialogBigram(self):
        self.msgBox.setIcon(QtWidgets.QMessageBox.Information)
        self.msgBox.setText("When this option is on, the probability of a correction being next to the words before and after it is considered. This is based off of a limited dataset, which may missing some common word pairs, so you have the option to turn it off.")
        self.msgBox.setWindowTitle("Context-Aware Correction")
        self.msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)

        self.msgBox.exec()
        
    def showDialogReal(self):
        self.msgBox2.setIcon(QtWidgets.QMessageBox.Information)
        self.msgBox2.setText("When this option is on, the application will try to find potential corrections in a word even if it is in the dictionary.")
        self.msgBox2.setWindowTitle("Real-word Correction")
        self.msgBox2.setStandardButtons(QtWidgets.QMessageBox.Ok)

        self.msgBox2.exec()

    def headerSelected(self, index):
        if index == 4:
            self.showConditional()
        elif index == 5:
            self.showUnigram()
        elif index == 6:
            self.showBigram()

    def tableSelected(self, row, column):
        if column == 4:
            self.showConditional()
        elif column == 5:
            self.showUnigram()
        elif column == 6:
            self.showBigram()
    
    def showConditional(self):
        self.msgBoxProb.setText("P(X|W) represents the probability of mistyping a word W as a non-word X. In other words, the probability of making the given error (substitution, transposition, deletion, insertion)")
        self.msgBoxProb.setWindowTitle("P(X|W)")
        self.msgBoxProb.setStandardButtons(QtWidgets.QMessageBox.Ok)

        self.msgBoxProb.exec()
    
    def showUnigram(self):
        self.msgBoxProb.setText("P(W) represents the probability of word W being typed regardless of context. It is based on a dataset comprising millions of modern English texts that ranks the most common words by their frequency")
        self.msgBoxProb.setWindowTitle("Unigram P(W)")
        self.msgBoxProb.setStandardButtons(QtWidgets.QMessageBox.Ok)

        self.msgBoxProb.exec()
    
    def showBigram(self):
        self.msgBoxProb.setText("The bigram probability is the probability of the word W appearing next to the words before and after it. The dataset for this is much more limited and prone to bad results, so I have included an option to exclude this value from the calculation.")
        self.msgBoxProb.setWindowTitle("Bigram P(W)")
        self.msgBoxProb.setStandardButtons(QtWidgets.QMessageBox.Ok)

        self.msgBoxProb.exec()

    def textEntered(self):
        #about all words
        
        newestCharPos = self.textEdit.textCursor().position()-1
        newestCharPos = 0 if newestCharPos < 0 else newestCharPos
        newestNextCharPos = newestCharPos + 1
        newestChar = ""
        newestNextChar = " "

        deleted = len(self.textEdit.toPlainText()) < self.numberOfCharacters 
        
        self.numberOfCharacters = len(self.textEdit.toPlainText())
        atEnd = self.textEdit.textCursor().atEnd()

        if self.textEdit.toPlainText() != None and len(self.textEdit.toPlainText()) > newestCharPos:
            newestChar = self.textEdit.toPlainText()[newestCharPos] 
            if len(self.textEdit.toPlainText()) > newestNextCharPos:
                newestNextChar = self.textEdit.toPlainText()[newestNextCharPos] 
        
        deletedWord = deleted and ((newestChar in string.punctuation) or (newestChar in string.whitespace)) 
        deletedWord = deletedWord and ((newestNextChar in string.punctuation) or (newestNextChar in string.whitespace)) 

        if (newestChar in string.punctuation) or (newestChar in string.whitespace) or (not atEnd) or deleted:
            if(self.underlineFlag):
        
                currentWord = self.getCurrentWord()
                translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
                inputWords = self.textEdit.toPlainText().translate(translator).split()
                
                startPos = 0
                for i in range(len(inputWords)):
                    word = inputWords[i]

                    #modifying the list of word-suggestion pairs. Accurate as long as there was no highlight
                    if len(inputWords) > len(self.input_list):          
                        if i >= len(self.input_list): #inserting a word at the end
                            inDictionary =  currentWord.lower() in self.words_list
                            inputWord = WordSuggestionPair(currentWord, inDictionary)
                            self.input_list.append(inputWord)
                            print("word add " + currentWord + str(self.input_list))
                            if i > 0:
                                self.findBigramProbabilities(i-1)

                            worker = Worker(self.findCorrections, i)
                            self.threadpool.start(worker)
                        elif self.input_list[i].word != word: #inserting a word in the middle
                            inDictionary =  word.lower() in self.words_list
                            inputWord = WordSuggestionPair(word, inDictionary)
                            self.input_list.insert(i,inputWord)
                            print("word ins " + word + str(self.input_list))

                            if i > 0:
                                self.findBigramProbabilities(i-1)
                            if len(self.input_list) > i+2:
                                self.findBigramProbabilities(i+1)

                            worker = Worker(self.findCorrections, i)
                            self.threadpool.start(worker)                            
                    elif self.input_list[i].word != word:
                        if deletedWord: #deleting a word
                            deleted = False
                            ex = self.input_list.pop(i) 
                            #print("word del " + ex + str(self.input_list))

                            self.setCurrentWord()

                            if i > 0:
                                self.findBigramProbabilities(i-1)
                            self.findBigramProbabilities(i)
                        elif len(self.input_list) > i+1 and word == self.input_list[i].word + self.input_list[i+1].word: 
                            deleted = False #deleting space in between words
                            ex = self.input_list.pop(i)    
                            self.input_list[i].word = word 
                            self.input_list[i].correct = word.lower() in self.words_list
                            #print("space del " + ex + str(self.input_list))
                            
                            worker = Worker(self.findCorrections, i)
                            self.threadpool.start(worker)

                            if i > 0:
                                self.findBigramProbabilities(i-1)
                            if len(self.input_list) > i+2:
                                self.findBigramProbabilities(i+1)

                        else: #modifying an existing word (maybe at end)
                            self.input_list[i].word = word
                            self.input_list[i].correct = word.lower() in self.words_list
                            #print("word sub " + str(self.input_list[i]) + str(self.input_list))

                            worker = Worker(self.findCorrections, i)
                            self.threadpool.start(worker)
                            if i > 0:
                                self.findBigramProbabilities(i-1)
                            if len(self.input_list) > i+2:
                                self.findBigramProbabilities(i+1)

                if deleted and ((newestChar in string.punctuation) or (newestChar in string.whitespace)):
                    for i in range(len(self.input_list) - len(inputWords)):
                        ex = self.input_list.pop()
                        #print("word deleted " + str(ex) + str(inputWords) + newestChar)
                        
                        self.findBigramProbabilities(len(self.input_list)-1)

                for i in range(len(self.input_list)):
                    if self.input_list[i].word != inputWords[i]:
                        self.textEdit.setEnabled(False)
                        print("failure")
                        print(str(self.input_list))
                        print(str(inputWords))
                if len(inputWords) > len(self.input_list):
                    self.textEdit.setEnabled(False)
                    print("failure")
                    print(str(self.input_list))
                    print(str(inputWords))

                self.rewriteText()       
                #self.textEdit.setFontPointSize(8)
                
            
                #about the current word 
                if atEnd:
                    self.setCurrentWord()
                



        self.underlineFlag = True
        
        
    def rewriteText(self):
        plainString = self.textEdit.toPlainText()
        newString = ""
        startPos = 0
        self.textEdit.setTextColor("black")
        self.textEdit.setFontUnderline(False)
        for i in range(len(self.input_list)):
            pos = plainString.find(self.input_list[i].word, startPos)
            endPos = pos + len(self.input_list[i].word) 
            newString += plainString[startPos:pos]
            #the word
            if self.input_list[i].correct:
                typedWord = self.input_list[i].word
                suggestedWord = typedWord
                if len(self.input_list[i].suggestions) > 0:
                    suggestedWord = self.words_list[self.input_list[i].suggestions[0].wordIndex]
                if self.realToggle.isChecked() and  suggestedWord != typedWord:
                    newString += "<u style='color:DarkSlateBlue;'>" + plainString[pos:endPos] + "</u>"
                    #newString += "<u style='text-decoration: underline;text-decoration-color: blue;'>" + plainString[pos:endPos] + "</u>"
                else:
                    newString += plainString[pos:endPos]
                

            else:
                newString += "<u style='color:red;'>" + plainString[pos:endPos] + "</u>"
            startPos = endPos
        if startPos < len(plainString):
            newString += plainString[startPos:len(plainString)]
        
        self.underlineFlag = False
        self.cursorFlag = True
        self.realCursorPosition = self.textEdit.textCursor().position()
        
        self.textEdit.setText(newString)   

    def getCurrentWord(self):
        
        spaceAdded = self.textEdit.toPlainText() + " "
        endOfWord = spaceAdded.find(" ", self.textEdit.textCursor().position())
        myString = self.textEdit.toPlainText()[0:endOfWord]
        translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
        noPunctuation = myString.strip().translate(translator)

        currentWord = noPunctuation.rpartition(" ")[2]
        return currentWord

    def printbutton(self):
        print(self.textEdit.toHtml())
       # print(self.textEdit.toPlainText().translate(str.maketrans('','',string.punctuation)))
        
    def setCurrentWord(self):
        _translate = QtCore.QCoreApplication.translate
        if self.bigramToggle.isChecked():
            self.realToggle.setEnabled(True)
        else:
            self.realToggle.setEnabled(False)

        cursorPosition = self.textEdit.textCursor().position()
    
        index = 0
        
        if self.textEdit.textCursor().atEnd():
            index = len(self.input_list) - 1
        else:
            startPos = 0
            for i in range(len(self.input_list)):
                
                startPos = self.textEdit.toPlainText().find(self.input_list[i].word, startPos)
                if cursorPosition >= startPos and cursorPosition <= startPos + len(self.input_list[i].word):
                    index = i
                startPos += len(self.input_list[i].word)

        currentWord = self.getCurrentWord()
        if currentWord != self.input_list[index].word:
            print("misfire")

        inDictionary = self.input_list[index].correct
        self.label.setText(_translate("SpellCheck", "Current word: " + currentWord))
        self.label_2.setText(_translate("SpellCheck", "Dictionary Match" if inDictionary else "No Dictionary Match"))

        if(not inDictionary) or self.realToggle.isChecked():

            self.displaySuggestions(index)


    def findCorrections(self, index):
        
        currentWord = self.input_list[index].word 
        self.input_list[index].suggestions = []
        self.input_list[index].totalP = .0001
        self.input_list[index].totalF = .0001
        self.input_list[index].totalBigramOff = 0.0001

        for x in range(len(self.words_list)): 
            potentialWord = self.words_list[x]
            if(potentialWord == currentWord): 
                
                newSuggestion = Suggestion("No error", x, "", "", 0, 95,self.frequencies[x])
                self.input_list[index].addSuggestion(newSuggestion)
                self.input_list[index].totalF += float(self.frequencies[x])
            else:
                
                if(type(potentialWord) == float):
                    potentialWord = "nan"
                if(len(potentialWord) == (len(currentWord)-1)): #checking for insertion
                    probability = 0
                    a = 0
                    for i in range(len(currentWord)):                        
                        check = currentWord[0:i] + currentWord[i+1:len(currentWord)]
                        if(check == potentialWord):
                            
                            if i > 0:
                                letterX = ord(potentialWord[i-1])-97
                                letterY = ord(currentWord[i]) - 97

                                probability += self.ins[letterX][letterY] if i > 0 else 0
                            else: 
                                letterX = ord(potentialWord[i])-97
                                letterY = ord(currentWord[i]) - 97
                                probability += self.ins[letterX][letterY]
                            
                            a = i
                    if probability > 0:
                        newSuggestion = Suggestion("Insertion", x, "", currentWord[a], a, probability,self.frequencies[x])
                        self.input_list[index].addSuggestion(newSuggestion)
                        self.input_list[index].totalP += probability
                        self.input_list[index].totalF += float(self.frequencies[x])
                        self.input_list[index].totalBigramOff += probability * float(self.frequencies[x])

                if(len(potentialWord) == (len(currentWord)+1) and len(currentWord)>0): #check for deletion
                    probability = 0
                    a = 0
                    for i in range(len(potentialWord)):
                        check = potentialWord[0:i] + potentialWord[i+1: len(potentialWord)]
                        if(check == currentWord):
                            if i > 0:
                                letterX = ord(currentWord[i-1])-97 
                                letterY = ord(potentialWord[i]) - 97
                                probability = self.dele[letterX][letterY] 
                            else:
                                letterX = ord(potentialWord[i])-97
                                letterY = ord(currentWord[i]) - 97
                                probability = self.dele[letterX][letterY]
                               
                            newSuggestion = Suggestion("Deletion", x, potentialWord[i], "", i, probability,self.frequencies[x] )
                            self.input_list[index].addSuggestion(newSuggestion)
                            self.input_list[index].totalP += probability
                            self.input_list[index].totalF += float(self.frequencies[x])
                            self.input_list[index].totalBigramOff += probability * float(self.frequencies[x])

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
        
                                    newSuggestion = Suggestion("Transposition", x, potentialWord[i:i+1], currentWord[i:i+1], i, probability,self.frequencies[x])
                                    self.input_list[index].addSuggestion(newSuggestion)
                                    self.input_list[index].totalP += probability
                                    self.input_list[index].totalF += float(self.frequencies[x])
                                    self.input_list[index].totalBigramOff += probability * float(self.frequencies[x])

                    for i in range(len(potentialWord)):
                        checkA = potentialWord[0:i] + potentialWord[i+1: len(potentialWord)]
                        checkB = currentWord[0:i] + currentWord[i+1:len(currentWord)]
                        if(checkA == checkB):
                            letterX = ord(potentialWord[i])-97
                            letterY = ord(currentWord[i]) - 97
                            probability = self.sub[letterX][letterY]

                            newSuggestion = Suggestion("Substition", x, potentialWord[i], currentWord[i], i, probability, self.frequencies[x])
                            self.input_list[index].addSuggestion(newSuggestion)
                            self.input_list[index].totalP += probability
                            self.input_list[index].totalF += float(self.frequencies[x])
                            self.input_list[index].totalBigramOff += probability * float(self.frequencies[x])

        if self.input_list[index].correct:
            self.input_list[index].totalP *= 20
            for i in self.input_list[index].suggestions:
                if i.type == "No error":
                    i.probability = self.input_list[index].totalP * 0.95


        self.findBigramProbabilities(index)

        if self.realToggle.isChecked():
            self.displaySuggestions(index)

        return
    
    def findBigramProbabilities(self,index):

        previous = "" 
        next = "" 
        if index > 0:
            previous = self.input_list[index-1].word 
        if index < len(self.input_list) - 1:
            next = self.input_list[index+1].word 
                
        self.input_list[index].totalB = .0001
        self.input_list[index].totalBigramOn = 0.0001
        
        for suggestion in self.input_list[index].suggestions:
            
            countP = self.bigram_dict.get((previous,self.words_list[suggestion.wordIndex]))
            if countP == None:
                countP = 50000
            countN = self.bigram_dict.get((self.words_list[suggestion.wordIndex],next))
            if countN == None:
                countN = 50000
            suggestion.bigram = countN*countP
            self.input_list[index].totalB += countN*countP
            self.input_list[index].totalBigramOn += countN*countP * suggestion.probability * float(suggestion.frequency)
        
        self.input_list[index].sortList(self.bigramToggle.isChecked())

    def displaySuggestions(self, index):

        
        for i in range(8):
            if len(self.input_list[index].suggestions) > i:
                
                correct = self.input_list[index].suggestions[i]                    
                
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
                item = QtWidgets.QTableWidgetItem( self.percentage(correct.probability / self.input_list[index].totalP) )
                self.tableWidget.setItem(i, 4, item)
                item = QtWidgets.QTableWidgetItem(self.percentage(float(correct.frequency) / self.input_list[index].totalF) )
                self.tableWidget.setItem(i, 5, item)
                conditional = correct.probability * float(correct.frequency)  / self.input_list[index].totalBigramOff
                if(self.bigramToggle.isChecked()):
                    conditional *= (correct.bigram * self.input_list[index].totalBigramOff) / self.input_list[index].totalBigramOn
                    item = QtWidgets.QTableWidgetItem(self.percentage(correct.bigram / self.input_list[index].totalB))
                    self.tableWidget.setItem(i, 6, item)
                else:
                    item = QtWidgets.QTableWidgetItem("N\A")
                    self.tableWidget.setItem(i, 6, item)
                item = QtWidgets.QTableWidgetItem(self.percentage(conditional))
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

    def scientific(self, the_float):
        eSci = "{:e}".format(float(the_float))
        e = eSci.find("e")
        return eSci[0:4] + " * 10^" + eSci[e+1:]
    def percentage(self,the_float):

        return f"{float(the_float)*100:.3f}%"


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
                if line[pipe+2] in string.ascii_lowercase: #transposition
                    right = line[pipe+1:pipe+3]
                    letterX = ord(right[0]) - 97
                    letterY = ord(wrong[0]) - 97
                    frequency = 0.1 * float(line[pipe+3:len(line)] )

                    self.trans[letterX][letterY] = frequency
                else:       #insertion
                    right = line[pipe+1]
                    letterX = ord(wrong[1]) - 97
                    letterY = ord(right[0]) - 97
                    frequency = 0.1 * float(line[pipe+3:len(line)] )
                    self.ins[letterX][letterY] = frequency
        


    def cursorPos(self):
        
        if(self.cursorFlag):
            myCursor = self.textEdit.textCursor()
            myCursor.setPosition(self.realCursorPosition, QtGui.QTextCursor.MoveMode.MoveAnchor)
            self.textEdit.setTextCursor (myCursor)
            self.cursorFlag = False
        if(self.grayTextFlag):
            _translate = QtCore.QCoreApplication.translate
            self.numberOfCharacters = 0
            self.grayTextFlag = False
            self.textEdit.setTextColor("black")
            self.textEdit.setText("")
            

        if not self.textEdit.textCursor().atEnd():
            self.setCurrentWord()

