import os
from datetime import datetime


current = os.getcwd()
logfile = 'main.log'
path = os.path.join(current, logfile)


def logger_par(path):
    
    def __logger(old_function):
        def new_function(*args, **kwargs):
            date_time = datetime.now()
            func_name = old_function.__name__
            result = old_function(*args, **kwargs)
            with open(path, 'a', encoding='utf-8') as log:
                log.write(f'Время вызова функции: {date_time}\n' 
                          f'имя функции: {func_name}\n' 
                          f'Аргументы: {args} _ {kwargs}\n'
                          f'Результат: {result}')
            return result
        return new_function

    return __logger



def test_2():
    paths = ('log_1.log', 'log_2.log', 'log_3.log')

    for path in paths:
        if os.path.exists(path):
            os.remove(path)

        @logger_par(path)
        def hello_world():
            return 'Hello World'

        @logger_par(path)
        def summator(a, b=0):
            return a + b

        @logger_par(path)
        def div(a, b):
            return a / b

        assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
        result = summator(2, 2)
        assert isinstance(result, int), 'Должно вернуться целое число'
        assert result == 4, '2 + 2 = 4'
        result = div(6, 2)
        assert result == 3, '6 / 2 = 3'
        summator(4.3, b=2.2)

    for path in paths:

        assert os.path.exists(path), f'файл {path} должен существовать'

        with open(path) as log_file:
            log_file_content = log_file.read()

        assert 'summator' in log_file_content, 'должно записаться имя функции'

        for item in (4.3, 2.2, 6.5):
            assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_2()
