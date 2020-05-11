from bs4 import BeautifulSoup

html = '''
<div class="member_info">
   <div id="UID_17C6B346E55C632F36B9F164F28E2211-SRC_750231642" class="memberOverlayLink clickable" onclick="widgetEvCall('handlers.initMemberOverlay', event, this);" data-anchorwidth="90">
      <div class="avatar profile_17C6B346E55C632F36B9F164F28E2211">
         <div class="avatarWrapper">
            <a>
               <div class="prw_rup prw_common_basic_image avatarImage" data-prwidget-name="common_basic_image" data-prwidget-init="">
                  <div class="ui_avatar resp"> <img src="https://media-cdn.tripadvisor.com/media/photo-l/1a/f6/7c/01/default-avatar-2020-5.jpg" class="basicImg" data-mediaid="452361217"></div>
               </div>
            </a>
         </div>
      </div>
      <div class="info_text pointer_cursor" onclick="widgetEvCall('handlers.usernameClick', event, this);">
         <div>bornaz2018</div>
      </div>
   </div>
   <div id="UID_17C6B346E55C632F36B9F164F28E2211-SRC_750231642" class="memberOverlayLink clickable" onclick="widgetEvCall('handlers.initMemberOverlay', event, this);" data-anchorwidth="90">
      <div class="memberBadging g10n is-shown-at-tablet">
         <div class="reviewerBadge badge"><span class="badgeText">1 review</span></div>
      </div>
   </div>
</div>
'''

soup = BeautifulSoup(html, "lxml")
avatar_div = soup.find("div",{'class':'avatarWrapper'})
img_tag = avatar_div.find("img", {'class':'basicImg'})
img_url = img_tag.attrs['src']
print(img_url)

name_div = soup.find("div",{'class':'info_text pointer_cursor'})
name = name_div.find("div").text
print(name)

