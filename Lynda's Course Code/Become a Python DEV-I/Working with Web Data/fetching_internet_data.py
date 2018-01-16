import urllib.request


def main():
    # open a connection to a URL using urllib request
    webUrl = urllib.request.urlopen('http://joemarini.com')

    # get the result code and print it
    print(str(webUrl.getcode()))

    # read the data from the URL and print it
    data = webUrl.read()
    print(data)



main()