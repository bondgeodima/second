import os
import shutil

def copy_file():
    """
    Сортирует картинки по папкам. Номер папкки соответствует номеру класса
    :return:
    """
    f = open("D:/bsn_view_3.csv", "r")
    p = 'D:/out/'
    p_out = 'D:/out_sort'
    for x in f:
        if x != "":
            x = x.split(";")
            if int(x[4]) > 0:
                fold = str(('%03d' %int(x[4])))
                type_fold = x[1][10:11]
                file = p + x[1][10:((len(x[1])) - 4)] + '.png'
                if type_fold == 't':
                    new_file = p_out + '/train/' + fold + "/" + x[1][10:((len(x[1])) - 4)] + '.png'
                    if not os.path.exists(p_out + '/train/' + fold + "/"):
                        os.mkdir(p_out + '/train/' + fold + "/")
                if type_fold == 'v':
                    new_file = p_out + '/val/' + fold + "/" + x[1][10:((len(x[1])) - 4)] + '.png'
                    if not os.path.exists(p_out + '/val/' + fold + "/"):
                        os.mkdir(p_out + '/val/' + fold + "/")
                # print(x[1][10:((len(x[1]))-4)], x[4])
                print (file)
                # os.rename(file, new_file)
                shutil.move(file, new_file)
                # os.replace(file, new_file)

def check_folder():
    """
    Проверяет каких папок нет (т.е. без информации, без картинок)
    :return:
    Возвращает перечень папок которіз нет
    """
    p_out = 'D:/out_sort/train/'
    p = []
    for x in os.scandir(p_out):
        # print (x.path[18:21])
        # traint
        p.append(int(x.path[18:21]))
        # val
        # p.append(int(x.path[16:19]))

    for i in range(1, 168):
            if i not in p:
                print (str(('%03d' %int(i))))


def calc_file_in_folder():
    """
    Считает количество файлов в каждой папке
    :return:
    Список: папка - количество файлов
    """
    p_out = 'D:/out_sort/train/'
    p = []
    f = {}
    for x in os.scandir(p_out):
        # print (x.path[18:21])
        # traint
        p.append(int(x.path[18:21]))
        # val
        # p.append(int(x.path[16:19]))
        i = 0
        for y in os.scandir(p_out + '/' + str(x.path[18:21]) + '/'):
            i += 1
        f[str(x.path[18:21])] = i

    for (key, value) in f.items():
        print(key , ":", value)

calc_file_in_folder()


