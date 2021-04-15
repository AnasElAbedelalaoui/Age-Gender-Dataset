import csv
from bs4 import BeautifulSoup
import requests 
import time
import cssutils
import PIL.Image
 
url ="https://birthdaybuddies.net/birthday/11th-april" 

response = requests.get(url)

if response.ok:
    l=[]
    soup=BeautifulSoup(response.text,'lxml')
    ico = soup.findAll("div",{"class":"col-sm-6 col-md-6 col-xl-3"})
    for i in ico : 
        urls=i.find('a')['href']
        l.append(urls)
        

with open('mesurls.txt','w') as file : 
    for link in l :
        file.write(link + '\n')
f=[]
with open('mesurls.txt','r') as inf:
    with open('data123.csv','w') as out: 
        for row in inf:
            url1=row.strip()
            response1=requests.get(url1)
            if response1.ok:
                soup1=BeautifulSoup(response1.text,'lxml')
                n=str(soup1.find('h1'))
                p=n[17:]
                name=p[:-5] 
                ul=soup1.find("ul",{"class":"info-box"})
                strong=ul.find('strong')
                a=strong.find('a')['href']    
                age=a[32:]
                strng=ul.findAll('strong')
                gender=str(strng[2])
                g=gender[8:]
                o=g[:2]
                img=soup1.find("ul",{"class","slides"})
                li=img.find('li')['style']
                style = cssutils.parseStyle(li)
                url2 = style['background-image']
                url2 = url2.replace('url(', '').replace(')', '')
                url3='https://birthdaybuddies.net'+url2
                response = requests.get(url3)
                file = open("monimage.png", "wb")
                file.write(response.content) 
                file.close()
                image=PIL.Image.open("monimage.png")
                details=image._getexif()
                if details is not None:
                    if len(details)>1:
                        date=details[36868]
                        print(date)
                    out.write(name+';'+age+';'+o+';'+url3+';'+date+'\n')


                

            
                
                   
                    
                       
                    
                
                    


        

    
