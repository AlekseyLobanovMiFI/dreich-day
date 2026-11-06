from PIL import Image
import random, math
C=dict(K=(43,42,51),sd=(74,78,87),sl=(140,143,148),sm=(112,116,122),hi=(170,173,176),
 ro=(91,102,114),rod=(70,79,90),roh=(118,129,140),wood=(138,111,78),woodd=(107,84,64),woodl=(165,136,98),
 warm=(242,185,94),warmd=(201,140,62),red=(163,59,59),redd=(122,43,43),mist=(214,214,206),mistd=(180,182,178),
 grass=(122,154,79),grassd=(78,107,58),heather=(142,106,158),heatherd=(110,80,128),
 thatch=(176,140,84),thatchd=(138,104,60),thatchl=(204,172,112),water=(62,92,112),dirt=(138,111,78),
 silver=(170,176,186),silverd=(130,136,148),white=(230,232,228),green=(78,107,58),greend=(59,82,48),moss=(122,154,79))
def new(w,h): return Image.new('RGBA',(w,h),(0,0,0,0))
def px(im,x,y,c):
    if 0<=x<im.width and 0<=y<im.height: im.putpixel((x,y),C[c]+(255,))
def rect(im,x,y,w,h,c):
    for i in range(x,x+w):
        for j in range(y,y+h): px(im,i,j,c)
def outline(im,x,y,w,h,c='K'):
    for i in range(x,x+w): px(im,i,y,c); px(im,i,y+h-1,c)
    for j in range(y,y+h): px(im,x,j,c); px(im,x+w-1,j,c)
def stone_wall(im,x,y,w,h,base='sl',mortar='sm',seed=1):
    rect(im,x,y,w,h,mortar); random.seed(seed); row=y
    while row<y+h:
        rh=random.choice([3,4]); col=x+random.randint(-3,0)
        while col<x+w:
            sw=random.randint(4,7)
            for i in range(max(col,x),min(col+sw-1,x+w)):
                for j in range(row,min(row+rh-1,y+h)): px(im,i,j,base)
            if x<=col<x+w: px(im,col,row,'hi')
            col+=sw
        row+=rh
def slate_roof(im,x,y,w,h):
    x-=2; w+=4; rect(im,x,y,w,h,'ro')
    for j in range(y+2,y+h,3):
        for i in range(x,x+w): px(im,i,j,'rod')
        off=((j-y)//3)%2*3
        for i in range(x+off,x+w,6): px(im,i,j-1,'rod'); px(im,i,j-2,'rod')
    for i in range(x,x+w): px(im,i,y,'roh')
    outline(im,x-1,y-1,w+2,h+2)
def window(im,x,y,w=8,h=8,mull='warmd'):
    rect(im,x,y,w,h,'K'); rect(im,x+1,y+1,w-2,h-2,'warm')
    for j in range(y+1,y+h-1): px(im,x+w//2,j,mull)
    for i in range(x+1,x+w-1): px(im,i,y+h//2,mull)
    rect(im,x-1,y+h,w+2,1,'hi')
def door(im,x,y,w=8,h=12):
    rect(im,x-1,y-1,w+2,h+1,'K'); rect(im,x,y,w,h,'wood')
    for i in range(x+2,x+w,3):
        for j in range(y,y+h): px(im,i,j,'woodd')
    px(im,x+w-2,y+h//2,'warm')
def chimney(im,x,y,h=10):
    rect(im,x,y,6,h,'sl'); outline(im,x,y,6,h); rect(im,x+1,y+1,4,1,'K')
def ellipse(im,cx,cy,rx,ry,c,oc='K'):
    for i in range(int(cx-rx)-1,int(cx+rx)+2):
        for j in range(int(cy-ry)-1,int(cy+ry)+2):
            d=((i-cx)/rx)**2+((j-cy)/ry)**2
            if d<=1: px(im,i,j,c)
            elif d<=1.35 and oc: px(im,i,j,oc)
