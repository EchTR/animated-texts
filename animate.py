# github.com/echtr
# requires "os" and "time" modules

import os 
import time
class at: #at = animated text
	def __init__(self,text,w_time, mode):
		self.text = text
		self.text_list = ""
		self.w_time = w_time
		self.mode = mode
	def animate(self):
		if (self.mode == 1):
			for i in self.text:
				self.text_list = self.text_list + i
				print(self.text_list)
				time.sleep(self.w_time)
				os.system("cls")
			print(self.text_list)
		elif (self.mode == 2):
			for i in self.text:
				self.text_list = self.text_list + i + "-"
				print(self.text_list)
				time.sleep(self.w_time)
				os.system("cls")
			print(self.text_list[0:len(self.text_list)-1])
		elif (self.mode == 3):
			i = len(self.text)
			while True:
				self.text_list = self.text[i-1] + self.text_list
				print(self.text_list)
				time.sleep(self.w_time)
				os.system("cls")
				i-= 1
				if i == 0:
					break
			print(self.text_list)
