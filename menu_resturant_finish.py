import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
import datetime


#this class give seller access on menu
class seller:
    def __init__(self,master):
        self.master = master
        master.title('Restaurant')
        
        #make a count of foods
        with open("C:/Users/parisa/OneDrive/Desktop/university/projects/menu.txt",'r') as file:
            lines = file.readlines()
            self.counter = len(lines)

        self.menubar = tk.Menu(self.master)
        self.master.config(menu = self.menubar)
        
        #make 4 option in menubar: open menu , add or remove a food , show list of customers , reset the list of customers
        self.menu_file = tk.Menu(self.master,tearoff = False,bg='pink')
        self.menubar.add_cascade(menu= self.menu_file,label="menu")
        self.menu_file.add_command(label="open file..." ,command=lambda master = self.master: self.open_menu(master))
        self.menu_file.add_command(label="add or remove...",command=lambda master = self.master:self.add_remove(master))
        self.menu_file.add_command(label="show customers...",command=lambda master = self.master:self.show_customer(master))
        self.menu_file.add_command(label='reset the customers list...',command=lambda master = self.master:self.reset(master))

        self.main_frame = tk.Frame(self.master,bg='oliveDrab1')
        self.main_frame.grid(row=0,column=0,sticky='nsew')

        #make a list to contain buttens
        self.butts = [[''for i in range(2)]for i in range(self.counter)] 
        
        #make a list to contain entrys,labels,...
        self.add_sth = []
    
    #make a func to reset the list of customers
    def reset(self,master):
        self.__init__(master)
        with open("C:/Users/parisa/OneDrive/Desktop/university/projects/list_of_customer.txt",'w') as customers:
            return  
    
    #make a func to open menu
    def open_menu(self,master):
        self.__init__(master)
        #open menu and make an inter userface of that
        with open("C:/Users/parisa/OneDrive/Desktop/university/projects/menu.txt",'r') as menu:
            list_food = menu.readlines()
            for food in list_food :
                list_new = food.split()
                frame = tk.Frame(self.main_frame,bg='oliveDrab1')
                i = int(food[0])
                frame.grid(row=i-1 , column=0)
                label_name = tk.Label(frame,text=f'{list_new[0]}.{list_new[1]}',bg='oliveDrab1')
                label_name.grid(row=0,column=0)
                
                #make sure that the color of available and unavailable are difrent
                color=''
                if list_new[2]=='available':
                    color='PaleGreen1'
                else:
                    color='OrangeRed'

                butt_exist = tk.Button(frame,text=list_new[2] ,bg=color,command=lambda l = list_food, j = int(food[0]):self.change(l,j,"exist"))
                butt_exist.grid(row=0,column=1)

                prise = tk.Entry(frame)
                prise.grid(row=0,column=2)
                
                #save the new prise
                butt_save = tk.Button(frame,text=f'prise ={list_new[3]}',bg='pink',command=lambda l = list_food,j = int(food[0]):self.change(l,j,'prise'))
                butt_save.grid(row=0,column=3)

                self.butts[i-1] = [prise,butt_exist,butt_save]
    
    #a func that change the prise
    def change(self,l,i,t):
        with open("C:/Users/parisa/OneDrive/Desktop/university/projects/menu.txt",'w') as new_menu:
            if t == "exist":
                food = l[i-1].split()
                if food[2] == "available":
                    food[2] = 'unavailable'
                    self.butts[i-1][1]['bg']=color='OrangeRed'
                else:
                    food[2] = 'available'
                    self.butts[i-1][1]['bg']=color= 'PaleGreen1' 
                self.butts[i-1][1]['text'] = food[2]          
            else:
                food = l[i-1].split()
                food[3] = self.butts[i-1][0].get()
                self.butts[i-1][2]['text'] =f'prise = {food[3]}'
            string = ''
            for item in food:
                string += item
                string += ' '
            string += '\n'
            l[i-1] = string
            new_menu.writelines(l)

    #make a func for add or remove a food        
    def add_remove(self,master):
        self.__init__(master)
        frame_add = tk.Frame(self.main_frame,bg='PaleGreen')
        frame_add.grid(row=0,column=0,sticky='ewns')

        label_name = tk.Label(frame_add,text='name:',bg='PaleGreen')
        label_name.grid(row=0,column=0)

        entry_name = tk.Entry(frame_add)
        entry_name.grid(row=0,column=1)
        self.add_sth.append(entry_name)

        label_prise = tk.Label(frame_add,text='prise:',bg='PaleGreen')
        label_prise.grid(row=1,column=0)

        entry_prise = tk.Entry(frame_add)
        entry_prise.grid(row=1,column=1)
        self.add_sth.append(entry_prise)

        label_image = tk.Label(frame_add,text='enter the address of image:',bg='PaleGreen')
        label_image.grid(row=2,column=0)

        entry_image = tk.Entry(frame_add)
        entry_image.grid(row=2,column=1)
        self.add_sth.append(entry_image)

        var = tk.IntVar()
        checkbox_av = tk.Checkbutton(frame_add,text='available',variable=var ,bg='PaleGreen')
        checkbox_av.grid(row=3,column=0)
        self.add_sth.append(var)

        butt_add = tk.Button(frame_add,text='add',bg='green',command=self.add)
        butt_add.grid(row=4,column=0)

        frame_remove = tk.Frame(self.main_frame,bg='orange')
        frame_remove.grid(row=1,column=0,sticky='ewns')

        label = tk.Label(frame_remove,text="enter the number of food that you want to remove it:",bg='orange')
        label.grid(row=0,column=0)

        entry_remove = tk.Entry(frame_remove)
        entry_remove.grid(row=0,column=1)
        self.add_sth.append(entry_remove)

        butt_remove = tk.Button(frame_remove,text='remove',bg='orangeRed',command=self.remove)
        butt_remove.grid(row=1,column=0)

    #a func for add a food(command of add Butt)    
    def add(self):
        self.counter += 1
        if self.add_sth[0].get() == '' or self.add_sth[1].get() == '' or self.add_sth[2].get() == '':
            messagebox.showerror(message="the entrys must be contain somthing")
            return 
        with open("C:/Users/parisa/OneDrive/Desktop/university/projects/menu.txt",'a') as new_menu:
            ex = "unavailable"
            if self.add_sth[3].get() == 1:
                ex = "available"
            new_menu.write(f'{self.counter} {self.add_sth[0].get()} {ex} {self.add_sth[1].get()} {self.add_sth[2].get()}\n')

    #a func for remove a food(command of remove butt)        
    def remove(self):
        if self.add_sth[4].get() == '':
            messagebox.showerror(message="the entry must be contains somthing")
            return
        
        r = int(self.add_sth[4].get())

        if r not in range(1,self.counter+1):
            messagebox.showerror(message=f"the entry must contains a number in range 1 to {self.counter} ")
            return
        
        with open("C:/Users/parisa/OneDrive/Desktop/university/projects/menu.txt",'r') as menu:
            lines = menu.readlines()
            lines.pop(r-1)
        with open("C:/Users/parisa/OneDrive/Desktop/university/projects/menu.txt",'w') as new_menu:
            for i in range(len(lines)):
                line = lines[i]
                list_word = line.split()
                list_word[0] = str(i+1)
                string = ''
                for word in list_word:
                    string += word
                    string += ' '
                string += '\n'
                lines[i] = string        
            new_menu.writelines(lines)    
    #this func open and show the list of customers file    
    def show_customer(self,master):
        self.__init__(master)
        with open("C:/Users/parisa/OneDrive/Desktop/university/projects/list_of_customer.txt",'r') as file:
            lines = file.readlines()
            for i in range(len(lines)):
                line = lines[i]
                label = tk.Label(self.main_frame,text=line,bg='oliveDrab1')
                label.grid(row=i,column=0)        

