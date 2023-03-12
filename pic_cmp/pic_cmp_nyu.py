import cv2,os
import numpy as np


display_count=654


root_list=[
'/home/colin/sota_depth_map/nyu/adabins_nyu_depthmap/',
'/home/colin/sota_depth_map/nyu/bts_nyu_depthmap/',
'/home/colin/sota_depth_map/nyu/dpt_nyu_depthmap/',
'/home/colin/sota_depth_map/nyu/nyu_test_depth/'
]


for i in range(display_count):

    img_list=[]

    img_name=str(i)+'.png'

    for k in root_list:

        img_path=os.path.join(k,img_name)

        img=cv2.imread(img_path)
        # print(img.shape)

        img=cv2.resize(img,(320,240))

        img_list.append(img)
    
    imgs=np.hstack(img_list)

    cv2.imshow('image index:'+str(i),imgs)
    cv2.waitKey(100000)
    cv2.destroyAllWindows()

    # break







