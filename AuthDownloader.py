import urllib.request
from urllib.request import urlopen
import urllib
from http import cookiejar


class AuthDownloader:
    def __init__(self, base_url, link, username, password, output_file):
        self.baseUrl = base_url
        self.link = link
        self.data = {"username": username,
                     "password": password}
        self.file = output_file

    def WriteFileWithContents(self):
        with open(self.file, "wb") as file:
            passwordManager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
            passwordManager.add_password(None, self.baseUrl, self.data["username"], self.data["password"])
            cookies = cookiejar.CookieJar()
            urllib.request.HTTPBasicAuthHandler(passwordManager)
            opener = urllib.request.build_opener(
                urllib.request.HTTPBasicAuthHandler(passwordManager),
                urllib.request.HTTPCookieProcessor(cookies)
            )
            urllib.request.install_opener(opener)
            request = urllib.request.Request(self.link)
            response = urlopen(request, timeout=180)
            downloaded_bits = response.read()
            file.write(downloaded_bits)




