import urllib.request


URL = 'https://clck.ru/--?url='


def cut_link(link):
    with urllib.request.urlopen(URL + link) as response:
        cutted_link = response.read().decode('utf-8')
    return cutted_link
