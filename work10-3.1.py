list1 = []
old_words_number = 0
file_name = input('请输入文件名：')
file = open(file_name, 'rt')
old_words = input('请输入需要替换的单词或字符：')
new_words = input('请输入新的单词或字符：')
for each_line in file:
       if old_words in each_line:
              old_words_number = each_line.count(old_words)
              each_line = each_line.replace(old_words, new_words)
       list1.append(each_line)
print('文件%s中共有%d个【%s】' % (file_name, old_words_number, old_words))
print('您确定要把所有的【%s】替换为【%s】吗？' % (old_words, new_words))
flag = input('【YES/NO】：')
if flag.upper() == 'YES':
       file_write = open(file_name, 'wt')
       file_write.writelines(list1)
       file_write.close()
else:
       print('文件%s未更改！' % file_name)
file.close()
