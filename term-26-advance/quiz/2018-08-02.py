import multiprocessing
import random
import time

"""
刘备张飞关羽，在某客栈喝酒，要不醉不归
消费者（刘、关、张）负责在桌子上喝酒
生产者（小二）负责拿酒到桌子上
"""
wine_content = [
    ('桑落酒', 1000),
    ('杜康酒', 500),
    ('仙酒', 500)]


class Wine(object):

    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

    def decrease_volume(self, num):
        # 减少酒的容量
        temp_data = self.volume - num
        # 如果 减少后的酒的容量为负数， 则将酒的容量设置为0
        self.volume = temp_data if temp_data >= 0 else 0


class Producer(multiprocessing.Process):

    def __init__(self, name, q):
        super().__init__()
        self.name = name
        self.q = q

    def run(self):
        # 等酒桌上没酒了再添一次酒，不一定要添满酒桌
        while True:
            if self.q.empty():
                print("洒家，拿酒，哥几个今天要不醉不归！")
                for i in range(random.randint(3, 5)):
                    w_name, w_volume = random.choice(wine_content)
                    w = Wine(w_name, w_volume)
                    self.q.put(w)
                    print("客官，您瞧好了，这是本店的{}, 入口不辣嗓，"
                          "饮后有留香，醉后不上头".format(w.name))


class Consumer(multiprocessing.Process):

    def __init__(self, name, capacity, q):
        super().__init__()
        # 姓名
        self.name = name
        # 理论酒量
        self.capacity = capacity
        # 剩余酒量
        self.wohainenghe = capacity
        self.q = q

    def decrease_capacity(self, num):
        temp_data = self.wohainenghe - num
        self.wohainenghe = temp_data if temp_data >= 0 else 0

    def run(self):

        while self.wohainenghe > 0:
            # 取得酒对象
            w = self.q.get()
            while self.wohainenghe > 0 and w.volume > 0:
                num = random.randint(200, 500)

                # 喝酒
                w.decrease_volume(num)
                self.decrease_capacity(num)
                print("{} 剩余酒量：{}".format(self.name, self.wohainenghe))
                # 控制喝酒频率
                time.sleep(random.randint(1, 3))

        print("{}已经醉倒, 呼噜...呼噜...".format(self.name))


def main():
    manager = multiprocessing.Manager()
    # 酒桌最大容量是5坛酒
    q = manager.Queue(5)
    p1 = Producer(name="小二", q=q)
    consumer1 = Consumer(name='刘备', capacity=6000, q=q)
    consumer2 = Consumer(name='关羽', capacity=7000, q=q)
    consumer3 = Consumer(name='张飞', capacity=8000, q=q)
    consumer1.start()
    consumer2.start()
    consumer3.start()
    p1.start()

    while True:
        if not (consumer1.is_alive() or consumer2.is_alive() or consumer3.is_alive()):
            print("刘、关、张，今夜果真不醉不归。。。")
            print('现在已经是寅时， 关店大吉!')
            p1.terminate()
            break


if __name__ == '__main__':
    main()
