from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox as ms
import sqlite3
from datetime import datetime

white = "#ffffff"
blue = "#2653a0"

# make database 
with sqlite3.connect('data5.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (Username TEXT NOT NULL ,Password TEXT NOT NULL,Aim TEXT NOT NULL);')
c.execute('CREATE TABLE IF NOT EXISTS intake (Username TEXT ,TotalIntake INTEGER, Date datetime);')
c.execute('CREATE TABLE IF NOT EXISTS workouts (Workout_Name TEXT ,Workout_Contents TEXT, Aim TEXT);')
db.commit()
db.close()

#main Class
class Login_Register:
    def __init__(self,master):
    	# Window 
        self.master = master
       
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        self.aimselect = StringVar()
        self.breakfast_Intake = IntVar()
        self.lunch_Intake = IntVar()
        self.dinner_Intake = IntVar()
        self.snacks_Intake = IntVar()
        
        #Create Widgets
        self.widgets()

    #Login Function
    def login(self):
        if self.username.get() == "" and self.password.get() == "":
            ms.showerror('Error!','Username and Password cannot be empty')
        elif self.username.get() == "":
            ms.showerror('Error!','Username cannot be empty')
        elif self.password.get() == "":
                ms.showerror('Error!','Password cannot be empty')
        else:
    	#Establish Connection
            with sqlite3.connect('data5.db') as db:
                c = db.cursor()
            find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
            c.execute(find_user,[(self.username.get()),(self.password.get())])
            result = c.fetchall()
            if result:
                self.logf.pack_forget()
                self.createHub()
            else:
                ms.showerror('Oops!','Username and Password Not Found.')
            
    def new_user(self):
        if self.n_username.get() == "" and self.n_password.get() == "":
            ms.showerror('Error!','Username and Password cannot be empty')
        elif self.n_username.get() == "":
            ms.showerror('Error!','Username cannot be empty')
        elif self.n_password.get() == "":
            ms.showerror('Error!','Password cannot be empty')
        elif self.aimselect.get() == "":
            ms.showerror('Error!','Please select an aim')
##        elif self.aimselect.get() != 'Maintain Fitness' or 'Get Fit' or 'Build Muscle':
##            ms.showerror('Error!','Invalid aim') 
  
