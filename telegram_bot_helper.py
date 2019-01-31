import json
import requests
from music_bot import get_request
from music_bot import link_cutter


TOKEN = "538355207:AAFyB_4TER5XfH3pKhUFJo2RVtTe4I9w-OE"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates"
    if offset:
        url += "?offset={}".format(offset)
    js = get_json_from_url(url)
    return js


def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return text, chat_id


def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)


def echo_all(updates):
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]

            music_info, link = get_request.get_music_info_and_link(text)
        except Exception as e:
            try:
                send_message("There is no such song", chat)
                return
            except Exception as e:
                print(e)
                return
        try:
            short_link = link_cutter.cut_link(link)
            send_message(music_info+"\n"+short_link, chat)
        except Exception as e:
            print(e)