#make a class to give customer access to menu                
class customer:
    def __init__(self,master):
        self.master = master
        master.title('Restaurant')
        self.menubar = tk.Menu(self.master)
        self.master.config(menu = self.menubar)

        self.menu_file = tk.Menu(self.master,tearoff = False,bg='pink')
        self.menubar.add_cascade(menu= self.menu_file,label="menu")
        self.menu_file.add_command(label="show menu" ,command=lambda master = self.master: self.show_menu(master))
        self.menu_file.add_command(label="show basket",command=self.show_basket)            

        self.frame = tk.Frame(self.master,bg='oliveDrab1')
        self.frame.grid(row=0,column=0,sticky='snew')
        self.main_frame = tk.Frame(self.frame,bg='oliveDrab1')
        self.main_frame.grid(row=0,column=0,sticky='snwe')
        
        self.empty_image = self.load_image('C:/Users/parisa/OneDrive/Desktop/university/projects/empty.jpg')
        
        self.list_image = []

        self.basket = {}
        with open("C:/Users/parisa/OneDrive/Desktop/university/projects/menu.txt",'r') as file:
            lines = file.readlines()
            for line in lines:
                words = line.split()
                self.basket[words[1]] = [0,words[3]]
                try:
                    self.list_image.append(self.load_image(words[4] + ' ' + words[5]))
                except:
                    self.list_image.append(self.empty_image)
        self.sth = []
        
    #this func opens the menu file and amake an inter userfsce of that
    def show_menu(self,master):
        self.__init__(master)
        with open("C:/Users/parisa/OneDrive/Desktop/university/projects/menu.txt",'r') as menu:
            lines = menu.readlines()
            for i in range(len(lines)):
                line = lines[i].split()

                frame = tk.Frame(self.main_frame,bg='oliveDrab1')
                frame.grid(row=i,column=0,sticky='nswe')
                
                label_image = tk.Label(frame,text='',image=self.list_image[i])
                label_image.grid(row=0,column=0,sticky='wsne')

                label_name = tk.Label(frame,text=line[1],bg='oliveDrab1')
                label_name.grid(row=0,column=1)

                label_prise = tk.Label(frame,text=line[3],bg='oliveDrab1')
                label_prise.grid(row=0,column=2)

                if line[2] == 'available':
                    butt_add = tk.Button(frame,text="add to basket",bg='green',command=lambda index = int(line[0]),l = lines,indx = i:self.add_to_basket(index,l,indx))
                    butt_add.grid(row=0,column=3)

                    butt_remove = tk.Button(frame,text="remove",bg='orangeRed1',command=lambda index = int(line[0]),l = lines,indx = i:self.remove_from_basket(index,l,indx))
                    butt_remove.grid(row=0,column=4)

                    label_count = tk.Label(frame,text=0)
                    label_count.grid(row=0,column=5)

                    self.sth.append(label_count)        
                else:
                    label = tk.Label(frame,text='unavailable',bg='orangered')
                    label.grid(row=0,column=3)    
    
    #a func to add the food that customer choose to basket
    def add_to_basket(self,index,l,i):
        line = l[index-1].split()
        prise_num = self.basket.get(line[1])
        prise_num[0] += 1
        self.sth[i]['text'] += 1 
       
    #a func to remove a food from basket
    def remove_from_basket(self,index,l,i):
        line = l[index-1].split()
        prise_num = self.basket.get(line[1])
        if prise_num[0] != 0:
            prise_num[0] -= 1
            self.sth[i]['text'] -= 1
        else:
            return    
        
    #a func to show basket for customer
    def show_basket(self):
        self.main_frame.destroy()
        index = 0
        plus = 0
        for food,prise_num in self.basket.items():
            if prise_num[0] != 0:
                plus += int(prise_num[1]) * int(prise_num[0])
                label_name = tk.Label(self.frame,text=food)
                label_name.grid(row=index,column=0)

                label_prise = tk.Label(self.frame,text=f'prise ={prise_num[1]}  number ={prise_num[0]}') 
                label_prise.grid(row=index,column=1)

                index += 1
        label_plus_prise = tk.Label(self.frame,text=f'total prise:{plus}',bg='pink')
        label_plus_prise.grid(row=index,column=0)

        label_user_name = tk.Label(self.frame,text='enter your name:',bg='pink')
        label_user_name.grid(row=index+1,column=0)

        entry_name = tk.Entry(self.frame)
        entry_name.grid(row=index+2,column=0)

        butt_save = tk.Button(self.frame,text='save',bg='green',command=lambda en = entry_name,p = plus:self.save(en,p))
        butt_save.grid(row=index+3,column=0)
    
    # save the basket and name of customer
    def save(self,ent,plus):
        now = datetime.datetime.today()
        mounth = str(now.month)
        day = str(now.day)
        year = str(now.year)
        hour = str(now.hour)
        minute = str(now.minute)
        second = str(now.second)
        with open("C:/Users/parisa/OneDrive/Desktop/university/projects/list_of_customer.txt",'a') as customers:
            if ent.get() != '':
                newlist={}
                for food , num_price in self.basket.items():
                    if num_price[0]!=0:
                        newlist[food]=num_price
                customers.write(f'name:{ent.get()}    foods:[number,prise] ={newlist} total prise ={plus}  data: {mounth}/{day}/{year}   {hour}:{minute}:{second}\n')
                messagebox.showinfo(message="your order has been saved.thank you for choice!")
            else:
                messagebox.showerror(message='please enter your name')
                return    

    def load_image(self,choice):
        image = Image.open(choice)
        image = image.resize((100, 100))
        photo = ImageTk.PhotoImage(image)
        return photo
            
