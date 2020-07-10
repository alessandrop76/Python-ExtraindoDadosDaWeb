import requests
import json
from bs4 import BeautifulSoup


"""
res2 = requests.get("https://digitalinnovation.one/blog/")
print(res2)

res = requests.get("https://web.digitalinnovation.one/community/")
res.encoding ='utf-8'

soup = BeautifulSoup(res.text, 'html.parser')

links = soup.find(class_="pagination").find_all('a')

all_pages = []
for link in links:
    page = requests.get(link.get('href'))
    all_pages.append(BeautifulSoup(page.text, 'html.parser'))
    
print(len(all_pages))


all_post = []

for posts in all_pages:
    posts = soup.find_all(class_='post')
    for post in posts:
        info = post.find(class_="post-content")
        title = info.h2.text
        preview = info.p.text
        author = info.find(class_="post-author").text
        time = info.find(class_="post-date")['datetime']
        #img = info.find(class_='wp-post-image')['src'] ---------------não rodou
        all_post.append({
            'title': 'title',
            'preview': 'preview',
            'author' : 'author',
            #'img' : 'img',---------------------não rodou
            'time' : 'time'
        })

print(all_post)
with open('posts.json', 'w') as json_file:
    json.dump(all_post, json_file, ident=4, ensure_ascii=False)

 """
""" 
#site UOL ESPORTES
res = requests.get("https://www.uol.com.br/esporte/")
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')
posts = soup.find_all(class_ ='thumbnail-standard')


all_posts = []
for post in posts:
    assunto = post.span.text
    titulo = post.h2.text
    imagem = post.img['src']
    link = post.a['href']
    all_posts.append({'assunto': assunto, 'titulo': titulo, 'imagem': imagem, 'link': link})



with open('posts.json', 'w') as json_file:
    json.dump(all_posts, json_file, indent=4, ensure_ascii=False)

 """    

#SITE DIGITAL INOVATION ONE

 
res = requests.get("https://web.digitalinnovation.one/track/fullstack-developer-banco-carrefour")
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')
cards = soup.find_all(class_ ='card-header')


all_cards = []
for card in cards:
    cartao = card-header['course-title m-0 p-0']
    title = info_col-md-9['m-0 p-0']

    all_cards.append({'cartao': card-header, 'title': title})



with open('posts.json', 'w') as json_file:
    json.dump(all_cards, json_file, indent=4, ensure_ascii=False)