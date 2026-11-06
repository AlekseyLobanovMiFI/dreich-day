from lib import *
C.update(dict(fire=(232,110,52),fire2=(246,190,80),thatch=(176,140,84),thatchd=(138,104,60),thatchl=(204,172,112)))
def thatch_roof(im,x,y,w,h,seed=3):
    x-=3; w+=6; h+=2; rect(im,x,y,w,h,'thatch'); random.seed(seed)
    for i in range(x,x+w):
        for j in range(y,y+h):
            r=random.random()
            if r<0.18: px(im,i,j,'thatchd')
            elif r<0.28: px(im,i,j,'thatchl')
    for i in range(x,x+w): px(im,i,y+h-1,'thatchd')
    outline(im,x-1,y-1,w+2,h+2)
def smithy():
    im=new(64,64)
    chimney(im,46,0,14)
    for (a,b) in ((47,0),(49,1)): px(im,a,b,'mistd')
    slate_roof(im,4,12,56,20)
    stone_wall(im,4,33,56,28,base='sm',mortar='sd',seed=21); outline(im,3,32,58,30)
    # open forge front
    rect(im,8,38,26,22,'K'); rect(im,9,39,24,21,'sd')
    rect(im,12,46,10,8,'K'); 
    for i in range(13,21):
        for j in range(47,53): px(im,i,j,'fire' if (i+j)%3 else 'fire2')
    # anvil
    rect(im,24,52,8,3,'sl'); rect(im,26,55,4,4,'sl'); outline(im,23,51,10,5); outline(im,25,55,6,5)
    # door
    door(im,42,46,9,14)
    # horseshoe sign
    rect(im,40,36,12,8,'woodd'); outline(im,39,35,14,10)
    for (a,b) in ((43,38),(43,39),(43,40),(44,41),(45,41),(46,41),(47,40),(47,39),(47,38)): px(im,a,b,'hi')
    return im
def lodge():
    im=new(64,64)
    slate_roof(im,4,10,56,22)
    rect(im,4,33,56,28,'woodd')
    for j in range(33,61,4):
        for i in range(4,60): px(im,i,j,'K' if j%8==1 else 'wood')
    for j in range(33,61):
        for i in range(4,60):
            if (j-33)%4 in (1,2): px(im,i,j,'wood')
    outline(im,3,32,58,30)
    window(im,10,40,9,8); window(im,45,40,9,8)
    door(im,27,46,10,14)
    # antlers above door
    for k in range(5):
        px(im,32-k,28+ (k%2),'woodl'); px(im,32+k,28+(k%2),'woodl')
    px(im,28,26,'woodl'); px(im,36,26,'woodl'); px(im,29,27,'woodl'); px(im,35,27,'woodl')
    rect(im,31,29,3,3,'woodl')
    # log pile
    for (a,b) in ((52,54),(56,54),(54,51)): ellipse(im,a,b,2,2,'woodl')
    return im
def croft():
    im=new(64,60)
    chimney(im,6,0,12)
    thatch_roof(im,6,6,52,24,seed=8)
    rect(im,6,33,52,24,'mist')
    random.seed(4)
    for _ in range(50): px(im,random.randint(6,57),random.randint(33,56),'mistd')
    outline(im,5,32,54,26)
    window(im,12,38,8,8); door(im,28,42,9,14)
    for hx in (44,50):
        rect(im,hx,51,5,5,'woodd'); outline(im,hx,51,5,5)
        for i in range(hx,hx+5): px(im,i,50,'heather')
    return im
def sheep(flip=False):
    im=new(16,12)
    ellipse(im,8,6,5,3.5,'mist')
    for (a,b) in ((5,4),(7,3),(10,4),(8,7),(6,7)): px(im,a,b,'mistd')
    rect(im,12,4,3,4,'K'); px(im,13,5,'white') ; px(im,12,3,'K')
    for x in (5,7,10,11): rect(im,x,9,1,3,'K')
    if flip: im=im.transpose(Image.FLIP_LEFT_RIGHT)
    return im
s=smithy(); s.save('smithy.png'); l=lodge(); l.save('lodge.png'); c=croft(); c.save('bridie_croft.png')
sh=sheep(); sh.save('sheep.png')
cv=Image.new('RGBA',(64*3+16+40,70),C['grass']+(255,))
cv.alpha_composite(s,(2,2)); cv.alpha_composite(l,(68,2)); cv.alpha_composite(c,(134,6)); cv.alpha_composite(sh,(205,30)); cv.alpha_composite(sheep(True),(222,45))
cv.resize((cv.width*4,cv.height*4),Image.NEAREST).save('iter3build_preview.png')
