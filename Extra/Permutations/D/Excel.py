#!/usr/bin/env python
# coding: utf-8

# In[1]:


def extraction(minimumMatches, numberOfSessions, outputFileName):
    import pandas as pd
    import numpy as np
    import glob, os
    import openpyxl

    #Settings
    psi = pd.read_excel('Input Merged File.xlsx')
    df = psi.to_numpy()
    row = ['Number',1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
           'a0', 'a00']
    df = np.insert(df, 0, row, 0)
    num_rows, num_cols = df.shape
    path = "PermutationFiles/"
    permLists = []

    #Variables
    #minimumMatches = int(input("Enter Minimum Number Of Matches e.g. '10': "))
    #numberOfSessions = int(input("Enter Number of Sessions e.g. '4': "))
    #outputFileName = input("Enter the name of your output file e.g 'Output': ")
    minimumMatches = int(minimumMatches)
    numberOfSessions = int(numberOfSessions)
    file = str(numberOfSessions) + " of 17 Permutations.txt"

    #Program Core
    f = open(path + file,'r')
    for i in f.readlines():
        i = i.rstrip()
        i = i.split(',')
        permLists.append(i)
        row = ['Number of Sessions Match', 'Specific Sessions', 'Number Hit 1', 'Number Hit 2', '']
    outExcel = [row]
    for p in permLists:
        outputList = []
        totalMatches = 0
        p = set(p)
        for i in range(0,num_rows):
            for j in range(1,num_cols):
                if str(df[i][j]) == 'nan':
                    continue
                cellSet = str(df[i][j]).split(',')
                cellSet = set(cellSet)
                if(p.issubset(cellSet)):
                    totalMatches += 1
                    x = (str(df[0][j]) + " " + str(df[i][0]))
                    outputList.append(x)
        if totalMatches < minimumMatches:
            continue
        else:
            numberSession = len(p)
            session = list(p)
            session = list(map(int,session))
            session.sort()
            session = str(session)
            session = session.replace("[","")
            session = session.replace("]","")
            hit1 = outputList[0].split()[0]
            hit2 = outputList[0].split()[1]
            row = [numberSession, session, hit1, hit2, str(totalMatches) + " hits"]
            outExcel.append(row)
            length = len(outputList)
            for o in range(1,length):
                splitCell = outputList[o].split()
                hit1 = splitCell[0]
                hit2 = splitCell[1] 
                row = ['', session, hit1, hit2, '']
                outExcel.append(row)
        row = ['', '', '', '', '']
        outExcel.append(row) 

    #Output    
    df = pd.DataFrame(outExcel)
    df.to_excel(outputFileName + '.xlsx', index=False, header=False)


# In[2]:


import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Extract your File')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Type Minimum Matches:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 80, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 100, window=entry1)

label3 = tk.Label(root, text='Type Number Of Sessions:')
label3.config(font=('helvetica', 10))
canvas1.create_window(200, 140, window=label3)

entry2 = tk.Entry (root) 
canvas1.create_window(200, 160, window=entry2)

label4 = tk.Label(root, text='Type Output File Name:')
label4.config(font=('helvetica', 10))
canvas1.create_window(200, 200, window=label4)

entry3 = tk.Entry (root) 
canvas1.create_window(200, 220, window=entry3)

def getExtraction():
    x1 = entry1.get()
    x2 = entry2.get()
    x3 = entry3.get()
    extraction(x1,x2,x3)
    
button1 = tk.Button(text='Get the Extracted XLSX', command=getExtraction, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 260, window=button1)

root.mainloop()

