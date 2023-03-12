import os,cv2


root_path='/home/colin/sota_depth_map/kitti/test_rgb/'

save_root=''

sample_count=697


for i in range(sample_count):


    rgb_path=os.path.join(root_path,str(i)+'.png')

    img=cv2.imread(rgb_path)

    print(img.shape)

    img=img[110:,:,:]

    print(img.shape)

    cv2.imshow('1',img)
    cv2.waitKey(100000)
    break

