import urllib.parse
import urllib.request
import re
import json


template_search_link = "http://zaycev.net/search.html?"
template_json_link = "http://zaycev.net/"


def get_music_info_and_link(request_text):
    query_parameter = urllib.parse.urlencode({"query_search": request_text})

    with urllib.request.urlopen(template_search_link + query_parameter) as response:
        html = response.read().decode('utf-8')

    link_json = re.search("/musicset/play/.+\.json", html)

    with urllib.request.urlopen(template_json_link + link_json[0]) as response:
        link = json.loads(response.read().decode('utf-8'))["url"]
    
    an_artist_element = re.search("<a target=\"_blank\" class=\"musicset-track__link\" href=\"/artist/.+?\">.+?</a>", html)[0]
    an_artist = re.search("(?<=>).*(?=<)",an_artist_element)[0]
    track_name_element = re.search("<a href=\"/pages/.+?>.*?</a>", html)[0]
    track_name = re.search("(?<=>).*(?=<)",track_name_element)[0]
    
    music_info = "Artist: "+an_artist+"\n"+"Track: "+track_name;
    
    return music_info, link
