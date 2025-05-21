from PyQt5 import QtWidgets, QtCore
from ui8 import Ui_MainWindow  # Import the generated class
import qqueue as q
from fpdf import FPDF
import os




# Create a class inheriting from FPDF
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Report Header", ln=True, align="C")

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

pdf = PDF()
pdf.add_page()

# Set font and add a title
pdf.set_font("Arial", size=12)


# Save the PDF




class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        # self.maximize.clicked.connect(lambda: app.exit())
        # # self.minimize.clicked.connect(lambda: app.exit())

        # self.frame_5.mouseMoveEvent = self.MoveWindow

        self.queue = q.Queue()
        self.enqueueButton.clicked.connect(self.setDisplay)
        self.dequeButton.clicked.connect(self.setPreview)
        self.printButton.clicked.connect(self.printPdf)
        self.dispayBox.setText("[]")

        self.cache = []
    # def MoveWindow(self, event):
    #     if self.isMaximized == False:
    #         self.Move(self.pos() + event.globalPos() - self.clickPosition)
    #         self.clickPosition = event.globalPost()
    #         event.accept()
    #         pass
    
    # def mousePressEvent(self, event):
    #     self.clickPosition = event.globalPos()
    #     pass

    def setDisplay(self):
        self.previewBox.clear()
        text = self.inputBox.text()


        if text.isdigit() and text not in self.cache:
            
            self.queue.enqueue(int(text))
            self.cache.append(text)
            
            # print("is text")
        elif not text.isdigit() and text not in self.cache:
            self.queue.enqueue(text)
            self.cache.append(text)
            # print("is int")       
        self.inputBox.clear()
        self.dispayBox.setText(str(self.queue.queue))
            
            
    
    def setPreview(self):
        self.previewBox.setText(str(self.queue.dequeue()))
        # print(self.queue.dequeue())
        self.dispayBox.setText(str(self.queue.queue))
        
    
    def get_file_name(self):
        while True:
            nu = 1
            filename = "report"+str(nu)+".pdf"

            if not os.path.exists(filename):
                return filename
                nu += 1
            else:
                return "report.pdf"

    def printPdf(self):
        
        text = self.previewBox.toPlainText()
        print(text)
        if len(text) <= 0:
            print("None")
        else:
            text = str(self.previewBox.toPlainText())+".pdf"
            print(text)
            pdf.cell(200,10, text, ln=True, align='C')
            pdf.output(text)
            self.previewBox.clear()

if __name__ == "__main__":          
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())