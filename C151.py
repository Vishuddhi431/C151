#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 07:43:42 2023

@author: vishuddhimakeshwaran
"""
from tkinter import *
root = Tk() 
root.geometry("400x500")
root.title("Profits Calculator")

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
profits = (2, 4.5, 1, 0.5, 6, 8, 4, 5.5, 9, 5.5, 3, 2)

maxProfit = max(profits)
print(maxProfit)
indexMax = profits.index(maxProfit)
print(indexMax)
print("The max profit of " + str(maxProfit) + " million occured in the month of " + str(months[indexMax]))


minProfit = min(profits)
print(minProfit)
indexMin = profits.index(minProfit)
print(indexMin)
print("The min profit of " + str(minProfit) + " million occured in the month of " + str(months[indexMin]))

labelMax = Label(root)
labelMax["text"] = "The max profit of " + str(maxProfit) + " million occured in the month of " + str(months[indexMax])
labelMax.place(relx = 0.5, rely = 0.4, anchor = CENTER)

labelMin = Label(root)
labelMin["text"] = "The min profit of " + str(minProfit) + " million occured in the month of " + str(months[indexMin])
labelMin.place(relx = 0.5, rely = 0.6, anchor = CENTER)

root.mainloop()