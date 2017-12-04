import requests
from bs4 import BeautifulSoup
import os
import re

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
        imageName+='.png'
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
        url = 'https://wall.alphacoders.com/search.php?search='+wallpaper_name+'&page='+str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,'lxml')
        for a in soup.find_all('img'):
            if(a.get('alt')):
                url_a=a.get('src')
                url_a=re.sub('thumb-[0-9]+-','',url_a)
                name=a.get('alt')[29:]
                download_web_image(url_a,name, checkdir)
        page +=1


print('--- Minimal Wallpapers Downloader ---')
print('\n  ')
folder = input("Enter the name of the folder you want to create :")
folderCreationCheck = rootDirectoryCreator(folder)
print('\n\n ')
wallpaper_name = input('Enter the Wallpaper you want to search for : ')

browse_spider(folderCreationCheck,wallpaper_name)
print('\n All the wallpapers were downloaded succesfully.')




