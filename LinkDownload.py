import os, sys, urllib
import AuthDownloader
import threading


def link_download(file, dir, username, password):
    os.chdir(dir)
    old_file_count = len(os.listdir(dir))
    with open(file) as fp:
        list = fp.readlines()
        for link in enumerate(list):
            with threading.Lock():
                file_name = os.path.basename(link[1])
                file_name = file_name.strip('\n')
                file_name = file_name.replace('?', '')
                file_name = file_name.replace('!', '')
                file_name = file_name.replace('%', '')
                file_name = file_name.replace('#', '')
                if len(file_name) > 150:
                    file_name = file_name[0:150]
                if os.path.exists(file_name):
                    continue

            try:
                bill = AuthDownloader.AuthDownloader("https://urs.earthdata.nasa.gov",
                                                     link[1], username, password, file_name)
                bill.WriteFileWithContents()

            except urllib.error.HTTPError as m:
                with threading.Lock():
                    print("\r--> %s Failed to download \"%s\". Reason: %s" % (threading.get_ident(), file_name, m))
                    continue

            except urllib.error.URLError as m:
                with threading.Lock():
                    print("\r--> %s Failed to download \"%s\". Reason: %s" % (threading.get_ident(), file_name, m))
                    continue

            except ConnectionResetError as m:
                with threading.Lock():
                    print("\r--> %s Failed to download \"%s\". Reason: %s" % (threading.get_ident(), file_name, m))
                    continue


            # Display download progress to user
            sys.stdout.write("\r    --> Downloading: %d/%d" % (len(os.listdir(dir)) - old_file_count, len(list)))
            sys.stdout.flush()
