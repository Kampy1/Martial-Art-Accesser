import requests
from bs4 import BeautifulSoup

MA_list = "https://en.wikipedia.org/wiki/List_of_Japanese_martial_arts"

def MartialArts(): 
    # the target we want to open     
    url = MA_list
      
    #open with GET method 
    resp=requests.get(url) 
      
    #http_respone 200 means OK status 
    if resp.status_code == 200: 
        print("Successfully opened the web page") 
        print("Martial Arts :-\n") 
     
        soup = BeautifulSoup(resp.text, 'html.parser')     
  
        # l is the list which contains all the text ie the various arts 
        l = soup.find("ul", {"class" : "class_title"}) 
       
        for i in l.findAll("a"): 
            print(i.text) 
    else: 
        print("Error") 
          
MartialArts()