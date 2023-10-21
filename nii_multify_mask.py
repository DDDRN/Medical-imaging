# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 17:18:22 2023

@author: cattt
"""


import nibabel as nib  
import numpy as np  
import os  
  
  
# 读取第一个 NIfTI 图像  
nii1 = nib.load(os.path.join(os.getcwd(), 'mask.nii'))  
data1 = nii1.get_fdata()  
  
# 读取第二个 NIfTI 图像  
nii2 = nib.load('mask.nii')  
data2 = nii2.get_fdata()  
  
# 将两个图像逐像素对应相乘  
result = data1 * data2  
  
# 创建一个新的 NIfTI 图像对象，将结果保存为 NIfTI 文件  
nii_result = nib.Nifti1Image(result, nii1.affine)  
nib.save(nii_result, 'result.nii')
