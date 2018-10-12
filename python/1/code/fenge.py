from PIL import Image
img=Image.open(r'h.jpg')
size=img.size
h=size[1]/3
w=size[0]/3
n=3
k=1
for i in range(n):
    for j in range(n):       
        a=img.crop((i*w,j*h,(i+1)*w,(j+1)*h))       
        a.save(str(k)+'.png')
        k+=1
