#Find PI to the Nth Digit


from tkinter import ttk 
import tkinter
from tkinter import messagebox

def ERROR_MSG():
     #pop up error massage and clear entry box
     messagebox.showinfo('ERROR','Please enter a number between 1 and 15')
     entryBox.delete(0,'end')

def input_check(event):
     #check user input is only integer between 1 and 15
     try:
         entryNum = int(entryBox.get())
     except:
          ERROR_MSG()
     else:
          if entryNum > 15 or entryNum < 1:
               ERROR_MSG()
          else:
               Nth_Digit(entryNum)
         

def Nth_Digit(Nth):
     #write in the approxLabel the pi number to the nearest number we got from user
     #write global variable of pi to the nearest the number we got from user
     global pi_to_the_nearst_Nth
     pi =str(22/7)
     pi_to_the_nearst_Nth = float(pi[:Nth+2])
     approxLabel.Config(pi_to_the_nearst_Nth)
     return pi_to_the_nearst_Nth


def window_size(w=260, h=80):
     #lock window size
     window.minsize(width=w, height=h)
     window.maxsize(width=w, height=h)
     window.resizable(width=False, height=False)


def copy(event):
     #copy pi
     window.clipboard_clear()
     window.clipboard_append(pi_to_the_nearst_Nth)
     

class labels(object):
     #i thought i may write many labels so, i thought this would decrease it 

     def __init__(self,master,text,rowPosition=0,columnPosition=0):
          self.label = ttk.Label(master,text=text)
          self.label.grid(row = rowPosition,column = columnPosition)

     def Config(self,textt,rrelief='flat'):
          self.label.config(text=textt,relief=rrelief,width = 15)
          

     
          
class btns(object):
     #same that i thought in Labels

     def __init__(self,master,text,rowPosition=0,columnPosition=0):
          self.btn = ttk.Button(master,text=text)
          self.btn.grid(row = rowPosition,column = columnPosition)
          self.btn.bind('<1>',input_check)
          

     def Bind(self,inpt,func):
          self.btn.bind(inpt,func)
          

window = tkinter.Tk()
window.title('Find PI to the Nth Digit')
window.iconbitmap('LOGO.ico')
window_size()

infoLabel = labels(window, 'Find PI to the Nth Digit:' ,1)
approxLabel = labels(window,'Enter an integer!' ,2 ,2)

entryBox = ttk.Entry(window, width = 5, justify = 'center')
entryBox.grid( row = 2 )

getApprox_Btn = btns(window,"Get approximation.",3)
getApprox_Btn.Bind('<1>',input_check)

copyApprox_Btn = btns(window,"Copy approximation.",3 ,2)
copyApprox_Btn.Bind('<1>',copy)



window.mainloop()

