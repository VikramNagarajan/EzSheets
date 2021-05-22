#importing modules
from tkinter import *
import os
import tkinter.font as tkFont
from PIL import Image, ImageTk, ImageFilter
from selenium import webdriver

#opening homepage
root = Tk()
root.title('Sapience')

#title
appTitleImage = Image.open(r'C:\Users\owner\Desktop\Visual Studio Code Projects\SapienceLogo(1).png')
appTitleImage = appTitleImage.resize((506, 156))
appTitleImage = ImageTk.PhotoImage(appTitleImage)
appTitle = Label(root, image=appTitleImage)
appTitle.pack()

#slogan
appSloganFont = tkFont.Font(family='Impact', size=20, slant=tkFont.ITALIC)
appSlogan = Label(root, text='Study Better, Study Smarter', fg='#4670B6', font=appSloganFont)
appSlogan.pack()

#spacer
ButtonFont = tkFont.Font(family='Arial', size=15, weight=tkFont.BOLD)
spacer = Label(root, text='', font=ButtonFont)
spacer.pack()


#ezsheets
def ezsheetsCommand():
  from selenium import webdriver
  from selenium.webdriver.common.keys import Keys
  import time

  worksheetWindow = Toplevel(root)
  worksheetWindow.title('EzSheets')
  wsFont = tkFont.Font(family='Arial', size=15)
  worksheetText = Label(worksheetWindow, text="What worksheet would you like to search for?", font=wsFont)
  wsButton = Button(worksheetWindow, text='Submit', font=wsFont, command=sheetsInit)
  sheetInp = Entry(worksheetWindow, width=50)
  worksheetText.pack()
  wsButton.pack()
  sheetInp.pack()
  
def sheetsInit():
  PATH = "C:\Program Files (x86)\chromedriver.exe"
  driver = webdriver.Chrome(PATH)

  driver.get("https://www.google.com/")
  search = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
  search.send_keys(str(sheetInp.get()) + " worksheet pdf")
  search.send_keys(Keys.RETURN)
  driver.find_element_by_xpath("//a[contains(@href, '.pdf')]").click()

noteIm = Image.open(r'C:\Users\owner\Desktop\Visual Studio Code Projects\SapienceLogo(1).png')
noteIm = noteIm.resize((270, 211))
noteIm = ImageTk.PhotoImage(noteIm)   
smartNotesButton = Button(root, image=noteIm, borderwidth=0, bg='white', fg='black', font=ButtonFont, command=ezsheetsCommand)
smartNotesButton.pack()

#Spacer
spacer1 = Label(root, text='', font=ButtonFont)
spacer1.pack()

root.mainloop()
