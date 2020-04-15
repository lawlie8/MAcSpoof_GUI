import subprocess
import ctypes, sys
import re
import tkinter as tk
import time
import sys
import os
import ctypes
import random
from tkinter import *
from tkinter.ttk import *
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    #ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    window = tk.Tk() #creates window
    window.tk.call('tk', 'scaling', 2.0)
    window.geometry("1050x380")
    window.resizable(width=False,height=False)
    window.title("MAcSpoof")
    #window.iconbitmap('m.ico')
    window.configure(bg='#333338')
    button = tk.Button(text ="Change",height = 1,width=10,fg="#d6d6c2",bg="blue")
    entry  = tk.Entry(width=20)
    label = tk.Label(text = "MAcSpoof Mac Address Changer" ,fg="#d6d6c2",bg="#333338")
    label.place(relx=.5,rely=.5,anchor="c")
    def entry(Addlist,Adapterlist,adapter_label):
        #Choose mac address function here
        entry = tk.Entry()
        entry.insert(0," Insert your option here")
        def clear_entry():
            entry.place_forget()
            entry.destroy()
            entry1 = tk.Entry()
            entry1.pack(anchor='w')
            entry1.focus()
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
                        choice = int(choice)
                        #print(choice)#mac change code must go here beacuse i fucked up the design
                        progress = Progressbar(window,orient=HORIZONTAL,length=1010,mode='determinate')
                        progress.place(anchor='w',x=20,y=350)
                        #asd = input()
                        progress['value'] = 10
                        window.update_idletasks()
                        random_mac = "02"
                        list = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
                        for i in range(0,10):
                            x = random.choice(list)
                            random_mac = random_mac + x
                        progress['value'] = 15
                        window.update_idletasks()
                        list = [
                        r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0000' -Name NetworkAddress",
                        r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0001' -Name NetworkAddress",
                        r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0002' -Name NetworkAddress",
                        r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0003' -Name NetworkAddress",
                        r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0004' -Name NetworkAddress",
                        r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0005' -Name NetworkAddress",
                        r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0006' -Name NetworkAddress",
                        r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0007' -Name NetworkAddress",
                        r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0008' -Name NetworkAddress",
                        r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0009' -Name NetworkAddress",
                        r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0010' -Name NetworkAddress",
                        r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0011' -Name NetworkAddress",
                        r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0012' -Name NetworkAddress",
                        r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0013' -Name NetworkAddress",
                        r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0014' -Name NetworkAddress",
                        r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0015' -Name NetworkAddress",
                        r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0016' -Name NetworkAddress",
                        r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0017' -Name NetworkAddress",
                        r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0018' -Name NetworkAddress",
                        r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0019' -Name NetworkAddress",
                        r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0020' -Name NetworkAddress",
                        r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0021' -Name NetworkAddress",
                        r"powershell Get-ItemPropertyValue -Path 'HKLM:\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0022' -Name NetworkAddress",
                        ]
                        i2 = Addlist[choice - 1].split('-')
                        cscs = Addlist[choice -1]
                        i2 = ''.join(i2)
                        time.sleep(0.5)
                        progress['value'] = 50
                        window.update_idletasks()
                        for i in list:
                            #works here
                            driver_description = i.replace('NetworkAddress','DriverDesc')
                            j = i.replace('NetworkAddress','OriginalNetworkAddress')
                            if os.popen(driver_description).read().split('\n')[0] == Adapterlist[choice - 1]:  #os popen probably gives output in windowed mode check here
                                #does not work here if loop problem
                                cou = os.popen(i).read().split('\n')
                                cou = str(''.join(cou))
                                cou = cou.split('-')
                                cou = str(''.join(cou))
                                if cou.lower() == i2.lower():
                                    set_value = i.replace('Get-ItemPropertyValue','Set-ItemProperty')
                                    try:
                                        os.system(set_value + " -Value " + random_mac + '> deb.txt')
                                    except:
                                        #print('cant change value')
                                        time.sleep(5)
                                        exit()
                                try:
                                    registry_value = os.popen(i).read().split('\n')[0] #test
                                    #print('registry_value = {}'.format(registry_value[33:62]))#test
                                    if registry_value[33:62] == 'NetworkAddress does not exist':
                                        new_item_entry = i.replace('Get-ItemPropertyValue','New-ItemProperty')
                                        os.system(new_item_entry + " -Value "+ random_mac + " -PropertyType 'String' > deb.txt")
                                        #print('Address Changed Restarting Devices')
                                        break
                                    else:
                                        os.system(set_value + " -Value " + random_mac + '> deb.txt')
                                except:
                                    #print('no works on 139')
                                    jlsdfsdf = 10
                        #use else conditioin if possible
                        #also possible admin rights problem
                        progress['value'] = 70
                        window.update_idletasks()
                        try:
                            os.system('powershell netsh interface set interface name="Wi-Fi" admin=disabled > deb.txt')
                            os.system('powershell netsh interface set interface name="Wi-Fi" admin=enabled > deb.txt')
                            os.system('powershell netsh interface set interface name="tap" admin=disabled > deb.txt')
                            os.system('powershell netsh interface set interface name="tap" admin=enabled > deb.txt')
                            os.system('powershell netsh interface set interface name="Ethernet" admin=disabled > deb.txt')
                            os.system('powershell netsh interface set interface name="Ethernet" admin=enabled > deb.txt')
                        except:
                            #print('Problem at restarting device do it manually\n')
                            #print("Press any key to Continue\n")
                            #lahaghakjgh = input()
                            exit()
                        progress['value'] = 100
                        window.update_idletasks()
                        MessageBox = ctypes.windll.user32.MessageBoxW
                        MessageBox(None, 'Mac Address Changed to '+ random_mac, 'Window title', 0)
                        entry1.delete(0,tk.END)
                        adapter_label.place_forget()
                        adapter_label.destroy()
                        entry1.place_forget()
                        entry1.destroy()
                        button_choose.place_forget()
                        button_choose.destroy()
                        progress.place_forget()
                        progress.destroy()
                        adapter_list()
                        '''***** ENDS HERE *****'''
                        #window.destroy()
                        '''***** ENDS HERE *****'''
                    else:
                        MessageBox = ctypes.windll.user32.MessageBoxW
                        MessageBox(None, 'Wrong Choice', 'Window title', 0)
                        entry1.delete(0,tk.END)
                        #print('134')
                else:
                    entry1.delete(0,tk.END)
                    MessageBox = ctypes.windll.user32.MessageBoxW
                    MessageBox(None, 'Wrong Choice', 'Window title', 0)
                    #print('140')
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
                i,k,h = str(i),str(k),str(h)
                label_text += i+"  :  "+k+"\t\t"+h+"\n"
            label_text = label_text.strip(" ")
            adapter_label = tk.Label(text = label_text,justify="left",fg='#d6d6c2',bg='#333338')
            adapter_label.pack(anchor='w',side ="left",padx=30)
            x.close()
            os.system('del ip.txt')
            entry(Addlist,Adapterlist,adapter_label)
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
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
try:
    window.mainloop()  #main window opens here
except:
    tomato = 'potato'
is_admin()
