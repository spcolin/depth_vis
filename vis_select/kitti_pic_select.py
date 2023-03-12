import os

source_root='/home/colin/sota_depth_map/kitti/'

source_list=[
'bts_kitti_depthmap',
'adabins_kitti_depthmap',
'dpt_kitti_depthmap',
'dpd_kitti',
'test_rgb'
]

target_root='/home/colin/about_dpd/pic/benchmark_pic/kitti/'

target_list=[
'bts',
'adabins',
'dpt',
'dpd',
'rgb'
]


index_list=[80 , 210 ,419 , 585]


for idx in index_list:

    for i in range(5):

        source_path=os.path.join(source_root,source_list[i])
        source_path=os.path.join(source_path,str(idx)+'.png')
        
        target_path=os.path.join(target_root,target_list[i])
        target_path=os.path.join(target_path,str(idx)+'.png')

        cmd_line='cp '+source_path+' '+target_path

        os.system(cmd_line)


    # break









