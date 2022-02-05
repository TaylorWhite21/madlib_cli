import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(url):
  citations = 0
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')
  titles = soup.find_all('a')
  for title in titles:
    if title.text == 'citation needed':
      citations+=1
      
  return citations


def get_citations_needed_report(url):
  passages = ''
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')
  titles = soup.find_all('p')
  for title in titles:
    if 'citation needed' in title.text:
      passages += title.text
  passages = passages.replace("'\n '", ' ')
  print(f'passages: {passages}')
  return passages
   
# def get_citations_needed_report(url):
#   passages = ''
#   page = requests.get(url)
#   soup = BeautifulSoup(page.content, 'html.parser')
#   titles = soup.find_all('p')
#   for title in titles:
#     if 'citation needed' in title.text:
#       passages = title.text
#   print(f'passages: {passages}')
#   return passages
  

get_citations_needed_report('https://en.wikipedia.org/wiki/Search_for_extraterrestrial_intelligence')
get_citations_needed_count('https://en.wikipedia.org/wiki/Search_for_extraterrestrial_intelligence')









# anchors = results('a')
# # print(anchors)
# links = [anchor['href'] for anchor in anchors]
# # print(links)

# python_link = links[1]
# # print(python_link)

# new_url = 'https://testing-www.codefellows.org' + python_link
# # print(new_url)

# link_content = requests.get(new_url)
# # print(link_content.content)
# link_soup = BeautifulSoup(link_content.content, 'html.parser')
# # print(link_soup)

# article = link_soup('article')[1]
# # print(article)

# list_items = article.select(' ul li ul li ')
# # print(list_items)

# for li in list_items:
#   print(li.text)
