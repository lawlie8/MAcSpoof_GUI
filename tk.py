import tkinter as tk
import time
import sys
import os
import ctypes
#import windll
ctypes.windll.shcore.SetProcessDpiAwareness(1)
window = tk.Tk() #creates window
window.tk.call('tk', 'scaling', 2.0)
window.geometry("1050x380")
window.configure(bg='#333338')
button = tk.Button(text ="Change",height = 1,width=10,fg="#d6d6c2",bg="blue")
entry  = tk.Entry(width=20)
label = tk.Label(text = "MAcSpoof Mac Address Changer" ,fg="#d6d6c2",bg="#333338")

label.place(relx=.5,rely=.5,anchor="c")




def entry(Addlist):
    #Choose mac address function here
    entry = tk.Entry()
    entry.insert(0,"Insert your option here")
    def clear_entry():
        entry.place_forget()
        entry.destroy()
        entry1 = tk.Entry()
        entry1.pack(anchor='w')
        def change_mac_address(event):
            choice = entry1.get()
            try:
                choice = int(choice)
            except:
                entry1.delete(0,tk.END)
                MessageBox = ctypes.windll.user32.MessageBoxW
                MessageBox(None, 'Wrong Entry Try Again', 'Error', 0)
            if choice <= len(Addlist):
                if choice >= 1:
                    try:
                        choice = int(choice)
                        print(choice)#mac change code must go here beacuse i fucked up the design
                    except:
                        MessageBox = ctypes.windll.user32.MessageBoxW
                        MessageBox(None, 'Wrong Choice', 'Window title', 0)
                        entry1.delete(0,tk.END)
                else:
                    MessageBox = ctypes.windll.user32.MessageBoxW
                    MessageBox(None, 'Wrong Choice', 'Window title', 0)
                    entry1.delete(0,tk.END)
            else:
                entry1.delete(0,tk.END)
                MessageBox = ctypes.windll.user32.MessageBoxW
                MessageBox(None, 'Wrong Choice', 'Window title', 0)
                #insert the thing that to be inserted here

        entry1.bind('<Return>',change_mac_address)
        button_choose = tk.Button(text='Go',height=0,width=12,fg="white",bg="blue",padx=5,command=change_mac_address,master=window)
        button_choose.pack(pady=15,anchor='w')

    entry.pack(anchor='w')
    entry.after(2000,clear_entry)


def adapter_list():
        dl = []
        ml = []
        Adapterlist = []
        Addlist = []
        os.system('ipconfig /all > ip.txt')
        x = open("ip.txt",'r+')
        hu = x.readlines()
        line_numbers = len(hu)
        for i in range(0,line_numbers):
            dev_des = hu[i].find('Description')
            device = hu[i][dev_des:dev_des + 800]
            device = device.strip(':').split('\n')
            #device = device.split('\n')
            device = ''.join(device)
            dl.append(device)
        for r in dl:
            if r != '':
                r = r.split('Description . . . . . . . . . . . : ')
                r = ''.join(r)
                Adapterlist.append(r)
        x = open("ip.txt",'r+')
        hu = x.readlines()
        line_numbers = len(hu)
        for j in range(0,line_numbers):
            dev_des = hu[j].find('Physical Address')
            device = hu[j][dev_des:dev_des + 80]
            device = device.strip(':')
            device = device.split('\n')
            device = ''.join(device)
            ml.append(device)
        for m in ml:
            if m != '':
                m = m.split('Physical Address. . . . . . . . . : ')
                m = ''.join(m)
                #print(r)
                Addlist.append(m)
        label_text = ""
        for i,k,h in zip(range(1,len(Addlist)+1),Addlist,Adapterlist):
            #adapter_label = tk.Label(text=i+k+h)
            #adapter_label.pack()

            i,k,h = str(i),str(k),str(h)
            label_text += i+"  :  "+k+"\t\t"+h+"\n"

        label_text = label_text.strip(" ")
        adapter_label = tk.Label(text = label_text,justify="left",fg='#d6d6c2',bg='#333338')
        adapter_label.pack(anchor='w',side ="left",padx=30)
        x.close()
        os.system('del ip.txt')
        entry(Addlist)


def label3():
    label3 = tk.Label(text="Devices Found :",fg="#f7a483",bg='#333338')
    label3.place(x=10,y=100)
    adapter_list()
def clear_label():
    label.place_forget()
    label2 = tk.Label(text="MAcSpoof Mac Address Changer Allows You to\n Change Your Wifi Adapter's Mac Address",fg='white',bg='#333338')
    label2.pack()
    label2.after(1000,label3)
label.after(3000,clear_label)


window.mainloop()  #main window opens here
