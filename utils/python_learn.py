1. 数组按照某关键字比较
  >>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
  >>> pairs.sort(key=lambda pair: pair[1])
  >>> pairs
  [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
  
2. import上層文件，需要添加上層路徑
  import sys
  sys.path.append("..")
  from utils import loadDate
3. List亂序
  import random   
  list = range(10)  
  random.shuffle(list) # 对list洗牌，在原list上做改变
