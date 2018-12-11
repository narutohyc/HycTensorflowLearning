
# python基础语法技巧


```python
# 查看库中常用模块
import numpy as np
import math
dir(math)
```




    ['__doc__',
     '__loader__',
     '__name__',
     '__package__',
     '__spec__',
     'acos',
     'acosh',
     'asin',
     'asinh',
     'atan',
     'atan2',
     'atanh',
     'ceil',
     'copysign',
     'cos',
     'cosh',
     'degrees',
     'e',
     'erf',
     'erfc',
     'exp',
     'expm1',
     'fabs',
     'factorial',
     'floor',
     'fmod',
     'frexp',
     'fsum',
     'gamma',
     'gcd',
     'hypot',
     'inf',
     'isclose',
     'isfinite',
     'isinf',
     'isnan',
     'ldexp',
     'lgamma',
     'log',
     'log10',
     'log1p',
     'log2',
     'modf',
     'nan',
     'pi',
     'pow',
     'radians',
     'remainder',
     'sin',
     'sinh',
     'sqrt',
     'tan',
     'tanh',
     'tau',
     'trunc']



## 数组按照某关键字比较


```python
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
pairs
```




    [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]



## import上层文件，需要添加上层路径


```python
import sys
sys.path.append("..")
# from utils import loadDate
```

## List打乱顺序


```python
import random
mlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(mlist) # 对list洗牌，在原list上做改变
print(mlist)
```

    [1, 7, 2, 9, 0, 3, 8, 5, 4, 6]
    

### 计算经纬度距离


```python
import math
def cal_dis(latitude1, longitude1, latitude2, longitude2):  
    # 计算实际距离（纬度1，经度1，纬度2，经度2）
    latitude1 = (math.pi / 180.0) * latitude1
    latitude2 = (math.pi / 180.0) * latitude2
    longitude1 = (math.pi / 180.0) * longitude1
    longitude2 = (math.pi / 180.0) * longitude2
    # 因此AB两点的球面距离为:{arccos[sina*sinx+cosb*cosx*cos(b-y)]}*R  (a,b,x,y)
    # 地球半径
    R = 6378.1
    temp = math.sin(latitude1) * math.sin(latitude2) + math.cos(latitude1) * \
            math.cos(latitude2) * math.cos(longitude2 - longitude1)
    d = math.acos(temp) * R
    return d
```

## 分割字符串并转换类型
``` python
fromstring(string, dtype=float, count=-1, sep='')
```


```python
import numpy as np
line = '12,26,31,17,90,28,88,40,77'
npyArray = np.fromstring(line, dtype=int, sep=',')
npyArray
```




    array([12, 26, 31, 17, 90, 28, 88, 40, 77])



## enumerate()函数原型
``` python
enumerate(self, /, *args, **kwargs)
Docstring:
    enumerate(iterable[, start]) -> iterator for index, value of iterable
```



```python
a = [5,2,4,6,7]
for i,j in enumerate(a,1):
    print('index:%d   value:%d' % (i,j))
```

    index:1   value:5
    index:2   value:2
    index:3   value:4
    index:4   value:6
    index:5   value:7
    

## 检查对象是否可调用
``` python
callable(obj, /)
Docstring:
    Return whether the object is callable (i.e., some kind of function).
```


```python
def fn(a):
    print(a)
print(callable(fn))
```

    True
    

## assert用法


```python
assert 2==2,'2==2？'
```

## 三目运算符


```python
'Yes' if True else 'No'
```




    'Yes'


