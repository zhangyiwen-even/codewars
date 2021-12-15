# Python的标准库有：
# 名称	            作用
# datetime	  为日期和时间处理同时提供了简单和复杂的方法。
# zlib	      直接支持通用的数据打包和压缩格式：zlib，gzip，bz2，zipfile，以及 tarfile。
# random	  提供了生成随机数的工具。
# math	      为浮点运算提供了对底层C函数库的访问。
# sys	      工具脚本经常调用命令行参数。这些命令行参数以链表形式存储于 sys 模块的 argv 变量。
# glob	      提供了一个函数用于从目录通配符搜索中生成文件列表。
# os	      提供了不少与操作系统相关联的函数。

# Python常用的第三方库有：
# 名称	           作用	
# Scrapy	   爬虫工具常用的库。
# Requests	   http库。	 
# Pillow	   是PIL（Python图形库）的一个分支。适用于在图形领域工作的人。
# matplotlib   绘制数据图的库。对于数据科学家或分析师非常有用。	 
# OpenCV	   图片识别常用的库，通常在练习人脸识别时会用到	
# pytesseract  图片文字识别，即OCR识别	
# wxPython	   Python的一个GUI（图形用户界面）工具。	 
# Twisted	   对于网络应用开发者最重要的工具。	 
# SymPy	       SymPy可以做代数评测、差异化、扩展、复数等等。	 
# SQLAlchemy   数据库的库。	 
# SciPy	       Python的算法和数学工具库。	 
# Scapy	       数据包探测和分析库。	 
# pywin32	   提供和windows交互的方法和类的Python库。	 
# pyQT	       Python的GUI工具。给Python脚本开发用户界面时次于wxPython的选择。	 
# pyGtk	       也是Python GUI库。	 
# Pyglet	   3D动画和游戏开发引擎。	 
# Pygame	   开发2D游戏的时候使用会有很好的效果。	 
# NumPy	       为Python提供了很多高级的数学方法。	 
# nose	       Python的测试框架。	 
# nltk	       自然语言工具包。	 
# IPython	   Python的提示信息。包括完成信息、历史信息、shell功能，以及其他很多很多方面。	 
# BeautifulSoup	xml和html的解析库，对于新手非常有用。

# 常用库
# 一.time 时间处理模块
# import time
# 1.time time() 返回当前时间的时间戳（1970纪元后经过的浮点秒数）。
# print(time.time())

# 2.import datetime
# MINYEAR <= year <= MAXYEAR
# 1 <= month <= 12
# 1 <= day <= number of days in the given month and year
# 0 <= hour < 24
# 0 <= minute < 60
# 0 <= second < 60
# 0 <= microsecond < 1000000
# 这是datetime.datetime参数的取值范围，如果设定的值超过这个范围，那么就会抛出ValueError异常。
# 其中year，month，day是必须参数。

# import datetime
# 3.strftime() 和 strptime()
# 由datetime转换成字符串：datetime.strftime()
# 由字符串转换成datetime：datetime.datetime.strptime()
# print(datetime.striftime())

# 二.目录操作模块
# 1.获取当前工作目录
# import sys
# print(sys.path[0])

# 2.获取执行命令的位置
# import os
# print(os.getcwd())

# 3.路径拼接
# import os 
# print(os.path.join('/usr/local','text.txt'))

# 4.路径拆分
# os.path.split() 函数：拆分路径
# import os
# print(os.path.split('/project/python-learn/learn55.py'))

# os.path.splitext()函数：直接获取文件扩展名
# import os
# print(os.path.splitext('/project/python-learn/learn55.py'))

# 5.文件重命名
# import os
# print(os.rename('learn55.py','learn54.py'))

# 6.删除文件
# import os
# print(os.remove('learn55.py'))

# 7.复制文件
# import shutil
# print(shutil.copyfile('learn54.py','learn55.py'))

# 8.遍历文件夹下的文件
# 1>.
# import os
# for filename in os.listdir('./'):
    # print(filename)

# 2>.
# import glob
# for filename in glob.glob('*.py'):
#     print(filename)

# 3>.
# import os
# for fpathe,dirs,fs in os.walk('./'):
#     print(fpathe)
#     print(dirs)
#     print(fs)
#     for f in fs:
#         print(os.path.join(fpathe,f))

# 9.判断文件是否存在
# import os
# print(os.path.isfile('text.txt')) #不存在返回false

# 10.判断目录是否存在
# import os
# print(os.path.exists('directory')) #不存在返回false

# 三.random:伪随机数生成器
# 1.导入库
# import random

# 2.随机整数
# from random import randint
# print(randint(1,10))    # 返回随机整数 N, N满足 a <= N <= b。

# 四.collections模块
# 该模块实现了专门的容器数据类型，为Python的通用内置容器提供了替代方案。 以下几种类型用的很多：
# defaultdict (dict子类调用工厂函数来提供缺失值)
# Counter (用于计算可哈希对象的dict子类)
# deque (类似于列表的容器，可以从两端操作)
# namedtuple (用于创建具有命名字段的tuple子类的工厂函数)
# OrderedDict (记录输入顺序的dict)

# 1.defaultdict
# 2.Counter:计数器
# (1)导入库
# from collections import Counter
# (2)Counter类创建
# 创建一个空的Counter类
# c = Counter()
# 从一个可迭代对象(list,tuple,dict,字符串等)创建
# c = Counter(iterable)

# (3)计件器键值对的增删查
# 计数值的访问
# c['计数键']
# 计数器的更新 使用另一个可迭代对象更新
# c.update(iterable)
# 计数键的删除
# del c['计数键']

# (4)计数器常用操作
# elements()
# 返回一个迭代器，每个元素重复计数的个数。元素顺序是任意的。如果一个元素的计数小于1， elements() 就会忽略它。
# most_common([n])
# 返回一个列表，提供 n 个频率最高的元素和计数。 如果没提供 n ，或者是 None ， most_common() 返回计数器中的 所有 元素。相等个数的元素顺序随机。
# subtract([iterable-or-mapping])
# 从迭代对象或映射对象减去元素。像dict.update() 但是是减去，而不是替换。输入和输出都可以是0或者负数。
# sum(c.values())  # 所有计数的总数
# c.clear()  # 重置Counter对象，注意不是删除
# list(c)  # 将c中的键转为列表
# set(c)  # 将c中的键转为set
# dict(c)  # 将c中的键值对转为字典
# c.items()  # 转为(elem, cnt)格式的列表
# Counter(dict(list_of_pairs))  # 从(elem, cnt)格式的列表转换为Counter类对象
# c.most_common()[:-n:-1]  # 取出计数最少的n-1个元素
# c += Counter()  # 移除0和负值

# 3.deque

# 4.namedtuple

# 5.OrderedDict