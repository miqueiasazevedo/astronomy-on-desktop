from ntpath import join
import os
from sys import platform
import requests
from bs4 import BeautifulSoup
import urllib.request

import subprocess
import shlex

SCRIPT = """
/usr/bin/osascript<<END
tell application "System Events" to set picture of every desktop to ("$PICTURE_DIR" as POSIX file as alias)
END"""


class AstronomyOnDesktop:

    def __init__(self, savePath='./', fileName='astronomy.jpg', siteUrl='https://apod.nasa.gov/apod/'):
        self.savePath = savePath
        self.fileName = fileName
        self.siteUrl = siteUrl

    def _getElement(self):
        site = urllib.request.urlopen(self.siteUrl).read()
        soup_HTML = BeautifulSoup(site, features="html.parser")
        imageElement = soup_HTML.find("img")
        return imageElement

    def _getUrlImage(self):
        imageElement = self._getElement()
        urlImage = str(join(self.siteUrl, imageElement['src']))
        return urlImage

    def _saveImage(self):
        imageBin = requests.get(self._getUrlImage()).content
        completePath = os.path.join(self.savePath, self.fileName)
        with open(completePath, 'wb') as handler:
            handler.write(imageBin)
        print(join(self._getUrlImage(), " - Saved image"))
        self.setDesktopBackground(completePath)

    def setDesktopBackground(self, completePath):
        SO = platform

        print(SO)
        if SO == 'darwin':
            subprocess.Popen(
                str('PICTURE_DIR='+completePath+'\n')+SCRIPT, shell=True)
            print(str('PICTURE_DIR='+completePath+'\n')+SCRIPT)
            """ subprocess.call(shlex.split(str(os.getcwd()+'/mac.sh '+completePath) )) """


image1 = AstronomyOnDesktop(
    '/Users/producao/www/astronomyOnDesktop/',  # Folder to save image
    'astronomy4.jpg',  # Image file name
    'https://apod.nasa.gov/apod/'
)

image1._saveImage()


""" save_path = './'
file_name = "astronomy.jpg"

url = "https://apod.nasa.gov/apod/"

site = urllib.request.urlopen(url).read()
soup_HTML = BeautifulSoup(site, features="html.parser")

image = soup_HTML.find("img")
completeName = os.path.join(save_path, file_name)

if (image) :
  linkImage = str(join(url,image['src'])) # text of content attribute
  imageSite = requests.get(linkImage).content
  print(join(linkImage, " - Saved image"))

  with open(completeName, 'wb') as handler:
      handler.write(imageSite)
else : print("Today is not a image! :( ") """
