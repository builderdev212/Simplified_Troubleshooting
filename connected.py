from urllib.request import urlopen
import webbrowser

def connected():
    try:
        urlopen("http://google.com")
        return True
    except:
        return False

def browse(url):
    webbrowser.open_new(url)
