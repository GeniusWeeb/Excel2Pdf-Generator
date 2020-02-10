
# do something
# version2.1 -> now we implement a file opender for the final product version
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QLineEdit,QFileDialog ,QFormLayout ,QLabel ,QComboBox , QHBoxLayout,QWidget
from pyqt5_tools import Qt
from PyQt5 import QtGui
from PyQt5.QtGui import QFont,QIcon,QPixmap
from jinja2 import Environment,FileSystemLoader
from weasyprint import HTML , CSS 
import pandas as pd
import sys





class window(QMainWindow):  
	def __init__(self):

		super(window,self).__init__()
		self.HAMA_dict= ['< 17 :','Mild Security' ,'18-24 :','Mild to Moderate Severity','25-30 :','Moderate to Severe' ]
		self.Ybocs_dict= ['08-15 :','Mild OCD' ,'16-23 :','Moderate OCD','24-31 :','Severe OCD','32-40 :','Extreme OCD' ]
		self.phobia_dict= ['0 :','None' ,'1 :','Mild','2 :','Moderate','3 :','Severe','4 :','Extreme' ]
	    		
		self.check_file = False
		self.confirm = False
		self.setWindowTitle("VAR")
		self.setGeometry(200,200,900,300)
		self.value = " "
		self.hama = "Hamlilton Anxiety Rating Scale"
		self.sara= "Self-Assessment of Resilience and Anxiety Scale"
		self.phobia="Severity Measure for Specific Phobia -Adult"
		self.ybocs = "Yale-Brown Obsessive Compulsive Scale" 
		self.send = ['','','','','','','','','','']
	    



		self.init_UI()
		



	def init_UI(self):


	   

	#	self.button  = QPushButton(self);
	#	self.button.setText("Press me sir")

	#	self.button.setGeometry(800,450,100,100)
	#	self.button.clicked.connect(self.but_press)

		font =QtGui.QFont()
		font.setBold(True)


		color = QtGui.QColor()
		color.blue()


		#adding combobox
		

		layout = QHBoxLayout()


		self.cb = QComboBox(self)
		self.cb.addItem('Hamlilton Anxiety Rating Scale')
		self.cb.addItem('Self-Assessment of Resilience and Anxiety Scale')
		self.cb.addItem('Yale-Brown Obsessive Compulsive Scale')
		self.cb.addItem('Severity Measure for Specific Phobia -Adult')
		self.cb.setGeometry(230,140,80,20)


		#image for 

		self.label4 = QLabel(self)
		self.label4.setPixmap(QPixmap('MainLogo.png'))
		self.label4.setGeometry(402,-280,900,650)
	

		#warning and other content

		self.labelN = QLabel(self)
		self.labelN.setGeometry(250,70,70,20)
		self.labelN.setText("NAME")
		self.labelN.setFont(font)
		self.labelN.setStyleSheet('color : black')





	#	self.label1.setStyleSheet('color : black')

		self.label2 = QLabel(self)
		self.label2.setGeometry(460,70,70,20)
		self.label2.setText("AGE")
		self.label2.setFont(font)
		self.label2.setStyleSheet('color : black')


		self.labelWT = QLabel(self)
		self.labelWT.setText("STATUS : ")
		self.labelWT.setGeometry(300,220,150,100)
		self.labelWT.setFont(font)
		self.labelWT.setStyleSheet('color : black')

		self.labelST = QLabel(self)
		  # //status message
		self.labelST.setGeometry(400,170,150,200)
		self.labelST.setFont(font)
		self.labelST.setStyleSheet('color : red')


		self.labe3 = QLabel(self)
		self.labe3.setGeometry(650,70,70,20)
		self.labe3.setText("GENDER")
		self.labe3.setFont(font)
		self.labe3.setStyleSheet('color : black')

    	
    
		

	#	self.LE = QLineEdit(self)
	#	self.LE.setGeometry(800,50,100,100)


	#	self.Progress = QProgressBar(self)
	#	self.Progress.setGeometry(400,400,300,20)

	#	self.b = QPushButton('download', self)
	#	self.b.clicked.connect(self.show_down)

		#creating a file opener here
		#its gonna be created after all the aforementioned content

		self.br = QPushButton("Browse Files",self)
		self.br.setGeometry(425,140,100,30)
		self.br.clicked.connect(self.file_open)





	#	self.DataSend  = QPushButton("Submit Data",self)
	#	self.DataSend.setGeometry(200,220,100,100)

	# sending data of Age to the excel file and modifying contents
	#	self.DataSend.clicked.connect(self.Excel_Edit)

      
                




		self.Gen = QPushButton(self)
		self.Gen.setText("GenereateD")
		self.Gen.setGeometry(425,180,100,30)
		self.Gen.clicked.connect(self.Gent)


      
	
		self.NameE = QLineEdit(self)			#at bottom
		self.NameE.setGeometry(200,90,130,20)
		
		




		self._age = QLineEdit(self)
		self._age.setGeometry(415,90,130,20)
		

		self._gender = QLineEdit(self)
		self._gender.setGeometry(600,90,130,20) #at BOPTTOM



		#self.setLayout(layout)


       


		self.show()



		
	def file_open(self):

		# once the file is returned from qT
		#  we can store into a obejct called excel_File and then read that indo a data frame/
		# then we can use openpyxl to perform actiions on it
		# as well as defining the enabling of the objects there
		try:
			
			self.name, _ = QFileDialog.getOpenFileName(self,'OPEN FILE',options= QFileDialog.DontUseNativeDialog)
			self.check_file = True


		    		
		    
			

			self.file = pd.ExcelFile(self.name)
			self.Temp_Sheet = pd.read_excel(self.file ,encoding = 'utf-8',index = False )
			
		
			self.Temp_Sheet.index+=1
			self.Temp_Sheet['Timestamp'] = pd.to_datetime(self.Temp_Sheet['Timestamp'])
			self.Temp_Sheet['Timestamp'] = self.Temp_Sheet['Timestamp'].dt.strftime('%d-%m')
			self.Temp_Sheet.rename(columns = {'Timestamp':'Date'} , inplace = True)
			print(self.Temp_Sheet)
				
			self.Main_Sheet = self.Temp_Sheet.T
			
			print(self.Main_Sheet)
			print("-----------------------DATA TYPES--------------------------")
			



		
			message = "FILE HAS BEEN LOADED !!"
			
			self.labelST.setText(message)
			self.labelST.setStyleSheet('color : green')
			self.confirm = False
		
			


			

			print("-----------------------DATA SHEET---------------------")
			
		except:
			
			message="FILE HAS NOT BEEN LOADED"
			self.labelST.setText(message)
		#	self.label.setText("No file has been added")



