import time
from multiprocessing import Pool


# Создавать локальный список all_data.
# Открывать файл name для чтения.
# Считывать информацию построчно (readline), пока считанная строка не окажется пустой.
# Во время считывания добавлять каждую строку в список all_data.


def read_info(name):
    all_data = []
    file_start_time = time.time()
    with open(name) as file:
        line = file.readline()
        while line:
            all_data.append(line)
            line = file.readline()
    file_read_time = time.time()
    print(f'Файл {str(name[2::])} прочитан за {round(file_read_time - file_start_time, 4)}')

if __name__ == '__main__':

    filenames = [f'./file {number}.txt' for number in range(1, 5)]


    # Линейный вызов
    # start_time = time.time()
    # for name in filenames:
    #     read_info(name)
    # stop_time = time.time()
    # print(f'Линейный вызов: {round(stop_time - start_time, 4)}')


    # Многопроцессный

    start_time = time.time()
    x= 0
    pool_name = []

    for name in filenames:
        x+= 1
        pool_name.append(name)

    with Pool(processes= x) as pool:
        res = pool.map(read_info, pool_name,)
        stop_time = time.time()
        print(f'Многопроцессный вызов: {round(stop_time - start_time, 4)}')