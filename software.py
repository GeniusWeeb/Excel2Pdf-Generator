
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
		#these are drop down box options that you can add on your own
		#they are in a dictioanry format as while rendering from jinja2 , we need to store in dictionary like format
		
		
		#uncomment them if u wanna use them in the same format or tinker with them
		#they serve as refernce scales in a report , and be removed wihout causing any code errors
		#self.HAMA_dict= ['< 01-10:','Mild ' ,'18-24 :','Moderate ','25-30 :',' Severe' ]
		#self.Ybocs_dict= ['08-15 :','Mild OCD' ,'16-23 :','Moderate OCD','24-31 :','Severe OCD','32-40 :','Extreme OCD' ]
		#self.phobia_dict= ['0 :','None' ,'1 :','Mild','2 :','Moderate','3 :','Severe','4 :','Extreme' ]
	    		
		self.check_file = False
		self.confirm = False
		self.setWindowTitle("VAR")
		self.setGeometry(200,200,900,300)
		self.value = " "
		
		#these values are printed out , and we also use them to check 
		#if the selected options in the drop-downboxes are same as these strings, then we print that certain
		#drop-box option
		self.hama = "hama _string"
		self.sara= "sara _string"
		self.phobia="phobia_string"
		self.ybocs = "ybocs_string" 
		
		#created an empty static list to assign data to it later
		self.send = ['','','','','','','','','','']
	    



		self.init_UI()
		



	def init_UI(self):


	   

	

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

    	
    
		


		#creating a file opener here
		#its gonna be created after all the aforementioned content

		self.br = QPushButton("Browse Files",self)
		self.br.setGeometry(425,140,100,30)
		self.br.clicked.connect(self.file_open)





	

      
                




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



		

       


		self.show()



		
	def file_open(self):

		# once the file is returned from qT
		#  we can store into a object called excel_File and then read that into a data frame/
		# then we can use openpyxl to perform actiions on it
		# as well as defining the enabling of the objects there
		try:
			
			self.name, _ = QFileDialog.getOpenFileName(self,'OPEN FILE',options= QFileDialog.DontUseNativeDialog)
			self.check_file = True


		    		
		    
			
			#the below 2 steps can be done in a single step but i just prefered to cache it
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
			
			#these prints statements are essentials to the developers, so far as we are working on the 
			#dev build , and to debug stats once the data excel file has been loaded.


			#status text that appears on the gui
			message = "FILE HAS BEEN LOADED !!"
			
			self.labelST.setText(message)
			self.labelST.setStyleSheet('color : green')
			self.confirm = False
		
			


			

			print("-----------------------DATA SHEET---------------------")
			
		except:
			
			message="FILE HAS NOT BEEN LOADED"
			self.labelST.setText(message)




	#Generates the output file : 
	#these weir check conditions are for us to prevent them from using the buttonwihout loading in a file
	def Gent(self):
		if self.check_file ==  True and self.confirm == False:


			#jinja2 at work here
			try:
				env = Environment(loader=FileSystemLoader('.'))
				template = env.get_template("convert.html")  #refer the cpnvert.html in the repo.
				print(self.send)
    		

				#these can be removed since our content is static and the check tailors
				#the output list/dictionary depending on the number of elements

				if self.cb.currentText() == self.hama:	#comparing checbox options
					#current textbox options and the stored one
					self.send = self.HAMA_dict.copy()  
					#the refernce scale we talked about earlier . ref : lin26
					self.value = "REFERENCE SCALE   :"
					#based on these , we alter the refernce scales
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

					#if we take small refernce scale  , the indexes at 7,8,9 will have null
					#but such a list cant exist during runtime generation
					#therefore we have ,  self.value = "" above in certain cases
			                
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
				
					message="PDF HAS BEEN GENERATED"
					self.labelST.setStyleSheet('color: green')
					self.labelST.setText(message)
					
					
					#clear all fields when successful generation
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



		#		so he can remove the write_pdf part and put it some where else coz it
		#		sans-throws an error so it must be fine in that weasyprint



		#the whole conversion takes place in one function
		# for better reusbality , u can break it down where you like
		#whatever suits your needs

	
				

			
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



