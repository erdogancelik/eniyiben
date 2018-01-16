import urllib.request
import json

def printResult(data):

    theJSON = json.loads(data)

    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])

def main():

    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    webUrl = urllib.request.urlopen(urlData)
    print(webUrl.getcode())

    if webUrl.getcode() == 200:
        data = webUrl.read()

        printResult(data)



main()