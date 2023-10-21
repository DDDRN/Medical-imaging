  
import nibabel as nib  
from PIL import Image  
import numpy as np  
import os  
  
# 指定 PNG 图像所在的文件夹路径  
png_folder = r'D:\\BaiduSyncdisk\\4-luguboli\\U-2-Net-master\\jpg2nii\\jpg\\'
  
# 获取文件夹中所有的 PNG 图像文件名  
png_files = [f for f in os.listdir(png_folder) if f.endswith('.jpg')]  
# 将文件名重新排序，避免出现1,10,2,20排序的情况
png_files.sort(key=lambda x:int(x.split('.')[0]))
  
# 确定图像大小和通道数  
img_shape = None  
img_channels = None  
for f in png_files:  
    img = Image.open(png_folder + f)  
    if img_shape is None:  
        img_shape = img.size  
    if img_channels is None:  
        img_channels = img.mode  
    if img_shape != img.size or img_channels != img.mode:  
        raise ValueError("All images must have the same size and number of channels.")  
  
# 创建一个空的 numpy 数组，用于存储所有 PNG 图像的数据  
img_data = np.zeros(img_shape + (len(png_files),), dtype=np.uint8)  
  
# 读取所有 PNG 图像并将其数据存储到 numpy 数组中  
for i, f in enumerate(png_files):  
    img = Image.open(png_folder + f)  
    img_array = np.array(img.rotate(-90,expand=1))  
    img_data[:,:,i] = img_array[:,:,0]

# 二值化，消除边缘模糊
img_data[img_data < 128] = 0
img_data[img_data > 128] = 255

  
# 创建一个新的 NIfTI 图像对象，将 numpy 数组作为数据传递给该对象  
nii_img = nib.Nifti1Image(img_data, np.eye(4))  
  
# # 确定 NIfTI 图像的数据类型  
# if img_channels == 'L':  
#     data_type = np.uint8  
# else:  
#     data_type = np.uint8 if img_channels == 'RGB' else np.uint16  
  
# # 创建一个新的 NIfTI 图像对象，将 numpy 数组作为数据传递给该对象  
# img_data = np.transpose(img_data, axes=(1,0,2)) 
# img_data = np.transpose(img_data, axes=(1,0,2)) 
# nii_img = nib.Nifti1Image(img_data.astype(data_type), np.eye(4))  
  
# 保存 NIfTI 图像  
nib.save(nii_img, 'output.nii')