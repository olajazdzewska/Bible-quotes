import requests
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QComboBox, \
	QPushButton, QHBoxLayout, QScrollArea, QMainWindow, QAbstractButton
from PySide6 import QtCore, QtGui
from PySide6.QtCore import QSize, Qt


BASE_URL = 'https://uncovered-treasure-v1.p.rapidapi.com'
headers = {
	"X-RapidAPI-Key": "5a02385ce2msh757a37e99c123d5p139cccjsnf1df664f76db",
	"X-RapidAPI-Host": "uncovered-treasure-v1.p.rapidapi.com"
}


def get_random_quote():
	url = BASE_URL + "/random"
	return requests.get(url, headers=headers).json()


def get_json_by_topic(text):
	# elif text == "topic":
	url = BASE_URL + f"/topic/{text}"
	return requests.get(url, headers=headers).json()


def get_quote_by_topic(text):
	result = ""
	for fragment in get_json_by_topic(text)["results"]:
		quote = fragment["text"]
		verse = fragment["scriptures"][0]
		result += '\n' + quote + '\n' + verse + '\n'
	return result



def random_quote_label():
	label = QLabel()
	label.setGeometry(200, 300)
	quote = get_random_quote()["results"][0]["text"]
	verse = get_today_quote()["results"][0]["scriptures"]
	text = f"{quote} \n {verse}"
	label.setText(text)
	# layout.addWidget(label)
	return label

def get_today_quote():
	url = BASE_URL + "/today"
	return requests.get(url, headers=headers).json()

def label_today():

	date = get_today_quote()["results"][0]["date"]
	title = f"Today's quote                                   {date}"
	label = QLabel()
	quote = get_today_quote()["results"][0]["text"]
	verse = get_today_quote()["results"][0]["scriptures"]
	text = f"{title} \n {quote} \n {verse}"
	label.setText(text)
	return label




def search_qlineedit():
	search_by_topic= QLineEdit()
	search_by_topic.setPlaceholderText("enter topic")
	return search_by_topic





def get_random_text():
	quote = get_random_quote()["results"][0]["text"]
	verse = get_today_quote()["results"][0]["scriptures"]
	text = f"{quote} \n {verse}"
	return text


class Scrollable_label(QScrollArea):
	def __init__(self, parent=None, *args, **kwargs):
		super().__init__(parent = parent)
		self.setWidgetResizable(True)
		content = QWidget(self)
		self.setWidget(content)

		# vertical box layout
		lay = QVBoxLayout(content)

		self.label = QLabel(content)

		# making label multi-line
		self.label.setWordWrap(True)

		lay.addWidget(self.label)


	def setText(self, text):
		# setting text to the label
		self.label.setText(text)



class Window(QWidget):
	def __init__(self, parent=None, *args, **kwargs):
		super().__init__(parent=parent)

		self.setGeometry(400, 400, 800, 800)
		self.layout = QVBoxLayout()
		self.layout.addWidget(label_today())
		self.random_quote_button = QPushButton("get random quote")
		self.random_quote_button.setFixedSize(QSize(200, 70))
		self.layout.addWidget(self.random_quote_button, alignment=Qt.AlignHCenter)

		self.random_label = QLabel()
		self.layout.addWidget(self.random_label, alignment=Qt.AlignHCenter)

		#self.random_label.setText(get_random_text())

		self.random_label.hide()

		self.random_quote_button.clicked.connect(self.random_label.setText(get_random_text()))
		self.random_quote_button.clicked.connect(self.random_label.show)

		self.line_edit = search_qlineedit()
		self.line_edit.setFixedSize(QSize(500, 30))
		self.layout.addWidget(self.line_edit, alignment=Qt.AlignHCenter)
		self.button_confirm = QPushButton("search")
		self.button_confirm.setFixedSize(QSize(100,30))
		self.layout.addWidget(self.button_confirm, alignment=Qt.AlignHCenter)
		self.searched_quote_label = Scrollable_label()
		self.layout.addWidget(self.searched_quote_label)

		self.button_confirm.clicked.connect(self.set_topic_label)

		self.setLayout(self.layout)


	def set_topic_label(self):
		self.topic = self.line_edit.text()
		self.searched_quote_label.setText(get_quote_by_topic(self.topic))



	def add_random_label(self):
		label = random_quote_label()
		self.layout.addWidget(label)



if __name__ == '__main__':

	app = QApplication()
	window = Window()
	window.show()
	app.exec()


	headers = {
		"X-RapidAPI-Key": "5a02385ce2msh757a37e99c123d5p139cccjsnf1df664f76db",
		"X-RapidAPI-Host": "uncovered-treasure-v1.p.rapidapi.com"
	}