##        elif len(self.n_password.get()) <8:
##            ms.showerror('Error!','Password cannot be less than 8 characters')
        else:
            #Establish Connection
            with sqlite3.connect('data5.db') as db:
                c = db.cursor()
            #Find Existing username 
            find_user = ('SELECT * FROM user WHERE username = ?')
            c.execute(find_user,[(self.n_username.get())])
            result = c.fetchall()
            if result:
                ms.showerror('Error!','Username Taken Try a Diffrent One.')
            else:
                ms.showinfo('Success!','Account Created!')
                self.log()
                insert = 'INSERT INTO user(username,password,aim) VALUES(?,?,?)'
                c.execute(insert,[(self.n_username.get()),(self.n_password.get()),(self.aimselect.get())])
            db.commit()

    def intake(self):  #check the inputs then add these to the database
 
        try :
            totalintake = self.breakfast_Intake.get() + self.lunch_Intake.get() + \
            self.dinner_Intake.get() + self.snacks_Intake.get()
            breakfast = self.breakfast_Intake.get()

            if totalintake >10000 or totalintake <500:
                ms.showerror('Error!','Inaccurate calories Please try again!')
    ##        ADD INTEGER CHECK HERE
                print (type(totalintake))
            else :
                print ("is not in range")

            time = str(datetime.now().date())
            with sqlite3.connect('data5.db') as db:
                c = db.cursor()   
                insert = 'INSERT INTO intake(username,TotalIntake,date) VALUES(?,?,?)'
                c.execute(insert,[(self.username.get()),(totalintake),time])
            db.commit()           
             
 
        except :
                # print (type(totalintake))
                print ("you can open windows here")
                ms.showerror('Error!','You write a string or empty .. And I am Cool and Handsome!')
                        
   


        
    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()
    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()
    def exit_button(self):
         root.destroy()

   
    #Draw Widgets
    def widgets(self):
        self.head = Label(self.master,text = 'DJB FITNESS TRACKER',font = ('Century Gothic',35),padx=10, pady=10,bg=blue, fg=white)
        self.head.pack(fill=BOTH)
        self.logf = Frame(self.master,padx=159,pady=130, bg=blue)
     
        Label(self.logf,text = 'Username: ',font = ('Century Gothic', '29'),fg=white,bg=blue,pady=25,padx=5).grid(row = 0,sticky = W)
        Entry(self.logf,textvariable = self.username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.logf,text = 'Password: ',font = ('Century Gothic', '29'),pady=1,padx=1,bg=blue,fg=white).grid(sticky = W)
        Entry(self.logf,textvariable = self.password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.logf,text = ' Login ',bd = 3 ,font = ('',15),padx=6,pady=6,command=self.login).grid(row=3,column=0)
        Button(self.logf,text = ' Create Account ',bd = 3 ,font = ('',15),padx=6,pady=6,command=self.cr).grid(row=3,column=1)
        Button(self.logf,text = ' EXIT ',bd = 3 ,font = ('',15),padx=6,pady=6,command = self.exit_button).grid(row=4,column=0)
        self.logf.pack()

        
        self.crf = Frame(self.master,padx=102,pady=100,bg=blue)
        Label(self.crf,text = 'Username: ',font = ('Century Gothic', '29'),pady=3,padx=3,fg=white,bg=blue).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.crf,text = 'Password: ',font = ('Century Gothic', '29'),pady=5,padx=5,fg=white,bg=blue).grid(sticky = W)
        Label(self.crf,text = 'Aim: ',font = ('Century Gothic', '29'),fg=white,bg=blue).grid(sticky = W)

        self.combo = ttk.Combobox(self.crf,width=15,textvariable= self.aimselect)
        self.combo['values'] = ("Maintain Fitness", "Get Fit", "Build Muscle")
        self.combo.grid(column = 1,sticky=W)
       
        Entry(self.crf,textvariable = self.n_password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.crf,text = 'Create Account',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.new_user).grid(row=8,column=0)
        Button(self.crf,text = 'Back to login',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.log).grid(row=8,column=1)

        
    def createHub(self):
        self.hub= Label(self.master,text = 'Calorie Intake',font = ('Century Gothic',35),padx=10,bg=blue, fg=white)
        self.hub.pack(fill=BOTH)
        self.hub = Frame(self.master,padx=10,pady=35 ,bg=blue, width=101, height=193)
        
        Label(self.hub,text = 'Please enter your calorie intake for today: ',font = ('Century Gothic', 19),fg=white,bg=blue).pack()
        Label(self.hub,text = 'Breakfast: ',font = ('Century Gothic', 14),fg=white,bg=blue).pack()
        Entry(self.hub,textvariable = self.breakfast_Intake,bd = 5,font = ('',9)).pack()
        Label(self.hub,text = 'Lunch: ',font = ('Century Gothic', '14'),bg=blue,fg=white).pack()
        Entry(self.hub,textvariable = self.lunch_Intake,bd = 5,font = ('',9)).pack()
        Label(self.hub,text = 'Dinner: ',font = ('Century Gothic', '14'),bg=blue,fg=white).pack()
        Entry(self.hub,textvariable = self.dinner_Intake,bd = 5,font = ('',9)).pack()
        Label(self.hub,text = 'Snacks: ',font = ('Century Gothic', '14'),bg=blue,fg=white).pack()
        Entry(self.hub,textvariable = self.snacks_Intake,bd = 5,font = ('',9)).pack()
        Label(self.hub,text ='',font = ('Century Gothic', 11),fg=white,bg=blue).pack()
        Button(self.hub,text = ' Continue ',bd = 5 ,font = ('Century Gothic',15),padx=15,pady=15,command=self.intake).pack()
        Label(self.hub,text ='',font = ('Century Gothic', 10),fg=white,bg=blue).pack()
        Label(self.hub,text = 'Please enter 0 if no calories were consumed ',font = ('Century Gothic', 19),fg=white,bg=blue).pack()

        self.hub.pack(fill=BOTH)

    def calorietoworkout(self):

        getaim = ('SELECT aim FROM user WHERE username = ?')
        
        
    def workoutpage(self):
        self.workout= Label(self.master,text = 'Workout',font = ('Century Gothic',35),padx=10,bg=blue, fg=white)
        self.hub.pack(fill=BOTH)
        self.hub = Frame(self.master,padx=10,pady=35 ,bg=blue, width=101, height=193)


        workout_name 
        Label(self.hub,text = 'Please enter your calorie intake for today: ',font = ('Century Gothic', 19),fg=white,bg=blue).pack()
        Label(self.hub,text = 'Breakfast: ',font = ('Century Gothic', 14),fg=white,bg=blue).pack()
        Entry(self.hub,textvariable = self.breakfast_Intake,bd = 5,font = ('',9)).pack()
        Label(self.hub,text = 'Lunch: ',font = ('Century Gothic', '14'),bg=blue,fg=white).pack()
        Entry(self.hub,textvariable = self.lunch_Intake,bd = 5,font = ('',9)).pack()
        Label(self.hub,text = 'Dinner: ',font = ('Century Gothic', '14'),bg=blue,fg=white).pack()
        Entry(self.hub,textvariable = self.dinner_Intake,bd = 5,font = ('',9)).pack()
        Label(self.hub,text = 'Snacks: ',font = ('Century Gothic', '14'),bg=blue,fg=white).pack()
        Entry(self.hub,textvariable = self.snacks_Intake,bd = 5,font = ('',9)).pack()
        Label(self.hub,text ='',font = ('Century Gothic', 11),fg=white,bg=blue).pack()
        Button(self.hub,text = ' Continue ',bd = 5 ,font = ('Century Gothic',15),padx=15,pady=15,command=self.intake).pack()
        Label(self.hub,text ='',font = ('Century Gothic', 10),fg=white,bg=blue).pack()
        Label(self.hub,text = 'Please enter 0 if no calories were consumed ',font = ('Century Gothic', 19),fg=white,bg=blue).pack()

     
root = Tk()
root.title("DJB Fitness Tracker")
#root.geometry("667x489+650+150")
Login_Register(root)
root.mainloop()
