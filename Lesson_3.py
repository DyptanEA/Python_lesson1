import pymorphy2

morph = pymorphy2.MorphAnalyzer()

f = open('text.txt', 'r', encoding="utf-8")
my_str = f.read()
f.close()
my_list = [',', '.', '-', '?',':',';','!',' —','(',')','"','»','«','  ']
for s in my_list:
    my_str = my_str.replace(s, ' ')
my_split = my_str.split()
my_split = list(map(lambda x: x.lower(), my_split))
my_split = list(map(lambda x: morph.parse(x)[0].normal_form, my_split))
my_set = set(my_split)
my_dict = dict.fromkeys(my_set, 0)
for i in range(len(my_split)):
     my_dict[my_split[i]] += 1
list_sort=list(my_dict.items())
list_sort.sort(key=lambda i: i[1])
print('словарь ',my_dict)
list_sort.reverse()
for i in range(5):
       print(list_sort[i])
print('всего различных слов в тексте: ',len(my_set))




