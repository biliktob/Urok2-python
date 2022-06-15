string = int(input("Введите угодное Вам количество элементов в списке:"))
list1 = []
for el in range(string):
    elem = input("Введите элементы:")
    list1.append(elem)
print("Ваш список: {s1}".format(s1=list1))
for i in range(0, len(list1) - 1):
        list1[i], list1[i+1] = list1[i+1], list1[i]
print(list1)
