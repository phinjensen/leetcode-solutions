from threading import Semaphore

class Foo:
    def __init__(self):
        self.firstDone = Semaphore(0)
        self.secondDone = Semaphore(0)


    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.firstDone.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.firstDone.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.firstDone.release()
        self.secondDone.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.secondDone.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
