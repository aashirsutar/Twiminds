# -*- coding: utf-8 -*-
import sys
import tweepy

from PyQt4 import QtCore, QtGui
from tw import Ui_Dialog

class StartQt4(QtGui.QMainWindow):
  def __init__(self, parent=None):
    QtGui.QWidget.__init__(self, parent)
    self.ui = Ui_Dialog()
    self.ui.setupUi(self)
    
    
    QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.tweet_write)
   
  def tweet_write(self):
    CONSUMER_KEY = 'Account Consumer Key'
    CONSUMER_SECRET = 'Account Consumer Secret'
    ACCESS_KEY = 'Account Access Key'
    ACCESS_SECRET = 'Account Access Secret'

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    api.update_status(self.ui.textEdit.toPlainText())
    self.ui.textEdit.clear()  
    #self.ui.label.text = 140-len(self.ui.textEdit.html)
    
    
if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  myapp = StartQt4()
  myapp.show()
  sys.exit(app.exec_())
  