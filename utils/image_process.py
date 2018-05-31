# -*- coding: utf-8 -*-

1) 圖像擴充np.pad  鏡像反轉復制
    import numpy as np
    from skimage import io
    image = io.imread('/home/hyc/code/dehaze/TestVirtualimages/ground_truth_image/art.png')
    padd = 600
    imga = np.pad(np.reshape(image,newshape=[-1,image.shape[0],image.shape[1],image.shape[2]]), [[0, 0], [padd, padd], [padd, padd], [0, 0]], mode='reflect')
    imga = np.reshape(imga,newshape=[imga.shape[1],imga.shape[2],imga.shape[3]])
    # io.imshow(imga)
    io.imsave('/home/hyc/code/dehaze/art.png',imga)
    # io.imshow(imga)

2)  圖像倍數復制
    img = io.imread(join(imgpath, imgList[ii]))
    padd = 3 #倍數
    imgdou = np.zeros([img.shape[0]*padd,img.shape[1]*padd,3])
    for jj in range(padd):
        for kk in range(padd):
            imgdou[jj*img.shape[0]:(jj+1)*img.shape[0],kk*img.shape[1]:(kk+1)*img.shape[1],:] = np.uint8(img[:,:,:])
    imgdou = np.uint8(imgdou)
    
3）xxx

4) xxx




