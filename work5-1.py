print("---欢迎进入通讯录程序---")
print("---1：查询联系人资料 ---")
print("---2：插入新的联系人---")
print("---3：删除已有联系人---")
print("---4：退出通讯录程序---")

aline = { }

while 1:
    nums = input('请输入相关的指令代码：')
   
    if nums == '1':
        name = input('请输入联系人姓名：')
        if name in aline:
            print(aline[name]+aline[tel])
        else:
            print('您输入的姓名不再通讯录中！')

    if nums == '2':
        name = input("请输入联系人姓名：")
        if name not in aline:
            tel = input("请输入用户联系电话：")
            aline[name] = name
            aline[tel] = tel
        else:
            print("您输入的姓名在通讯录中：",aline[name],aline[tel])
            arr = input("是否修改用户资料（YES/NO)： ")
            if arr == 'YES':
                tel = input("请输入用户联系电话：")
                aline[tel] = tel

    if nums == '3':
        name = input("请输入您要删除的联系人： ")
        if name in aline:
            del aline[name]
        else:
            print("你输入的联系人不在通讯录")

    if nums == '4':
        print("退出通讯录程序")
        break
print(aline)
