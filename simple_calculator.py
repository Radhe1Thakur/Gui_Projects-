#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 07:57:54 2020

@author: rsthakur
"""
from tkinter import *
import tkinter as tk 

# variable declaration 


def btn_click(number):
    current = Entary_label.get()
    Entary_label.delete(0,END)
    Entary_label.insert(0,str(current)+ str(number))
    
def btn_clear():
    Entary_label.delete(0,END)
    
def add_click():
    first_num = Entary_label.get()
    global f_num 
    global math 
    math = "addition"
    f_num = eval(first_num)
    Entary_label.delete(0, END)
     
def mul_click():
    first_num = Entary_label.get()
    global f_num 
    global math 
    math = "multiplication"
    f_num = eval(first_num)
    Entary_label.delete(0, END)

def sub_click():
    first_num = Entary_label.get()
    global f_num 
    global math 
    math = "subtraction"
    f_num = eval(first_num)
    Entary_label.delete(0, END)

def div_click():
    first_num = Entary_label.get()
    global f_num 
    global math 
    math = "division"
    f_num = eval(first_num)
    Entary_label.delete(0, END)
    
def equal_click():
    s_num = Entary_label.get()
    Entary_label.delete(0, END)
    if math == 'addition':
        Entary_label.insert(0, f_num+ eval(s_num))
    elif math == 'subtraction':
        Entary_label.insert(0, f_num - eval(s_num))
    elif math == 'multiplication':
        Entary_label.insert(0, f_num * eval(s_num))
    elif math == 'division':
        Entary_label.insert(0, f_num / eval(s_num))
   
    
    
    
root = tk.Tk()
root.title("Simple Calculator")

num_var  = tk.StringVar()

# Entry for Calculator
Entary_label = tk.Entry(root,width = 50, bd = 5, textvariable = num_var )
Entary_label.grid(row = 0, column = 0, columnspan = 3, padx = 5, pady = 5)
#Entary_label.insert(0,"number")

# buttons in calculator 
btn_1 = tk.Button(root, text = "1", pady = 10, padx = 50,bd = 3,bg = "#81a9eb"
                  ,command = lambda :btn_click(1) ).grid(row = 1, column = 0) 
btn_2 = tk.Button(root, text = "2", pady = 10, padx = 50,bd = 3,bg = "#81a9eb"
                  ,command = lambda :btn_click(2)).grid(row = 1, column = 1) 
btn_3 = tk.Button(root, text = "3", pady = 10, padx = 50,bd = 3,bg = "#81a9eb"
                  ,command = lambda :btn_click(3)).grid(row = 1, column = 2) 
btn_4 = tk.Button(root, text = "4", pady = 10, padx = 50,bd = 3,bg = "#81a9eb"
                  ,command = lambda :btn_click(4)).grid(row = 2, column = 0) 
btn_5 = tk.Button(root, text = "5", pady = 10, padx = 50,bd = 3,bg = "#81a9eb"
                  ,command = lambda :btn_click(5)).grid(row = 2, column = 1) 
btn_6 = tk.Button(root, text = "6", pady = 10, padx = 50,bd = 3,bg = "#81a9eb"
                  ,command = lambda :btn_click(6)).grid(row = 2, column = 2) 
btn_7 = tk.Button(root, text = "7", pady = 10, padx = 50,bd = 3,bg = "#81a9eb"
                  ,command = lambda :btn_click(7)).grid(row = 3, column = 0) 
btn_8 = tk.Button(root, text = "8", pady = 10, padx = 50,bd = 3,bg = "#81a9eb"
                  ,command = lambda :btn_click(8)).grid(row = 3, column = 1) 
btn_9 = tk.Button(root, text = "9", pady = 10, padx = 50,bd = 3,bg = "#81a9eb"
                  ,command = lambda :btn_click(9)).grid(row = 3, column = 2) 
btn_clear = tk.Button(root, text = "clear", pady = 10, padx = 40,bd = 3, bg = "#eb6250"
                      ,command = btn_clear).grid(row = 6, column = 0,) 
btn_0 = tk.Button(root, text = "0", pady = 10, padx = 50,bd = 3,bg = "#81a9eb"
                  ,command = lambda :btn_click(0)).grid(row = 4, column = 0)
btn_decimal = tk.Button(root, text = ".", pady = 10, padx = 50,bd = 3,bg = "#ebe15e"
                  ,command = lambda :btn_click('.')).grid(row = 5, column = 0)  
btn_div = tk.Button(root, text = "%", pady = 10, padx = 47,bd = 3, bg = "#c5e8d4"
                    ,command = div_click).grid(row = 5, column = 2)
btn_add = tk.Button(root, text = "+", pady = 10, padx = 50,bd = 3, bg = "#c5e8d4"
                    ,command = add_click).grid(row = 4, column = 1) 
btn_sub = tk.Button(root, text = "-", pady = 10, padx = 51,bd = 3, bg = "#c5e8d4"
                    ,command = sub_click).grid(row = 4, column = 2) 
btn_mul = tk.Button(root, text = "x", pady = 10, padx = 50,bd = 3, bg = "#c5e8d4"
                    ,command = mul_click).grid(row = 5, column = 1)
btn_equal = tk.Button(root, text = "=", pady = 10, padx = 112,bd = 3,bg = "#46eb57"
                      , command = equal_click).grid(row = 6, column = 1,columnspan = 2)  

root.mainloop()