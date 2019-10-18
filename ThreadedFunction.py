import threading


def RunMethodWithThreads(function, args, threads):
    # Creating threads
    thread_list = []
    for i in range(threads):
        t = threading.Thread(target=function, name="thread{}".format(i),
                             args=args, daemon=True)
        thread_list.append(t)
        t.start()

    for t in thread_list:
        t.join()
