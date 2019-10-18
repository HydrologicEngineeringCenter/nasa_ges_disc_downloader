import argparse
import check
import LinkDownload
import ThreadedFunction
import time


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--path_to_links", dest="links_path", help="text file having list of download links",
                        type=str, required=True)
    parser.add_argument("-d", "--destination", dest="download_directory", help="download location of files",
                        type=str, required=True)
    parser.add_argument("-u", "--username", dest="username", help="username for website",
                        type=str, required=True)
    parser.add_argument("-p", "--password", dest="password", help="password for website",
                        type=str, required=True)
    parser.add_argument("-n", "--threads", dest="thread_count", help="amount of threads for download",
                        type=int, required=True)
    args = parser.parse_args()

    file = check.check_file(args.links_path)
    directory = check.check_dir(args.download_directory)

    start = time.time()
    ThreadedFunction.RunMethodWithThreads(LinkDownload.link_download, (file, directory, args.username, args.password),
                                          args.thread_count)
    end = time.time()
    elapsed_time = end - start
    print("\n -- Total Download Time: %d:%.2d --\n" % (elapsed_time / 60, elapsed_time % (elapsed_time / 60)))
    return 0


main()
