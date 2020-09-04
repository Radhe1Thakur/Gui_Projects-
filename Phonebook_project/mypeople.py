from tkinter import *
from tkinter import messagebox
from mongoengine import connect 
from databaseConnect import PhonebookData
from addpeople import AddPeople
from updateWin import Update

# connecting to mongoDB database 
connect(db = 'My_mongo', host = 'mongodb+srv://dbradhe:radhecool@cluster0.dil7k.mongodb.net/My_mongo?retryWrites=true&w=majority')
print('connection established sucessfully!!!!')

class MyPeople(Tk):
    
    def __init__(self):
        super(MyPeople, self).__init__()
        self.geometry('650x600+400+200')
        self.resizable(False,False)
        self.title('My Peoples')
        self.window_view_top('My People')
        self.window_view_bottom()

    def window_view_top(self, win_title):

        # top frame 
        self.top_frame = Frame(self, height = 150, bg = 'grey')
        self.top_frame.place(x= 0, y = 0, relwidth = 1)

        # items in top frame 
        #self.icon = PhotoImage(file = '/home/rsthakur/Desktop/radhe_python/mongo_db/mongo_env/src/tk_projects/Phonebook_project/icon/bo.png')
        #self.icon_label = Label(self.top_frame, image = self.icon, bg = 'grey')
        #self.icon_label.place(x  = 110, y = 40)

        title_label = Label(self.top_frame, text = win_title, font = 'arial 25 bold', bg = 'grey', fg = '#05d9fa')
        title_label.place(x = 200, y = 60)

    def window_view_bottom(self):
        # bottom frame 
        self.bottom_frame = Frame(self, height =400, bg = '#e8a7a2')
        self.bottom_frame.place(x= 0, y = 160, relwidth = 1 )

        # items in bottom Frame
        self.scroll = Scrollbar(self.bottom_frame, orient = VERTICAL)

        self.list_box = Listbox(self.bottom_frame, width = 60, height = 27,font = 'time 10' )
        self.list_box.place(x = 0, y = 0)
        self.list_box.config(yscrollcommand = self.scroll.set)
        self.scroll.config(command = self.list_box.yview)

        self.scroll.place(x= 425, relheight = 1)

        self.list_box_data()        

        # adding button in buttom frame 
        add_btn = Button(self.bottom_frame, text = 'Add', width = 12, pady = 10, font = 'sans 12 bold', bd = 5, bg = '#10525c', fg = 'white',command = self.add_people)
        add_btn.place(x = 465, y = 30)
        
        update_btn = Button(self.bottom_frame, text = 'Update', width = 12, pady = 10, font = 'sans 12 bold', bd = 5, bg = '#10525c', fg = 'white', command = self.update_data)
        update_btn.place(x = 465, y = 100)

        add_btn = Button(self.bottom_frame, text = 'Display', width = 12, pady = 10, font = 'sans 12 bold', bd = 5, bg = '#10525c', fg = 'white', command = self.show_info)
        add_btn.place(x = 465, y = 170)

        add_btn = Button(self.bottom_frame, text = 'Delete', width = 12, pady = 10, font = 'sans 12 bold', bd = 5, bg = '#10525c', fg = 'white', command = self.delete_data)
        add_btn.place(x = 465, y = 240)

        back_btn = Button(self.bottom_frame, text = 'Back', width = 12, pady = 10, font = 'sans 12 bold', bd = 5, bg = '#10525c', fg = 'white', command = self.destroy)
        back_btn.place(x = 465, y = 310)

    def add_people(self):
        add_win = AddPeople()
        add_win.mainloop()

    def update_data(self):
        selected_item = self.list_box.curselection()
        data = self.list_box.get(selected_item)
        d_id = data.split('.')[0]
        
        # making object of Update class 
        up_win = Update(d_id)
        up_win.mainloop()

    def list_box_data(self):
        # extracting data form data base 
        datas = PhonebookData.objects()
        print('data detected')
        count = 0
        self.list_box.delete(0, END)
        for data in datas :
            self.list_box.insert(count, str(data.user_id)+'.'+ data.user_name + ' '+ data.user_email+' '+str(data.user_contact))
            count += 1

    def delete_data(self):
        # selecting data
        selected_item = self.list_box.curselection()
        data = self.list_box.get(selected_item)
        d_id = data.split('.')[0]

        # collecting data from database
        data = PhonebookData.objects(user_id = d_id).get()
        delete = messagebox.askyesnocancel(
                                            'Delete Query',
                                            'Are yo sure to delete data of '+data.user_name
                                          ) 
        if delete == True :
            data.delete()
            self.list_box_data()

    def show_info(self):
        
        self.window_view_top('Person Details')
        # bottom frame 
        self.bottom_frame = Frame(self, height =400, bg = '#e8a7a2')
        self.bottom_frame.place(x= 0, y = 160, relwidth = 1 )

        # collecting data
        selected_item = self.list_box.curselection()
        data = self.list_box.get(selected_item)
        d_id = data.split('.')[0]
        # Extracting data from  data base
        data = PhonebookData.objects(user_id = d_id).get()
        
        # Displaying data
        id_label = Label(self.bottom_frame, text = 'Id : ', font = 'sans 12 bold', bg  = '#464a49', fg = 'white', pady = 10, )
        id_label.place(x= 70, y = 20, width = 150)
        data_id_label = Label(self.bottom_frame, text = data.user_id, font = 'sans 12 bold', bg  = '#464a49', fg = 'white', pady = 10, )
        data_id_label.place(x= 270, y = 20, width = 300)

        name_label = Label(self.bottom_frame, text = 'Name : ', font = 'sans 12 bold', bg  = '#464a49', fg = 'white', pady = 10 )
        name_label.place(x= 70, y = 80, width = 150)
        data_name_label = Label(self.bottom_frame, text = data.user_name, font = 'sans 12 bold', bg  = '#464a49', fg = 'white', pady = 10, )
        data_name_label.place(x= 270, y = 80, width = 300)

        email_label = Label(self.bottom_frame, text = 'Email : ', font = 'sans 12 bold', bg  = '#464a49', fg = 'white', pady = 10 )
        email_label.place(x= 70, y = 140, width = 150)
        data_email_label = Label(self.bottom_frame, text = data.user_email, font = 'sans 12 bold', bg  = '#464a49', fg = 'white', pady = 10, )
        data_email_label.place(x= 270, y = 140, width = 300)

        contact_label = Label(self.bottom_frame, text = 'Phone No. : ', font = 'sans 12 bold', bg  = '#464a49', fg = 'white', pady = 10 )
        contact_label.place(x= 70, y = 200, width = 150)
        data_contact_label = Label(self.bottom_frame, text = data.user_contact, font = 'sans 12 bold', bg  = '#464a49', fg = 'white', pady = 10, )
        data_contact_label.place(x= 270, y = 200, width = 300)

        back_btn = Button(self.bottom_frame, text = 'Back', width = 20,font = 'arial 12 bold',bg = '#10525c', fg = 'white', bd = 5, command = self.go_back)
        back_btn.place(x= 220, y = 300)

    def go_back(self):
        self.window_view_top('My People')
        self.window_view_bottom()