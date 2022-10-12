from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu, QMenuBar, QAction, QFileDialog, QDesktopWidget, QLabel, QGridLayout, QActionGroup
from PyQt5.QtGui import QIcon, QImage, QPainter, QPen, QBrush
from PyQt5.QtCore import Qt, QPoint
from PyQt5 import QtWidgets
from PyQt5 import QtGui
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        title="Virtual Whiteboard"

        icon="icons/paint.png"

        self.setWindowTitle(title)
        self.showFullScreen()
        self.setWindowIcon(QIcon(icon))

        self.image= QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

        self.drawing= False
        self.brushSize= 2
        self.brushColor= Qt.black
        self.lastPoint= QPoint()

        mainMenu=self.menuBar()
        fileMenu=mainMenu.addMenu("File")
        brushSize=mainMenu.addMenu("Brush Size")
        brushColor=mainMenu.addMenu("Brush Color")

        quitAction= QtWidgets.QAction("Quit", self.window())
        quitAction.setShortcut("Esc")
        fileMenu.addAction(quitAction)
        quitAction.triggered.connect(self.exit)

        saveAction=QAction(QIcon("icons/save.png"), "Save",self)
        saveAction.setShortcut("Ctrl+S")
        fileMenu.addAction(saveAction)
        saveAction.triggered.connect(self.save)

        clearAction=QAction(QIcon("icons/clear.png"), "Clear",self)
        clearAction.setShortcut("Ctrl+C")
        fileMenu.addAction(clearAction)
        clearAction.triggered.connect(self.clear)

        eraseAction=QAction(QIcon("icons/erase.png"), "Erase",self)
        eraseAction.setShortcut("Ctrl+E")
        fileMenu.addAction(eraseAction)
        eraseAction.triggered.connect(self.erase)

        threepxAction=QAction(QIcon("icons/threepx.png"), "3px", self)
        brushSize.addAction(threepxAction)
        threepxAction.triggered.connect(self.threePixel)

        fivepxAction=QAction(QIcon("icons/fivepx.png"), "5px", self)
        brushSize.addAction(fivepxAction)
        fivepxAction.triggered.connect(self.fivePixel)

        sevenpxAction=QAction(QIcon("icons/sevenpx.png"), "7px", self)
        brushSize.addAction(sevenpxAction)
        sevenpxAction.triggered.connect(self.sevenPixel)

        ninepxAction=QAction(QIcon("icons/ninepx.png"), "9px", self)
        brushSize.addAction(ninepxAction)
        ninepxAction.triggered.connect(self.ninePixel)

        elevenpxAction=QAction(QIcon("icons/elevenpx.png"), "11px", self)
        brushSize.addAction(elevenpxAction)
        elevenpxAction.triggered.connect(self.elevenPixel)

        twentypxAction=QAction(QIcon("icons/twentypx.png"), "20px", self)
        brushSize.addAction(twentypxAction)
        twentypxAction.triggered.connect(self.twentyPixel)

        bucketpxAction=QAction(QIcon("icons/bucketpx.png"), "Bucket", self)
        brushSize.addAction(bucketpxAction)
        bucketpxAction.triggered.connect(self.bucketPixel)

        blackAction=QAction(QIcon("icons/black.png"), "Black", self)
        blackAction.setShortcut("Ctrl+B")
        brushColor.addAction(blackAction)
        blackAction.triggered.connect(self.blackColor)

        whiteAction=QAction(QIcon("icons/white.png"), "White", self)
        whiteAction.setShortcut("Ctrl+W")
        brushColor.addAction(whiteAction)
        whiteAction.triggered.connect(self.whiteColor)

        redAction=QAction(QIcon("icons/red.png"), "Red", self)
        redAction.setShortcut("Ctrl+R")
        brushColor.addAction(redAction)
        redAction.triggered.connect(self.redColor)

        greenAction=QAction(QIcon("icons/green.png"), "Green", self)
        greenAction.setShortcut("Ctrl+G")
        brushColor.addAction(greenAction)
        greenAction.triggered.connect(self.greenColor)

        yellowAction=QAction(QIcon("icons/yellow.png"), "Yellow", self)
        yellowAction.setShortcut("Ctrl+Y")
        brushColor.addAction(yellowAction)
        yellowAction.triggered.connect(self.yellowColor)

        blueAction=QAction(QIcon("icons/blue.png"), "Blue", self)
        blueAction.setShortcut("Ctrl+B")
        brushColor.addAction(blueAction)
        blueAction.triggered.connect(self.blueColor)



    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing= True
            self.lastPoint= event.pos()
            #print(self.lastPoint)


    def mouseMoveEvent(self, event):
        if(event.buttons() & Qt.LeftButton) & self.drawing:
            painter=QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint= event.pos()
            self.update()


    def mouseReleaseEvent(self, event):
        if event.button() ==Qt.LeftButton:
            self.drawing= False

    def paintEvent(self, event):
        canvasPainter=QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())
    

    def save(self):
        filePath, _=QFileDialog.getSaveFileName(self, "Save Image", "", "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*)")
        if filePath=="":
            return
        self.image.save(filePath)

    def exit(self):
        QtWidgets.qApp.quit()

    def clear(self):
        self.image.fill(Qt.white)
        self.update()

    def erase(self):
        self.brushSize= 5
        self.brushColor=Qt.white



    def threePixel(self):
        self.brushSize= 3
    def fivePixel(self):
        self.brushSize= 5
    def sevenPixel(self):
        self.brushSize= 7
    def ninePixel(self):
        self.brushSize= 9
    def elevenPixel(self):
        self.brushSize = 11
    def twentyPixel(self):
        self.brushSize = 20


    def blackColor(self):
        self.brushColor=Qt.black
    def whiteColor(self):
        self.brushColor=Qt.white
    def redColor(self):
        self.brushColor=Qt.red
    def greenColor(self):
        self.brushColor=Qt.green
    def yellowColor(self):
        self.brushColor=Qt.yellow
    def blueColor(self):
        self.brushColor=Qt.blue
    def bucketPixel(self):
        self.image.fill(self.brushColor)



if __name__=="__main__":
    app=QApplication(sys.argv)
    window= Window()
    window.show()
    app.exec()
