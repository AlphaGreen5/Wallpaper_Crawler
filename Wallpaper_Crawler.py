import requests
from bs4 import BeautifulSoup
import os
import re
import sys
from time import sleep

def rootDirectoryCreator(name):
    newpath = r'C:\\Users\\Alpha Wave\\Desktop\\'+name
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        print('\n New directory named '+str.upper(name)+' was created...')
        return newpath
    else:
        print('New Directory could not be created...')
        return str(0)

def download_web_image(imageUrl,imageName,path):
    if path == '0':
        print('Image could not be downloaded, because there already exists a directory with same name. Try with a different name.')
    else:
        
        fullName = path+'\\'+imageName
        req=requests.get(imageUrl,stream=True)
        req.raise_for_status()
        with open(fullName,'wb') as fd:
            for chunk in req.iter_content(chunk_size=300000):
                print('File Downloading')
                fd.write(chunk)
        print(imageName+' was downloaded')
    
def browse_spider(checkdir,wallpaper_name):
    page = 1
    while page <= 80:
        print('\n\n Getting Page '+str(page)+' contents...')
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
                        download_web_image(url_a,name, checkdir)
                else:
                    download_web_image(url_a,name, checkdir)
        page +=1

def menu():
    print("\n")
    print('\nDo you want to exit or want to go to the menu :')
    ans=input("(Enter exit or menu) :")
    if(ans.lower()=='menu'):
        os.system('cls')
        main()
    elif(ans.lower()=='exit'):
        print('Good Bye')
        sleep(1)
        sys.exit(0)
    else:
        print("You have entered unknown option")
        menu()

def main():
    print('--- Minimal Wallpapers Downloader ---')
    print('\n  ')
    try:
              
        folder = input("Enter the name of the folder you want to create :")
        folderCreationCheck = rootDirectoryCreator(folder)
        print('\n\n ')
        wallpaper_name = input('Enter the Wallpaper you want to search for : ')
        if(folder=='' or wallpaper_name==''):
            print("\n\nYou didn't enter wallpaper name or folder name or both.")
            print("\n\n")
            main()
        browse_spider(folderCreationCheck,wallpaper_name)
        print('\n All the wallpapers were downloaded succesfully.')
    except KeyboardInterrupt:
        menu()
        
            
if __name__=="__main__":
    main()
