import cv2,os
import numpy as np


display_count=697


root_list=[
'/home/colin/sota_depth_map/kitti/bts_kitti_depthmap/',
'/home/colin/sota_depth_map/kitti/adabins_kitti_depthmap/',
'/home/colin/sota_depth_map/kitti/dpt_kitti_depthmap/',
]

for i in range(585,display_count):

    img_list=[]

    img_name=str(i)+'.png'

    for k in root_list:

        img_path=os.path.join(k,img_name)

        img=cv2.imread(img_path)
        # print(img.shape)

        img=cv2.resize(img,(608,120))

        img_list.append(img)
    
    imgs=np.vstack(img_list)

    cv2.imshow('image index:'+str(i),imgs)
    cv2.waitKey(100000)
    cv2.destroyAllWindows()

    # break







