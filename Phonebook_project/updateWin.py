from tkinter import *
from tkinter import messagebox
from mongoengine import connect 
from databaseConnect import PhonebookData

# connecting to database 
connect(db = 'My_mongo', host = 'mongodb+srv://dbradhe:radhecool@cluster0.dil7k.mongodb.net/My_mongo?retryWrites=true&w=majority')
print('connection established sucessfully!!!!!!')

class Update(Tk):
    
    def __init__(self, data_id):
        super(Update, self).__init__()
        self.geometry('650x600+400+200')
        self.resizable(False,False)
        self.title('Update Contact')
        self.person_id = data_id
        self.Updatewindow_view()

    def Updatewindow_view(self):

        # top frame 
        self.top_frame = Frame(self, height = 150, bg = 'grey')
        self.top_frame.pack(fill = X)

        title_label = Label(self.top_frame, text = 'Update Information', font = 'arial 25 bold', bg = 'grey', fg = '#05d9fa')
        title_label.place(x = 200, y = 60)

        # bottom frame 
        self.bottom_frame = Frame(self, height =400, bg = '#e8a7a2')
        self.bottom_frame.pack(fill = X, pady = 10)

        # collecting specified data 
        print('collecting current data')
        current_data = PhonebookData.objects(user_id = self.person_id).get()
        c_name = current_data.user_name
        c_email = current_data.user_email
        c_contact = current_data.user_contact 

        # atributes for adding people
        id_label = Label(self.bottom_frame, text = 'Id : ', font = 'sans 12 bold', bg  = '#464a49', fg = 'white', pady = 10, )
        id_label.place(x= 10, y = 20, width = 150)
        self.id_entry = Entry(self.bottom_frame, width = 40, font = 'sans 12', bd = 3)
        self.id_entry.place(x= 220, y = 20, height = 40)
        self.id_entry.insert(0, self.person_id)
        self.id_entry.focus()

        name_label = Label(self.bottom_frame, text = 'Name : ', font = 'sans 12 bold', bg  = '#464a49', fg = 'white', pady = 10 )
        name_label.place(x= 10, y = 80, width = 150)
        self.name_entry = Entry(self.bottom_frame, width = 40,font = 'sans 12', bd = 3)
        self.name_entry.place(x= 220, y = 80, height = 40)
        self.name_entry.insert(0, c_name)

        email_label = Label(self.bottom_frame, text = 'Email : ', font = 'sans 12 bold', bg  = '#464a49', fg = 'white', pady = 10 )
        email_label.place(x= 10, y = 140, width = 150)
        self.email_entry = Entry(self.bottom_frame, width = 40, font = 'sans 12', bd = 3)
        self.email_entry.place(x= 220, y = 140, height = 40)
        self.email_entry.insert(0,  c_email)

        contact_label = Label(self.bottom_frame, text = 'Phone No. : ', font = 'sans 12 bold', bg  = '#464a49', fg = 'white', pady = 10 )
        contact_label.place(x= 10, y = 200, width = 150)
        self.contact_entry = Entry(self.bottom_frame, width = 40,font = 'sans 12', bd = 3)
        self.contact_entry.place(x= 220, y = 200, height = 40)
        self.contact_entry.insert(0, c_contact)

        # button to add 
        add_details = Button(self.bottom_frame, text = 'Update Details', font = 'arial 20 bold',bg = '#3b2d16', fg = 'white', bd = 5, command = self.update_data)
        add_details.place(x= 250, y = 300)

    def update_data(self):
        try:
            found_data = PhonebookData.objects(user_id = self.person_id).get()
            found_data.update(
                user_id = self.id_entry.get(),
                user_name = self.name_entry.get(),
                user_email = self.email_entry.get(),
                user_contact = self.contact_entry.get()
            )
            self.destroy()

        except DoesNotExist:
            messagebox.showerror('Exixtance Error', 'The data searched is not found in data base......')