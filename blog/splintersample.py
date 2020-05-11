from splinter import Browser

url = "https://www.tripadvisor.in/Restaurant_Review-g1078423-d948529-Reviews-Martin_Berasategui-Lasarte_Province_of_Guipuzcoa_Basque_Country.html"

browser = Browser()
browser.visit(url)
review_div = browser.find_by_id('review_750231642')
img_div = review_div.find_by_css('div[class="ui_avatar resp"]').first
itag = img_div.find_by_tag("img").first
print(itag['src'])

name_div = review_div.find_by_css('div[class="info_text pointer_cursor"] div').first
name = name_div.text
print(name)
browser.quit()
