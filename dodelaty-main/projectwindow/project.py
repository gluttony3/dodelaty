from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow
from PyQt5.QtMultimedia import QMediaPlayer ,QMediaContent
from PyQt5.QtCore import QUrl
class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Створюємо медіа плеер
        self.video1 = QMediaPlayer(self)
        # Вивыд зображення на вивід
        self.video1.setVideoOutput(self.ui.video)
        self.ui.start.clicked.connect(self.video1.play)
        self.ui.stop.clicked.connect(self.video1.stop)

        # Шлях до відео що ми програємо
        #vid = QMediaContent(QUrl.fromLocalFile("videos\\10.avi"))      
        #self.video.setMedia(vid)
        # Запускаємо відео
        #self.video1.play()
        #if self.ui.autostart.isChecked():
            #self.video1.play()
        self.configure()
    def configure(self):
        self.ui.start.clicked.connect(self.starrt)
        self.ui.stop.clicked.connect(self.stopp)
        self.ui.calendarWidget.selectionChanged.connect(self.calendarr)
           
    def stopp(self):
        self.video1.stop()

    def starrt(self):
        self.video1.play()

    def calendarr(self):
        # Дізнатися обрану дату
        date = self.ui.calendarWidget.selectedDate()
        print(date)
        num = date.day()
        vid = QMediaContent(QUrl.fromLocalFile(f"videos\\{num}.avi"))
        self.video1.setMedia(vid)
        if self.ui.autostart.isChecked(): 
            self.video1.play()
   
app = QApplication([])
ex = Widget()
ex.show()
app.exec_()
