from tkinter import *

import datetime as dt 
from mypeople import MyPeople
from addpeople import AddPeople

date = dt.datetime.now().date()
date = str(date)
print(date)

class app_display(Tk):

    def __init__(self):
        super(app_display, self).__init__()
        self.title('My PhoneBook')
        self.geometry('650x600+400+200')
        self.resizable(False, False)  # size of window cant be changed
        self.sub_display()

    def show_people(self):
        people = MyPeople()
        people.mainloop()

    def add_people(self):
        add_screen = AddPeople()
        add_screen.mainloop()

    def about(self):
        # top frame 
        self.top_frame = Frame(self, height = 150, bg = 'grey')
        self.top_frame.place(x= 0, y = 0, relwidth = 1)
        
        self.title_label = Label(self.top_frame, text = 'About Us', font = 'arial 25 bold', bg = 'grey', fg = '#05d9fa')
        self.title_label.place(x = 200, y = 60)

        # bottom frame 
        self.bottom_frame = Frame(self, height =400, bg = '#e8a7a2')
        self.bottom_frame.place(x= 0, y = 160, relwidth = 1 )

        id_label = Label(self.bottom_frame, text = 'This is phonebook application'
                                                    '\n Any one can store ther information like'
                                                    '\n username userEmail User Phone Number'
                                                    , font = 'sans 12 bold', bg  = '#e8a7a2', fg = '#031738', pady = 10, )
        id_label.place(x= 130, y = 20, width = 400, height = 300)
        back_to_mypeople = Button(self.bottom_frame, text = 'Back', width = 12,font = 'arial 15 bold',bg = '#10525c', fg = 'white', bd = 5, command = self.back_main)
        back_to_mypeople.place(x= 250, y = 300)

    def back_main(self):
        self.sub_display()


    def sub_display(self):
        # top frame 
        self.top_frame = Frame(self, height = 150, bg = 'grey')
        self.top_frame.place(x= 0, y = 0, relwidth = 1)

        # items in top frame 
        self.icon_photo = PhotoImage(file = '/home/rsthakur/Desktop/radhe_python/mongo_db/mongo_env/src/tk_projects/Phonebook_project/icon/book1.png')
        self.icon_label = Label(self.top_frame, image = self.icon_photo, bg = 'grey')
        self.icon_label.place(x  = 110, y = 40)

        self.title_label = Label(self.top_frame, text = 'Phonebook App', font = 'arial 25 bold', bg = 'grey', fg = '#05d9fa')
        self.title_label.place(x = 200, y = 60)

        self.date_label = Label(self.top_frame, text = "Today's Date : "+date, font = ('arial', 12, 'bold'), bg = 'grey' , fg = 'white' )
        self.date_label.place(x= 420, y = 20)

        # bottom frame 
        self.bottom_frame = Frame(self, height =400, bg = '#e8a7a2')
        self.bottom_frame.place(x= 0, y = 160, relwidth = 1 )

        # items in bottom frame 
        self.show_btn = Button(self.bottom_frame , text = 'My People', width = 20,font = 'time 12 bold', bg = '#10525c', fg = 'white', bd = 5,pady = 10, command = self.show_people)
        self.show_btn.place(x= 200, y = 50)

        self.add_btn = Button(self.bottom_frame , text = 'Add People',width = 20, font = 'time 12 bold', bg = '#10525c', bd = 5, fg = 'white',pady = 10,command = self.add_people)
        self.add_btn.place(x= 200, y = 130)

        self.about_btn = Button(self.bottom_frame , text = 'About us', width = 20,font = 'time 12 bold', bg = '#10525c', bd = 5,pady = 10, fg = 'white', command = self.about)
        self.about_btn.place(x= 200, y = 210)

        self.Exit_btn = Button(self.bottom_frame , text = 'Exit', width = 20,font = 'time 12 bold', bg = '#10525c', bd = 5,pady = 10, fg = 'white', command = self.quit)
        self.Exit_btn.place(x= 200, y = 290)


def main():
    app = app_display()
    app.mainloop()

if __name__ == '__main__' :
    main()