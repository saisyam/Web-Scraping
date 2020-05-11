from bs4 import BeautifulSoup
import requests

url = "https://www.tripadvisor.in/Restaurant_Review-g1078423-d948529-Reviews-Martin_Berasategui-Lasarte_Province_of_Guipuzcoa_Basque_Country.html"

response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
avatar_div = soup.find("div",{'class':'avatarWrapper'})
img_tag = avatar_div.find("img", {'class':'basicImg'})
img_url = img_tag.attrs['src']
print(img_url)

name_div = soup.find("div",{'class':'info_text pointer_cursor'})
name = name_div.find("div").text
print(name)

