import argparse
import check
import LinkDownload
import ThreadedFunction
import time


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("FILE_PATH", help="text file having list of download links", type=str)
    parser.add_argument("DOWNLOAD_DIRECTORY", help="download location of files", type=str)
    parser.add_argument("USERNAME", help="username for website", type=str)
    parser.add_argument("PASSWORD", help="password for website", type=str)
    parser.add_argument("THREAD_COUNT", help="amount of threads for download", type=int)
    args = parser.parse_args()

    file = check.check_file(args.FILE_PATH)
    directory = check.check_dir(args.DOWNLOAD_DIRECTORY)

    start = time.time()
    ThreadedFunction.RunMethodWithThreads(LinkDownload.link_download, (file, directory, args.USERNAME, args.PASSWORD), args.THREAD_COUNT)
    end = time.time()
    elapsed_time = end - start
    print("\n -- Total Download Time: %d:%.2d --\n" % (elapsed_time / 60, elapsed_time % (elapsed_time / 60)))
    return 0


main()
