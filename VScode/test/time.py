time = int(input("请输入凌晨过去了多久:\n>>>"))
if time < 60:
    print("当前时间是12点%s分" % time)
else:
    hour = time%60
    print("当前时间是12点%s分" % time)
