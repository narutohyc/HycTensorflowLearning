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
4. 列表刪除某些行或列
  对于一个二维数组，axis=0，表示行，axis=1，表示列
  这里删除第 0 行，第 2 行，第 4 行：
  np.delete(A, [0, 2, 4], axis=0)
5. 數組內復制
  from numpy import tile
  >>> a = np.array([0, 1, 2])
  >>> np.tile(a, 2)
      array([0, 1, 2, 0, 1, 2])
  >>> np.tile(a, (2, 2))
      array([[0, 1, 2, 0, 1, 2],
             [0, 1, 2, 0, 1, 2]])
  >>> np.tile(a, (2, 1, 2))
      array([[[0, 1, 2, 0, 1, 2]],
             [[0, 1, 2, 0, 1, 2]]])

6. 計算經緯度距離
  def cal_dis(latitude1, longitude1, latitude2, longitude2):  # 计算实际距离（纬度1，经度1，纬度2，经度2）
    latitude1 = (math.pi / 180.0) * latitude1
    latitude2 = (math.pi / 180.0) * latitude2
    longitude1 = (math.pi / 180.0) * longitude1
    longitude2 = (math.pi / 180.0) * longitude2
    # 因此AB两点的球面距离为:{arccos[sina*sinx+cosb*cosx*cos(b-y)]}*R  (a,b,x,y)
    # 地球半径
    R = 6378.1
    temp = math.sin(latitude1) * math.sin(latitude2) + \
           math.cos(latitude1) * math.cos(latitude2) * math.cos(longitude2 - longitude1)
    d = math.acos(temp) * R
    return d

7. 分割字符串并转换类型
  line = '12,26,31,17,90,28,88,40,77'
  npyArray = np.fromstring(line, dtype=int, sep=',')
  >>> [12, 26, 31, 17, 90, 28, 88, 40, 77]
  
8. 














