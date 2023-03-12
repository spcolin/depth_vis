import os

source_root='/home/colin/sota_depth_map/nyu/'

source_list=[
'bts_nyu_depthmap',
'adabins_nyu_depthmap',
'dpt_nyu_depthmap',
'dpd_nyu_old',
'nyu_test_depth',
'test_rgb'
]

target_root='/home/colin/about_dpd/pic/benchmark_pic/nyu/'

target_list=[
'bts',
'adabins',
'dpt',
'dpd',
'gt',
'rgb'
]


index_list=[16 ,22, 63, 91 ,93 ,115 ,117 ,158 ,171, 218	, 352, 367, 374, 401 ,596, 597]


for idx in index_list:

    for i in range(5):

        source_path=os.path.join(source_root,source_list[i])
        source_path=os.path.join(source_path,str(idx)+'.png')
        
        target_path=os.path.join(target_root,target_list[i])
        target_path=os.path.join(target_path,str(idx)+'.png')

        cmd_line='cp '+source_path+' '+target_path

        os.system(cmd_line)

    source_path=os.path.join(source_root,source_list[-1])
    source_path=os.path.join(source_path,str(idx)+'.jpg')

    target_path=os.path.join(target_root,target_list[-1])
    target_path=os.path.join(target_path,str(idx)+'.jpg')

    cmd_line='cp '+source_path+' '+target_path

    os.system(cmd_line)

    # break









