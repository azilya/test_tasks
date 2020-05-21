import time


class Timer(object):
    def __init__(self, name=None):
        self.name = name
        self.tstart = time.time()

    def __enter__(self):
        self.tstart = time.time()
        return self

    def elapsed_s(self):
        return time.time() - self.tstart

    def __exit__(self, type, value, traceback):
        if self.name:
            print(f'{self.name}')
        v = self.elapsed_s()
        if v > 1:
            print(f'Elapsed: {self.elapsed_s():0.2f} s')
        elif v > 0.001:
            print(f'Elapsed: {self.elapsed_s():0.4f} s')
        else:
            print(f'Elapsed: {self.elapsed_s():0.9f} s')

    def __repr__(self):
        return f'"Timer(tstart={self.tstart}, elapsed={self.elapsed_s():0.5f})'


def slowly_process(s):
    # s = s * 0.01  # для временного ускорения запуска без кэша
    time.sleep(s)
    print(f"slowly processed for {s} s")


def cache(func):
    # словарь значений для набора аргументов;
    # число аргументов разное в зависимости от функции,
    # это позволяет хранить их в общей структуре
    storage = {}

    def cache_(*args, **kwargs):
        # сортируем именованные параметры по алфавиту,
        # чтобы они однозначно определялись по порядку значений: a, b, c
        kwargs = dict(sorted(kwargs.items()))

        # объединяем не именованные и именованные параметры в один ключ,
        # чтобы иметь возможность получить результат из кэша,
        # если способ передачи параметра изменился между вызовами:
        # f(1) -> f(a=2)
        arguments = args + tuple(kwargs.values())

        # если набор аргументов уже обработан, берем результат из кэша
        if arguments in storage:
            return storage[arguments]
        # в противном случае вычисляем результат и кэшируем его
        else:
            res = func(*args, **kwargs)
            storage[arguments] = res
            return res

    return cache_


@cache
def f1(a):
    slowly_process(1)
    return a + 0.1


@cache
def f2(a, b):
    slowly_process(1)
    return f1(a) * 2 + b


@cache
def f3(a, b, c):
    slowly_process(1)
    return f2(a, b) + c


with Timer() as t:
    for i in range(10):
        print(f"f1({i})={f1(i)}")
    for i in range(5):
        for j in range(5):
            print(f"f2({i}, {j})={f2(i, j)}")
    for i in range(3):
        for j in range(2):
            print(f"f3({i}, {j}, c=-100)={f3(i, j, c=-100)}")
    print(t)
