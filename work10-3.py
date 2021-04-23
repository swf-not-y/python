filename = input("请输入文件名：")
old = input("请输入需要替换的单词或字符：")
new = input("请输入新的单词或字符：")
lines = []
c = 0

with open(filename,'r') as file:
    lines1 = file.readlines()
for line in lines1:
    if old in line:
        line = line.replace(old,new)
        c+=1
    lines.append(line)
    
print(f"文件{filename}共有{c}个{old}")
decide = input(f"你确定要把所有的{old}替换成{new}吗？\n[yes/no]:")
if decide in ["yes"]:
    with open(filename,'w') as file1:
        w1 = file1.writelines(lines)
with open(filename) as file2:
    w2 = file2.read()
print(w2)
