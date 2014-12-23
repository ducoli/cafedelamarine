#coding: utf-8

from bs4 import BeautifulSoup
import requests
import re
import webbrowser
import clipboard



website = "http://www.tebeotv.fr/emission/le-cafe-de-la-marine-du-telegramme.html"

def find_player(url):
	page = requests.get(url)
	soup = BeautifulSoup(page.text)
	return unicode(soup.find(text=re.compile("url_video")))
	
def identify_url(adr):

    offset_u = len('url_video = ')+1
    
    debut_u = adr.find("url_video")
    
    fin_u = adr.find(";",debut_u)-1
    
    adr = adr[debut_u + offset_u:fin_u]
    
    return adr

def identify_tit(strg):
	
    offset_t=len('titre = ')+5
    debut_t =strg.find('titre')
    fin_t= strg.find(';',debut_t)	-6
    
    titre = strg[debut_t + offset_t:fin_t]
    titre = titre.replace(u'\xe9','e')
    titre =titre.replace('-','').replace(' ', '')
    return titre

def build_action(a_url, a_title):
    return  'x-icabmobile://x-callback-url/download?url=' + a_url + '&filename=' + a_title
    
if __name__ == '__main__':
    
    #source = clipboard.get()
    source = website
    player = find_player(source)
    adresse = identify_url(player)
    titre= identify_tit(player)
    #clipboard.set(adresse)
    
    action = build_action(adresse,titre)
    
    webbrowser.open(build_action(adresse,titre))
    
    print('Done!')
