#1
l = []
s = 'word'
i = 5
f = 3.4
b = True
d = [0,1]
l.append(s)
l.append(i)
l.append(f)
l.append(b)
l.append(d)
print('1)',l)

#2
names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]
a = names.count('Jack')
print('2)', a)

#3
names
a = names[1:11:2]+names[11:]

print('3)',a)

#4
name = 'Adil'
year = 2005
lang = 'Python'
myList = []
myList.append(name)
myList.append(year)
myList.append(lang)
print('4)',myList)

#5
name = ['Adil','Usman','Beks','Damir','Islam']
s = ","
a = s.join(name)
print('5)',a)

