import multiprocessing


class Producer(multiprocessing.Process):

    def __init__(self, q):
        super().__init__()
        self.q = q

    def run(self):
        for i in range(10):
            self.q.put(i)
            print("生产者生产了 数字: {}".format(i))


class Consumer(multiprocessing.Process):

    def __init__(self, q):
        super().__init__()
        self.q = q

    def run(self):
        while True:
            i = self.q.get()
            print("消费者消费了 数字: {}".format(i))


def main():
    manager = multiprocessing.Manager()
    q = manager.Queue()
    p = Producer(q)
    c = Consumer(q)
    p.start()
    c.start()
    c.join()


if __name__ == '__main__':
    main()
