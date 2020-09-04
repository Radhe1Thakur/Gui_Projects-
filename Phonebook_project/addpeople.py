from tkinter import *
from tkinter import messagebox
from mongoengine import connect 
from databaseConnect import PhonebookData

# connecting to database 
connect(db = 'My_mongo', host = 'mongodb+srv://dbradhe:radhecool@cluster0.dil7k.mongodb.net/My_mongo?retryWrites=true&w=majority')
print('connection established sucessfully!!!!!!')

class AddPeople(Tk):
    
    def __init__(self):
        super(AddPeople, self).__init__()
        self.geometry('650x600+400+200')
        self.resizable(False,False)
        self.title('My Peoples')
        self.Addwindow_view()

    def db_store(self):

        print('calling function ')

        # reading data entered 
        id = self.id_entry.get()
        name = self.name_entry.get()
        email = self.email_entry.get()
        contact = self.contact_entry.get()

        if id and name and email and contact != "" :
            # adding data to database 
            data = PhonebookData(
                user_id = id,
                user_name = name,
                user_email = email,
                user_contact = contact
            )
            try :
                data.save()
                self.id_entry.delete(0, END)
                self.name_entry.delete(0, END)
                self.email_entry.delete(0, END)
                self.contact_entry.delete(0, END)
            except Exception as e:
                messagebox.showerror('Error in Entry',str(e))
        else:
            messagebox.showerror('Field Error', 'All field must  be filled....', icon = 'warning') 
        


    def Addwindow_view(self):

        # top frame 
        self.top_frame = Frame(self, height = 150, bg = 'grey')
        self.top_frame.pack(fill = X)

        # variables for Entry 
        self.id_var = IntVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.contact_var = IntVar()


        # items in top frame 
        #self.icon = PhotoImage(file = '/home/rsthakur/Desktop/radhe_python/mongo_db/mongo_env/src/tk_projects/Phonebook_project/icon/bo.png')
        #self.icon_label = Label(self.top_frame, image = self.icon, bg = 'grey')
        #self.icon_label.place(x  = 110, y = 40)

        title_label = Label(self.top_frame, text = 'Add People', font = 'arial 25 bold', bg = 'grey', fg = '#05d9fa')
        title_label.place(x = 200, y = 60)

        # bottom frame 
        self.bottom_frame = Frame(self, height =400, bg = '#e8a7a2')
        self.bottom_frame.pack(fill = X, pady = 10)

        # atributes for adding people
        id_label = Label(self.bottom_frame, text = 'Id : ', font = 'sans 12 bold', bg  = '#464a49', fg = 'white', pady = 10, )
        id_label.place(x= 10, y = 20, width = 150)
        self.id_entry = Entry(self.bottom_frame, width = 40, textvariable = self.id_var, font = 'sans 12', bd = 3)
        self.id_entry.place(x= 220, y = 20, height = 40)
        #id_entry.insert(0, 'enter id')
        self.id_entry.focus()

        name_label = Label(self.bottom_frame, text = 'Name : ', font = 'sans 12 bold', bg  = '#464a49', fg = 'white', pady = 10 )
        name_label.place(x= 10, y = 80, width = 150)
        self.name_entry = Entry(self.bottom_frame, width = 40, textvariable = self.name_var,font = 'sans 12', bd = 3)
        self.name_entry.place(x= 220, y = 80, height = 40)
        #name_entry.insert(0, 'Enter name')

        email_label = Label(self.bottom_frame, text = 'Email : ', font = 'sans 12 bold', bg  = '#464a49', fg = 'white', pady = 10 )
        email_label.place(x= 10, y = 140, width = 150)
        self.email_entry = Entry(self.bottom_frame, width = 40, textvariable = self.email_var,font = 'sans 12', bd = 3)
        self.email_entry.place(x= 220, y = 140, height = 40)
        #email_entry.insert(0, 'Enter Email')

        contact_label = Label(self.bottom_frame, text = 'Phone No. : ', font = 'sans 12 bold', bg  = '#464a49', fg = 'white', pady = 10 )
        contact_label.place(x= 10, y = 200, width = 150)
        self.contact_entry = Entry(self.bottom_frame, width = 40, textvariable = self.contact_var,font = 'sans 12', bd = 3)
        self.contact_entry.place(x= 220, y = 200, height = 40)
        #contact_entry.insert(0, 'Enter Contact')

        # button to add 
        add_details = Button(self.bottom_frame, text = 'Add Details', width = 12, font = 'arial 15 bold',bg = '#3b2d16', fg = 'white', bd = 5, command = self.db_store)
        add_details.place(x= 370, y = 300)

        back_to_mypeople = Button(self.bottom_frame, text = 'Back', width = 12,font = 'arial 15 bold',bg = '#3b2d16', fg = 'white', bd = 5, command = self.back_myPeople)
        back_to_mypeople.place(x= 100, y = 300)

    def back_myPeople(self):
        self.destroy()