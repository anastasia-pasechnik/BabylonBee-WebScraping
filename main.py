import requests
from bs4 import BeautifulSoup
import PySimpleGUI as sg
from tkinter import Tk, font

# To display list of fonts
root = Tk()
font_tuple = font.families()
root.destroy()

# FONTS
font = "Rockwell, 18"
article_font = "Rockwell, 15"

# code for getting newest article
URL = "https://babylonbee.com/news"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html.parser')
headlines = soup.find_all('article-card')

headlineList = []


for headline in headlines:
    text = str(headline).partition(":title='")[2].partition("'>")[0]
    if (text != ''):
        headlineList.append(text)

refreshed = headlineList[0]
sg.theme('DarkPurple1')   # Theme


# All the stuff inside your window.
layout = [
    [sg.Text('BABYLON BEE LATEST ARTICLE: ', key='-bold-', size=(70,1), font= font, justification='left')],
    [sg.Text(refreshed, font=article_font, size=(90,1), justification="left")],
    [sg.Text('\nEarlier Articles: ', font=font)],
    [sg.Text(headlineList[1], font= article_font, justification='left')],
    [sg.Text(headlineList[2], font= article_font, justification='left')],
    [sg.Text(headlineList[3], font= article_font, justification='left')],
    [sg.Button('Refresh'), sg.Button('Cancel')],
    [sg.Text("Press refresh to check for the updated latest article! ", size=(70,1), font=article_font)],
]


# Create the window
window = sg.Window('Babylon Bee Webscraper', layout , size=(900,400))


# Event Loop to process "events" and get the "values" of the inputs

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        print('You canceled')
        break

    if event == 'Refresh':
        refreshed = headlineList[0]

window.close()