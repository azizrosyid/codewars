# https://www.codewars.com/kata/5fee4559135609002c1a1841/train/python
import re
db = {}


def clean_url(url):
    regex = "^(?:https?:\\/\\/)?(?:www\\.)?"
    url = re.sub(regex, "", url)
    url = re.sub("[^a-z]+", "", url)
    url = url.replace(".", "")
    return url

def generate_id(url):
    url = clean_url(url) * 10
    gap = len(url) // (len(url) // 5)
    result = ""
    for i,v in enumerate(range(gap+1,len(url),gap)):
        result += url[v]
        if i == 3:
            break
    return result

def url_shortener(long_url):
    global db
    short_url = "short.ly/"+generate_id(long_url)
    db[short_url] = long_url
    return short_url

def url_redirector(short_url):
    return db[short_url]


short_url1 = url_shortener(
    "https://www.codewars.com/kata/5ef9c85dc41b4e000f9a645f")
short_url2 = url_shortener(
    "https://www.codewars.com/kata/5ef9c85dc41b4e000f9a645f")
print(db)
print(short_url1)
print(short_url2)
# "https://www.codewars.com/kata/5ef9c85dc41b4e000f9a645f"
url_redirector(short_url1)
