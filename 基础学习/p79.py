#function: 更改图片尺寸大小
import os
import os.path
from PIL import Image
'''
filein: 输入图片
fileout: 输出图片
width: 输出图片宽度
height:输出图片高度
type:输出图片类型（png, gif, jpeg...）
'''
def ResizeImage(filein, fileout, width, height, type):
    img = Image.open(filein)
    out = img.resize((width, height),Image.ANTIALIAS) #resize image with high-quality
    out.save(fileout, type)
if __name__ == "__main__":
	count=1
	os.chdir('C:\\Users\\Administrator\\Pictures')
	for filein in os.listdir(os.getcwd()):
		if filein.endswith('png'):
		    fileout = 'testout_%d.png'%(count)
		    width = 540
		    height = 270
		    type = 'png'
		    count+=1
		    ResizeImage(filein, fileout, width, height, type)