#global value         
user = ''
entry=''
frame=''

#identify the user(customer or seller)
def find_user():
    global frame
    window = tk.Tk()
    window.resizable(width=False, height=False)
    window.geometry('300x300')
    window.rowconfigure(0, minsize=50, weight=1)
    window.columnconfigure(0, minsize=50, weight=1)
    #frame=tk.Frame(window,bg='oliveDrab1')
    #frame.grid(row=0,column=0,sticky="nsew")

    label = tk.Label(window,text="chose:(customer or seller)",bg='oliveDrab1')
    button_customer = tk.Button(window,text="customer",command = lambda win = window: accept_pass(win,"customer"),bg='pink')
    button_seller = tk.Button(window,text="seller",command=lambda win = window:accept_pass(win,"seller"),bg='Pink')
   
    label.grid(row=0,column=0)
    button_customer.grid(row=50,column=0)
    button_seller.grid(row=50,column=1)
    
    window.mainloop()

#prove that user is seller    
def accept_pass(window,us):
    global entry
    global frame
    if us == "customer":
        frame.destroy
        cust=customer(window)
        window.mainloop()
        
    else:
        label = tk.Label(frame,text="enter the password:",bg='oliveDrab1')
        entry = tk.Entry(frame)
        check_butt = tk.Button(frame,text="check password",command=lambda w=window:check_pass(w),bg='pink')

        label.grid(row=2,column=0)
        entry.grid(row=2,column=1)
        check_butt.grid(row=2,column=2)
        
def check_pass(window):
    global entry
    global frame
    password=entry.get()

    if password == '1234':
        frame.destroy
        sell=seller(window)
        window.mainloop()
    else:
        messagebox.showerror(message="the password is not correct")

        
find_user()

