import requests
from bs4 import BeautifulSoup
import sys
import random

#Added for testing
import time

MA_list = "https://en.wikipedia.org/wiki/List_of_Japanese_martial_arts"

#Function to pull the list of Martial Arts
def MartialArtsList(Arts_count): 
    url = MA_list
    count = 0

    Ordered_MA_list = []

    resp = requests.get(url) 

    if resp.status_code == 200: 
        print("Successfully opened the web page") 

        #Parses the HTML for Python
        soup = BeautifulSoup(resp.text, 'html.parser')

        Arts_list = soup.select('div.div-col > ul > li')

        for arts in Arts_list:
            count += 1
        print(f"{count} Martial Arts found:\n")

        for arts in Arts_list:
            arts.text
            Ordered_MA_list.append(arts.text)
            
            if Arts_count == 0:
                print(arts.text)

        if Arts_count > 0:
            chosen_arts = random.sample(Ordered_MA_list, k = Arts_count)
            for art in chosen_arts:
                print(art)
        elif Arts_count == 0:
            pass
        else:
            sys.exit("Error in retrieval. Abberant number entered. Please try again.")

    else: 
        print("Error") 

def MA_data(option):

    result_list = []

    url = f"https://en.wikipedia.org/wiki/{option}"

    resp = requests.get(url) 

    if resp.status_code == 200: 
        print("Successfully opened the web page") 

        soup = BeautifulSoup(resp.text, 'html.parser')

        Details_list = soup.select('div.div-col > ul > li')

        for info in Details_list:
            print(info.text)

#NEXT STEP!! Pulling information on Arts

print("How many entities would you like to see? Enter '0' for all entries")
count = int(input())

MartialArtsList(count)

print("What Martial Art would you like to learn about?")
Martial_Art = str(input())

result = MA_data(Martial_Art)

if result:
    for art in result:
        print(f"What would you like to learn about {Martial_Art}?")
else:
    print("Unable to download data")
