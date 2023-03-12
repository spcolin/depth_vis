import numpy as np
import matplotlib.pyplot as plt
import os



npy_path='/home/colin/sota_depth_npy/nyu/bts_nyu_depth.npy'

save_root='/home/colin/sota_depth_map/nyu/bts_nyu_depthmap/'

if not os.path.exists(save_root):

    os.makedirs(save_root)

depth_npy=np.load(npy_path)

print(type(depth_npy))
print(depth_npy.shape)


for idx in range(len(depth_npy)):

    print(idx)

    depth=depth_npy[idx]

    depth=depth[45:471,41:601]

    save_path=os.path.join(save_root,str(idx)+'.png')

    plt.imsave(save_path,depth,cmap='jet')

    # break
