from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
from bs4 import BeautifulSoup
import re
import requests
import threading

def download_web_image(imageUrl,imageName,path):
    fullName = path+'\\'+imageName
    req=requests.get(imageUrl,stream=True)
    req.raise_for_status()
    with open(fullName,'wb') as fd:
        for chunk in req.iter_content(chunk_size=300000):
            fd.write(chunk)
        window.label4.config(text='Downloading Wallpapers')
        image_name=imageName+' got downloaded.'
        window.label5.config(text=image_name)
    
    
def browse_spider(folder_Name,wallpaper_name):
    page = 1
    while page <= 80:
        #print('\n\n Getting Page '+str(page)+' contents...')
        url = 'https://alpha.wallhaven.cc/search?q='+wallpaper_name+'&categories=111&purity=100&sorting=relevance&order=desc&page='+str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,'lxml')
        for a in soup.find_all('img'):
            if(a.get('alt')=='loading'):
                url_a=a.get('data-src')
                name=re.sub('https://alpha.wallhaven.cc/wallpapers/thumb/small/th-','',url_a)
                url_a=re.sub('thumb/small/th-','full/wallhaven-',url_a)
                r=requests.get(url_a)
                if r.status_code==404:
                    url_a=re.sub('jpg','png',url_a)
                    rew=requests.get(url_a)
                    if rew.status_code==404:
                        continue
                    else:
                        download_web_image(url_a,name, folder_Name)
                else:
                    download_web_image(url_a,name, folder_Name)
        page +=1


class wall_crawler():
    def __init__(self,alpha):
        alpha.minsize(400,250)
        alpha.resizable(False,False)
        alpha.title('Wallpaper Downloader')

        
        #label

        self.label=ttk.Label(alpha,text='Wallpaper Downloader',foreground='green',font=('arial',13,'bold'))
        self.label.place(x=110,y=2)

        self.label1=ttk.Label(alpha,text='Folder      :',foreground='red',font=('arial',13))
        self.label1.place(x=10,y=40)

        self.label2=ttk.Label(alpha,text='Wallpaper :',foreground='red',font=('arial',13))
        self.label2.place(x=10,y=80)
        self.label3=ttk.Label(alpha,text='Name',foreground='red',font=('arial',13))
        self.label3.place(x=10,y=100)

        self.label4=ttk.Label(alpha,text='',foreground='red',font=('arial',13,'bold'))
        self.label4.place(x=100,y=150)

        self.label5=ttk.Label(alpha,text='',foreground='blue',font=('arial',13,'bold'))
        self.label5.place(x=90,y=200)

        
        

        #Entry
        self.entry=ttk.Entry(alpha,width=30)
        self.entry.place(x=120,y=40)
        
        self.entry1=ttk.Entry(alpha,width=30)
        self.entry1.place(x=120,y=80)
        folder_new=self.entry.get()
        wallpaper_Name=self.entry1.get()
        

        #Buttons
        self.button=ttk.Button(alpha,text='Browse',command=self.filename)
        self.button.place(x=315,y=38)
        self.button1=ttk.Button(alpha,text='Download',command=threader)
        self.button1.place(x=230,y=110)

        

    def filename(self):
        self.file=filedialog.askdirectory()
        self.entry.delete(0,END)
        self.entry.insert(0,self.file)
        

def threader():
    t=threading.Thread(target=start)
    t.daemon=True
    t.start()
    
def start():
    folder_new=window.entry.get()
    wallpaper_Name=window.entry1.get()
    folder_new=str(folder_new)
    wallpaper_Name=str(wallpaper_Name)
    browse_spider(folder_new,wallpaper_Name)
    

def main():
    global window
    root=Tk()
    window=wall_crawler(root)
    root.mainloop()



    
if __name__=="__main__":
    main()
