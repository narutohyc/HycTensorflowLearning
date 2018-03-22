# -*- coding: utf-8 -*-

1) 圖像擴充np.pad
    import numpy as np
    from skimage import io
    image = io.imread('/home/hyc/code/dehaze/TestVirtualimages/ground_truth_image/art.png')
    padd = 600
    imga = np.pad(np.reshape(image,newshape=[-1,image.shape[0],image.shape[1],image.shape[2]]), [[0, 0], [padd, padd], [padd, padd], [0, 0]], mode='reflect')
    imga = np.reshape(imga,newshape=[imga.shape[1],imga.shape[2],imga.shape[3]])
    # io.imshow(imga)
    io.imsave('/home/hyc/code/dehaze/art.png',imga)
    # io.imshow(imga)

2)






