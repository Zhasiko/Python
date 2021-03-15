import re
import csv

file = open(r'C:\pythonn\week4\raw.data','r',encoding ='utf8')
x = file.read()
namecPattern = r'\nФилиал.*(?P<NAMEC>\b[a-zA-Z]+).*Астана\n'
BINpattern = r'\nБИН.*(?P<BIN>\b[0-9]+)'

NameSol = re.search(namecPattern, x).group("NAMEC")
BINSol = re.search(BINpattern, x).group("BIN")

DatePattern = r'\nВремя: (?P<date>\b[0-9].*)\n{1}(?P<address>.*)'

DateSol = re.search(DatePattern, x).group("date")
AddressSol = re.search(DatePattern, x).group("address")

itemPattern = r"(?P<name>.*)\n{1}(?P<count>.*)x(?P<price>.*)\n{1}(?P<total>.*)\n{1}Стоимост\n{1}(?P<total2>.*)"
itemPatternSol = re.compile(itemPattern)


items = [["Филиал","БИН","Наименование товара","Кол-во","Цена за единиц", "Общ цена","Дата","Адресс"]]


for m in re.finditer(itemPatternSol, x):
    #items.append([NameSol,BINSol, m.group("name").strip(),m.group("count").strip(), m.group("price").strip(), m.group("total2").strip(),DateSol, AddressSol])
 print(m.group("name") + " " + m.group("count") + m.group("price"))
'''
DatePattern = r'\nВремя: (?P<date>\b[0-9].*)\n{1}(?P<address>.*)'
AddressPattern = r'\nг. (?P<address>.*)'

DateSol = re.search(DatePattern, x).group("date")
AddressSol = re.search(AddressPattern, x).group("address")

with open('file.csv','w',newline='',encoding = 'utf8') as f:
    writer = csv.writer(f)
    writer.writerows(items)
'''
file.close()
