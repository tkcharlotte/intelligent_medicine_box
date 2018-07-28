import sys
import cv2
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from test import *
from test1 import *
import zbar
import requests
reload(sys)
sys.setdefaultencoding('utf8')
class MainWindow(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        # put in
        self.put_in_button = QPushButton(self)
        self.put_in_button.setText("Medicine Store")
        self.put_in_button.setFixedHeight(64)
        self.put_in_button.setFixedWidth(128)
        self.put_in_button.clicked.connect(self.put_in)

        # put out
        self.put_out_button = QPushButton(self)
        self.put_out_button.setText("Medicine Deliver")
	self.put_out_button.setFixedHeight(64)
        self.put_out_button.setFixedWidth(128)
        self.put_out_button.clicked.connect(self.put_out)
       
	# shurukuang
	self.nameEdit = QLineEdit(self)	

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.put_in_button)
        self.h_layout.addWidget(self.put_out_button)
	self.h_layout.addWidget(self.nameEdit)
        self.setLayout(self.h_layout)
        self.setGeometry(150, 100, 800, 600)
        self.setFixedHeight(1000)
        self.setFixedWidth(1600)
        self.show()

    def put_in(self):
        # create a reader
  	scanner = zbar.ImageScanner()
    # configure the reader
   	scanner.parse_config('enable')
    	font=cv2.FONT_HERSHEY_SIMPLEX
    	camera=cv2.VideoCapture(0)
    	flag = True
	name = self.nameEdit.text()
    	while(True):
        # Capture frame-by-frame
            grabbed, frame = camera.read()
            if not grabbed:
                break
            pil= Image.fromarray(frame).convert('L')
            width, height = pil.size
            raw = pil.tobytes()
            zarimage = zbar.Image(width, height, 'Y800', raw)
            scanner.scan(zarimage)
            for symbol in zarimage:
        # do something useful with results
                if not symbol.count:
                    print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data
                    url = 'http://118.25.142.175:23333/banzi'
		    url1 = 'http://118.25.142.175:23333/person'
                    info = (symbol.data +' 1 %s') % (name)
		    print info 
                    Data = {"string":info}
                    response = requests.post(url,data=Data)
	            response1 = requests.post(url1,data=Data)
		
                    flag = False
                #cv2.putText(frame,symbol.data,(20,100),font,1,(0,255,0),4)
            if not flag:
                break
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    	camera.release()
    	cv2.destroyAllWindows()

    def put_out(self):
            # create a reader
    	scanner = zbar.ImageScanner()
    # configure the reader
    	scanner.parse_config('enable')
    	font=cv2.FONT_HERSHEY_SIMPLEX
    	name = self.nameEdit.text()
	camera=cv2.VideoCapture(0)
    	flag = True

    	while(True):
        # Capture frame-by-frame
            grabbed, frame = camera.read()
            if not grabbed:
                break
            pil= Image.fromarray(frame).convert('L')
            width, height = pil.size
            raw = pil.tobytes()
            zarimage = zbar.Image(width, height, 'Y800', raw)
            scanner.scan(zarimage)
            for symbol in zarimage:
        # do something useful with results 
                if not symbol.count:
                    print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data
                    url = 'http://118.25.142.175:23333/handsome'
		    url1 = 'http://118.25.142.175:23333/cute'
		    info = (symbol.data +' 0 %s') % (name)
                    Data = {"string":info}
                    response = requests.post(url,data = Data)
		    response1 = requests.post(url1,data = Data)
                    flag = False
                #cv2.putText(frame,symbol.data,(20,100),font,1,(0,255,0),4)
            if not flag:
                break
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        camera.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("Image Mask")
    window = MainWindow()
    sys.exit(app.exec_())

