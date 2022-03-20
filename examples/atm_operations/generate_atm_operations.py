import random
import time
from threading import Thread

random.seed(42)
FILE = open("atm_operations.txt", "a")
FILE.write("\n")


class ATM(Thread):
    def __init__ (self, num, counter):
        Thread.__init__(self)
        self.num = num
        self.countdown = counter

    def ATM(self):
        deposit = ["d%s", "r%s", "a%s"]
        check = ["c%s", "r%s"]
        withdraw = ["w%s", "r%s", "s%s"]

        processes = [deposit, check, withdraw, []]
        process = random.choice(processes)

        for p in process:
            event = p % str(self.num)
            # print(event, end="")
            FILE.write(event)
            time_delay = random.random()
            time.sleep(time_delay/1000)

    def run(self):
        while self.countdown:
            self.ATM()
            self.countdown -= 1


def main():
    n_atm = 10
    N = [10, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000]
    counter = N[9]
    for thread_number in range(n_atm):
        thread = ATM(thread_number, counter)
        thread.start()


if __name__ == '__main__':
    main()
