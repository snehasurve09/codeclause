import pyshorteners
#user input
url=input("Enter the URL: ")
def shortenurl(url):
    s=pyshorteners.Shortener()
    print("Shortener URL: ",(s.tinyurl.short(url)))
shortenurl(url)