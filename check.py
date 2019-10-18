import os, sys, requests

def check_dir(user_dir):
    if (os.path.isdir(user_dir) == False):
        try:
            os.mkdir(user_dir)
        except PermissionError:
            print("Permission denied, check permission settings")
            sys.exit()
        except FileNotFoundError:
            print("Can't create multiple subdirectories")
            sys.exit()
        else:
            os.chdir(user_dir)
    else:
        os.chdir(user_dir)
    return user_dir

def check_url(user_url):
    try:
        r = requests.get(user_url)
    except:
        print("URL does not exist or unreachable\n")
        sys.exit()
    if (r.status_code != 200):
        print("URL does not exist or unreachable\n")
        sys.exit()
    return user_url

def check_file(file):
    if not os.path.exists(file):
        print("%s does not exist\n" % file)
        sys.exit()
    return file