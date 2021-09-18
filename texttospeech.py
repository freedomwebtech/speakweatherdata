import requests
from bs4 import BeautifulSoup
from gtts import gTTS
import os




def speak(a):
    tts = gTTS(text=a, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")
    

    


    

city = "Mumbai"


url = "https://www.google.com/search?q="+"weather"+city
html = requests.get(url).content


soup = BeautifulSoup(html, 'html.parser')
temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text


data = str.split('\n')
time = data[0]
sky = data[1]


listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
strd = listdiv[5].text





print("Temperature is", temp)
print("Time: ", time)
print("Sky Description: ", sky)


speak("Temperature is"+temp)
speak("Time:"+time)
speak("Sky Description: "+sky)




