import string
import numpy as np
import pickle
import argparse


class Train:

    def __init__(gen, data):
        gen.data = data

    def norma(gen):
        #очистка текста
        words = np.array("".join(c.lower() for c in gen.data if (c.isalpha() | (c == ' '))).split(' '))
        return words

    def fit(gen, data):
        model = {}
        unique = np.unique(data)
        #создадим пустой словарь
        for u in unique:
            model[u] = []
        for u in unique:
            #создание массива контекстных слов
            act_word, = np.where(data == u)
            next_word = np.array([data[a + 1] for a in act_word if a != len(data) - 1])
            #создание массива уникальных значений контекстых слов и их подсчет
            unique_cont, counts = np.unique(next_word, return_counts=True)
            #заполнение словаря контекстными словами и вероятностями
            for val, coun in zip(unique_cont, counts):
                model[u].append([val, coun / np.sum(counts)])
        return model

    def generate(gen, model, url):
        #сохранение модели в файл
        with open(url, 'wb') as f:
            pickle.dump(model, f)

# консольный парсер
parser = argparse.ArgumentParser()
#добавление аргументов в парсер
parser.add_argument('--input-dir', dest='input_dir',
type = str)
parser.add_argument('--model', type=str)
args = parser.parse_args()
input_dir = args.input_dir
#ввод текста с клавиатуры
if input_dir == None:
    data = input('Введите текст, на основе которого будет проходить обучение:').replace('\n', ' ')
    #проверка(word count > 1)
    while len(data.split(' ')) == 1:
        data = input('Введите больше одного слова').replace('\n', ' ')
else:    
    #открыти датасета
    f = open(input_dir, 'r')
    data = f.read().replace('\n', ' ')
model = Train(data=data)
norm_text = model.norma()
fit_model = model.fit(norm_text)
model.generate(fit_model, args.model)
            if endword not in D:
                D[endword] = D.get(endword, ['.'])
            break

for i in range(0, len(a)):
    if a[i] in alph:
        s = str(a[i])
        s = s.lower()
        nfile += s
    else:
        nfile += " "
#print(oone)
a = nfile.split()
for i in range(0, len(a)):
    if a[i] not in D:
        D[a[i]] = D.get(a[i], [])
    if i != len(a) - 1:
        D[a[i]] += [a[i + 1]]
w = list(D.keys())
#print(D)
word = random.choice(w)
k = 1
while k == 1:
    print("Введите команду gen для генерации текста: ", end="")
    n = input()
    if n == "gen":
        while word != '.':
            print(word, end = " ")
            word = random.choice(list(D[word]))
        print('.')
        word = random.choice(w)
    print("Для продолжения нажмите 1: ", end = "")
    n1 = int(input())
    if n1 != 1:
        break