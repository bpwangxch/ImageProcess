
import os
import os.path
from collections import Counter
#windows ,给出一个路径，递归遍历所有文件；所有重名的文件，只保留一份，其余都删除。保留的文件目录未做限定
rootdir = r"Z:\王兴春\巴塘河"
dict1={}
list1=[]
for parent, dirnames, filenames in os.walk(rootdir):
    for filename in filenames:
        dict1[os.path.join(parent, filename)]=filename #key:全路径,value:文件名称
        list1.append(filename)
'''
Counter(list1),返回一个Counter类型：Counter({'1.rar': 11, '1.txt': 11, '1.zip': 11})；
 转换成dict类型后：<class 'dict'>: {'1.rar': 11, '1.txt': 11, '1.zip': 11}

 '''
delf = open("log.txt","a")
list2=[str(k) for k,v in dict(Counter(list1)).items() if v>1]
todeleteno=0
for l in list2:
    n = 0
    for k,v in dict1.items():
        if l==v:
            if n==0:
                print('不删:{v}-----{k}'.format(v=v, k=k))
            else:
                todeleteno+=1
                print('删除{n}:{v}-----{k}'.format(n=str(todeleteno).zfill(5),v=v, k=k))
                delf.write('删除{n}:{v}-----{k}'.format(n=str(todeleteno).zfill(5),v=v, k=k))
                os.remove(k)
            n+=1
delf.close()
print("删除总数:"+str(todeleteno))
