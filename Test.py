import re
str="1232弱智13213智障哈哈小学生哈"
list=['弱智','小学生','智障']

for s in list:
    if re.search(s,str)!=None:
        s,e=re.search(s, str).span()
        str=str[0:s]+"**"+str[e:]

print(str)


