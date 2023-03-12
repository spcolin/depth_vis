import os

file_path='/home/colin/code/bts_kitti/train_test_inputs/eigen_test_files_with_gt.txt'

test_file=open(file_path)

files=test_file.readlines()

test_file.close()

source_root='/media/colin/colinSSD/kitti/'

target_root='/home/colin/sota_depth_map/kitti/test_rgb/'

file_count=len(files)

for i in range(file_count):
    print(i)


    line=files[i]

    rgb_path=line.split()[0]

    source_path=os.path.join(source_root,rgb_path)

    target_path=os.path.join(target_root,str(i)+'.png')

    cmd_line='cp '+source_path+' '+target_path

    # print(cmd_line)

    os.system(cmd_line)

    # break
