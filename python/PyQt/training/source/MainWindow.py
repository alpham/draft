from PyQt4.QtCore import *
from PyQt4.QtGui import *
from forms.mainwindow import Ui_MainWindow
from libs import facebook
from libs import hdfs
import sys

class MainWindow(QMainWindow,Ui_MainWindow):
	def __init__(self,parent=None):
		self.ui = Ui_MainWindow()
		QMainWindow.__init__(self,parent)
		self.ui.setupUi(self)
		self.setup_connections()

	def setup_connections(self):
		QObject.connect(self.ui.go_pushButton, SIGNAL('clicked()'), self.go_pushButton_function)
		QObject.connect(self, SIGNAL('data_loaded()'), self.update_ui)


	def go_pushButton_function(self):
		token = 'CAACEdEose0cBAOYoE3uX68C6BSzWEonFkdeUZAyy8MXQX4dsZA0WDNd4OgmL5hbLAIbiPJofzgDZCHYokPevpzXCyID9D1tzAEVXJoUCFaxWQM3CM9y78ZBh8PQvm0eOvjdWTaLg8mSQduHpZBSGxpWouttMBuI8qUk06T81jZCTIvvpqjHS27wApHar7D64YVaR1t19kTiQZDZD'
		account_id = self.ui.account_id_lineEdit.text().toUtf8()
		graph = facebook.GraphAPI(token)
		profile = graph.get_object(account_id)
		friends = graph.get_connections(account_id, "friends")
		posts = graph.get_connections(account_id, "posts")	


		friend_list = [friend['name'] for friend in friends['data']]
		posts_list = [post['actions'][0]['link'] for post in posts['data']]

		self.posts_list = QStringList(posts_list)
		self.friends_count = len(friend_list)
		self.ui.friends_count_label.setText(str(self.friends_count)+" friends")
		self.friend_list = QStringList(friend_list)
		self.emit(SIGNAL("data_loaded()"))

	def update_ui(self):
		pass
