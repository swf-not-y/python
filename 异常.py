try:
	a1=input("请输入一个被除数：")
	a2=input("请输入一个除数：")
	print("商为：",a1/a2)
except Exception:
	print("除数不能是0")