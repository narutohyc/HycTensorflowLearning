1. 讀取、訪問csv
  data = pd.read_csv(path)
  data['Heart_Rate'][0]
  
2. 保存csv
  cols = ['Heart_Rate', 'Respiratory', 'Attention']
  traindate = pd.DataFrame(traindate, columns=cols)
  traindate.to_csv(savetrainpath)
  
3. 判斷文件
  # 是否是文件
  os.path.isfile(filename)
  # 是否是目錄
  os.path.isdir(filename)
  # 列出所有文件
  csvList = os.listdir(filepath)
  
  
4. python创建、删除文件与文件夹
  os.mkdir(savepath)   #创建文件夹
  os.remove(path)  #删除文件 path. 如果path是一个目录， 抛出 OSError错误。
  os.rmdir(path)   #如果要删除目录，请使用rmdir().
  
  
5. 拼接路径
  os.path.join(’savepath‘, ‘png/demo’)   #正确
  os.path.join(’savepath‘, ‘/png/demo’)  #错误
  

6. 判断是否有中文
  def is_chinese(uchar):
    if u'\u4e00' <= uchar <= u'\u9fff':
        return True
    else:
        return False
      
7. 查看剩余空间大小 ubuntu下有效
  def checkDis(path):
    import os
    hd = {}
    disk = os.statvfs(path)
    percent = (disk.f_blocks - disk.f_bfree) * 100 / (disk.f_blocks - disk.f_bfree + disk.f_bavail) + 1
    return 100 - percent
  
