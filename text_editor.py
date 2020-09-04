"""
this is a text  Editor app in which  we can create new file or open any file , add text to it and save it.
"""

# import area
from tkinter import *
from tkinter import filedialog

# class Definition for  text Editior 

class text_editor(Tk):

    current_open_file = 'no_file'

    def __init__(self):
        super(text_editor, self).__init__()
        self.title('My Text Editor')
        self.geometry('800x600+300+100')
        self.text_screen()
        self.menu_creator()

    def new_file(self):
        self.text_area.delete(1.0,END)
        self.current_open_file = 'no_file'

    def open_file(self):
        file_return = filedialog.askopenfile(initialdir = '/home/rsthakur', title = 'select file to open', 
                      filetypes = (('text files', '*.txt'), ('All files', '*.*')) )
        #adding file item to  text area
        if file_return != None :
            self.text_area.delete(1.0, END)
            for line in file_return:
                self.text_area.insert(END, line)
            self.current_open_file = file_return.name
        file_return.close()

    def save_as_file(self):
        f = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt')
        if f is None :
            return
        file_data = self.text_area.get(1.0, END)
        self.current_open_file = f.name
        f.write(file_data)
        f.close()

    def save_file(self):
        if self.current_open_file == 'no_file':
            self.save_as_file()
        else:
            f = open(self.current_open_file, 'w+')
            f.write(self.text_area.get(1.0, END))
            f.close()

    def cut_text(self):
        self.copy_text()
        self.text_area.delete('sel.first', 'sel.last')

    def copy_text(self):
        self.text_area.clipboard_clear()
        self.text_area.clipboard_append(self.text_area.selection_get())

    def paste_text(self):
        self.text_area.insert(INSERT, self.text_area.clipboard_get())

    def text_screen(self):
        self.text_area = Text(self, undo = True,font = ('', 15))
        self.text_area.place(relx= 0.0, rely = 0.0, relwidth = 1, relheight = 1)
        self.text_area.focus()

    def menu_creator(self):

        #crating menu bar 
        menu_bar = Menu(self)
        self.config(menu = menu_bar)

        # changing style of menu 
        menu_bar.config(bg = '#d8f0da', fg = '#171a17')

        ## adding menues to menu bar
        #file menu
        file_menu = Menu(menu_bar, tearoff = 0)
        menu_bar.add_cascade(label = 'File', menu = file_menu)
        # edit menu 
        edite_menu = Menu(menu_bar, tearoff = 0)
        menu_bar.add_cascade(label = 'Edit', menu = edite_menu) 
        # search menu 
        search_menu = Menu(menu_bar, tearoff = 0)
        menu_bar.add_cascade(label = 'Search', menu = search_menu) 
        # option menu 
        option_menu = Menu(menu_bar, tearoff = 0)
        menu_bar.add_cascade(label = 'Options', menu = option_menu) 
        # help menu 
        help_menu = Menu(menu_bar, tearoff = 0)
        menu_bar.add_cascade(label = 'Help', menu = help_menu) 

        # adding items in file menu 
        file_menu.add_command(label = 'New',command = self.new_file)
        file_menu.add_command(label = 'open', command = self.open_file)
        file_menu.add_command(label = 'Save', command = self.save_file)
        file_menu.add_command(label = 'Save as', command = self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label = 'Print Preview')
        file_menu.add_command(label = 'Print...')
        file_menu.add_separator()
        file_menu.add_command(label = 'Quit', command = self.quit)

        # items in Edit menu
        edite_menu.add_command(label = 'Undo', command = self.text_area.edit_undo)
        edite_menu.add_command(label = 'Redo', command = self.text_area.edit_redo)
        edite_menu.add_separator()
        edite_menu.add_command(label = 'Cut', command = self.cut_text)
        edite_menu.add_command(label = 'Copy', command = self.copy_text)
        edite_menu.add_command(label = 'Paste', command = self.paste_text)
        edite_menu.add_command(label = 'Delete')
        edite_menu.add_separator()
        edite_menu.add_command(label = 'Select All')

        #items in search menu 
        search_menu.add_command(label = 'Find...')
        search_menu.add_command(label = 'Find Next')
        search_menu.add_command(label = 'Find Previous')
        search_menu.add_command(label = 'Replace...')
        search_menu.add_separator()
        search_menu.add_command(label = 'Jump To...')

        # items in option menu 
        option_menu.add_command(label = 'Font...')
        option_menu.add_command(label = 'Word Wrap')
        option_menu.add_command(label = 'Line Number')
        option_menu.add_separator()
        option_menu.add_command(label = 'Auto Indent')

        # item in help menu 
        help_menu.add_command(label = 'About')



screen = text_editor()
screen.mainloop()