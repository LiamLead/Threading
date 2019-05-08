import threading
import time


class Payment(threading.Thread):
    def __init__(self, threadID, name, delay, count):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay
        self.count = count

    def run(self):
        print("Starting: " + self.name + "\n")
        thread_lock.acquire()                # lock everything until this thread has finished
        print_time(self.name, self.delay, self.count)
        thread_lock.release()                # release the krakens (the lock)
        print("Exiting: " + self.name + "\n")


class Loading(threading.Thread):
    def __init__(self, threadID, name, delay, count):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay
        self.count = count

    def run(self):
        print("Starting: " + self.name + "\n")
        thread_lock.acquire()
        thread_lock.release()
        print_time(self.name, self.delay, self.count)
        print("Exiting: " + self.name + "\n")


def print_time(name, delay, count):
    while count:
        time.sleep(delay)
        print("%s: %s %s" % (name, time.ctime(time.time()), count))
        count -= 1


payment = Payment(1, "Payment", 1, 5)
load_page = Loading(2, "LoadingPage", 1, 3)
send_email = Loading(3, "SendingEmail", 1.2, 10)
thread_lock = threading.Lock()

payment.start()
load_page.start()
send_email.start()
payment.join()
load_page.join()
send_email.join()
print("Done")
