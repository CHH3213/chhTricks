from PIL import  Image
import os

"""
使用PIL库批量修改图片为固定大小
"""

path="../../../../../研究生生活/2023.02旅游视频制作/0.漫威片头制作/素材"  #图片所在的文件夹路径
path_new="../../../../../研究生生活/2023.02旅游视频制作/0.漫威片头制作/素材统一尺寸"  #图片所在的文件夹路径
for maindir, subdir,file_name_list in os.walk(path):
    print(file_name_list)
    for file_name in file_name_list:
        image=os.path.join(maindir,file_name) #获取每张图片的路径
        file=Image.open(image)
        out=file.resize((1920,1080),Image.ANTIALIAS)  #以高质量修改图片尺寸为(1920,1080)
        out.save(image)                            #以同名保存到原路径