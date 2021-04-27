with open('第十章文本测试.txt') as file:    #相对路径
	a1 = file.read()
	a3 = file.tell   #查看当前文件指针位置
	file.seek(20,0)   #移动指针
	a2 = file.read()
	file.seek(40,0)
	a4=file.readline()
	file.seek(30,0)
	a5=file.read(4)
	file.seek(40,0)
	a6=file.readlines()

with open('第十章文本测试.txt','a') as file1:
	file1.write("美团老板是我。")

with open('第十章文本测试.txt') as file2:
	a7=file2.read()
print(a1)
print(a3)
print(a2)
print('\t')
print(a4)
print(a5)
print('\t')
print(a6)
print('**************')
print(a7)