#	def Excel_Edit(self):	
	# we are going to make us of  self.AgeEdit.text() here and modify the data
		print("")
		#all excel edits gui and stuff to be made  here
		#all connections

#	def reset(self):
#		print("HI we are here")
#		self.check_file = False
#		self.confirm = False






#	def show_down(self):
#		self.completed = 0

#		while self.completed <100:
			
#			self.completed+=0.0001
#			self.Progress.setValue(self.completed)
			
			
			
# this is a cusotm pop up  message box

#	def but_press(self):
#		mes = QMessageBox.question(self,"this is a sample string","are you sure?",QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,QMessageBox.No)
#		if mes == QMessageBox.Yes:
#			self.label.setText("he pressed Yes")
#		elif mes == QMessageBox.No:
			
#			self.label.setText(self.LE.text())
#		else:
#			self.label.setText("he pressed cancel")
	
	
		
		
			


#gen and save together










	def Gent(self):
		if self.check_file ==  True and self.confirm == False:



			try:
				env = Environment(loader=FileSystemLoader('.'))
				template = env.get_template("convert.html")
				print(self.send)
    		



				if self.cb.currentText() == self.hama:
					self.send = self.HAMA_dict.copy()
					self.value = "REFERENCE SCALE   :"
					self.send.insert(6,'')
					self.send.insert(7,'')
					self.send.insert(8,'')
					self.send.insert(9,'')


					print("this is hama")
					
				if self.cb.currentText() == self.sara:
					print("this is sara")
					self.value = " "
				if self.cb.currentText() == self.ybocs:
					self.send = self.Ybocs_dict.copy()
					self.value = "REFERENCE SCALE  :"
					self.send.insert(8,'')
					self.send.insert(9,'')
					print("this is ybocs")
				if self.cb.currentText() == self.phobia:
					self.value = "REFERENCE SCALE :"
					self.send = self.phobia_dict.copy()
					print("this is phobia")
				
				print(self.send)
				print(type(self.send))
				
			#we need to define variables and holders here  for them to be stylized		
				template_vars = {"title" : self.cb.currentText(),
			                   "HAMA_DATA": self.Main_Sheet.to_html(justify='left',col_space=3,show_dimensions= False, ),
			           #      "HAMA_DATA": change(self),


			                
			                 "NAME": self.NameE.text(),
			                 'AGE' : self._age.text(),
			                 'GENDER': self._gender.text(),
			                 'ref':self.value,
			                 'range1': self.send[0],
			                 'value1':self.send[1],
			                 'range2': self.send[2],
			                 'value2':self.send[3],
			                 'range3': self.send[4],
			                 'value3':self.send[5],
			                 'range4': self.send[6],
			                 'value4': self.send[7],
			                 'range5': self.send[8],
			                 'value5': self.send[9],

			                 
			                 


			                 


			                 }


			    #this is the main template part that gets genrated
				html_out = template.render(template_vars)

				self.name, _ = QFileDialog.getSaveFileName(self,'SAVE FILE',self.tr("PDF files (*.pdf)"),options= QFileDialog.DontUseNativeDialog)
				print(type(self.name))
				if (len(self.name) == 0):
					message="FILE LOADED,ENTER NAME !!"
					self.labelST.setText(message)
					self.check_file = True

				else:
					self.check_file = True	
					HTML(string=html_out).write_pdf("{0}.pdf".format(self.name),stylesheets=['style.css'],presentational_hints =True)
					print(self.name)
				#	print(template_vars['title'])
					message="PDF HAS BEEN GENERATED"
					self.labelST.setStyleSheet('color: green')
					self.labelST.setText(message)
					
					self.NameE.clear()
					self._age.clear()
					self._gender.clear()
					self.value = " "
					self.send = ['','','','','','','','','','']
					self.confirm = True


				try:
					self.reset(self)	
				except:
					print("reset not working")	


	
	 	
			


					

				
				
		#		




		#		so he can remove the write_pdf part and put it some where else coz it
		#		sans-throws an error so it must be fine in that weasyprint





	
				


			except:
				message="ERROR !! NOT PRINTED"
				self.labelST.setText(message)
	  			

		else:
			message="FILE NOT SELECTED !!"
			self.labelST.setText(message)
		    #self.Gen.setText('Select FILE')  	










if __name__ == "__main__":

	app = QApplication(sys.argv)
	widget = QWidget()
	win  = window()
	sys.exit(app.exec_())



