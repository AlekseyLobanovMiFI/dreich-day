from lib import *
def kirk():
    W,H=80,112; im=new(W,H)
    # bell tower (left)
    tx,tw=6,22
    rect(im,tx,24,tw,84,'sm'); stone_wall(im,tx,24,tw,84,base='hi',mortar='sl',seed=3); outline(im,tx-1,23,tw+2,86)
    # spire roof
    for k in range(22):
        y=2+k; half=k//2+1
        for i in range(tx+tw//2-half,tx+tw//2+half): px(im,i,y,'ro' if i<tx+tw//2 else 'rod')
        px(im,tx+tw//2-half-1,y,'K'); px(im,tx+tw//2+half,y,'K')
    px(im,tx+tw//2-1,0,'K'); px(im,tx+tw//2,0,'K'); rect(im,tx+tw//2-1,1,2,2,'warm')
    # belfry opening with bell
    rect(im,tx+6,30,10,12,'K'); ellipse(im,tx+11,37,3,3,'warm','warmd'); px(im,tx+11,41,'warmd')
    # clock-ish round window
    ellipse(im,tx+11,54,3,3,'warm')
    # nave
    nx=28
    slate_roof(im,nx,40,48,30)
    stone_wall(im,nx,71,48,37,base='hi',mortar='sl',seed=9); outline(im,nx-1,70,50,39)
    rect(im,nx,106,48,2,'sd')
    # gothic windows
    for wx in (nx+6,nx+34):
        rect(im,wx,78,8,14,'K'); rect(im,wx+1,80,6,11,'warm')
        px(im,wx+1,80,'K'); px(im,wx+6,80,'K'); px(im,wx+1,79,'K')
        for j in range(80,91): px(im,wx+4,j,'warmd')
        rect(im,wx+1,85,6,1,'warmd')
    # arched door
    rect(im,nx+19,88,12,20,'K'); rect(im,nx+20,90,10,18,'wood')
    px(im,nx+20,90,'K'); px(im,nx+29,90,'K')
    for i in range(nx+22,nx+30,3):
        for j in range(90,108): px(im,i,j,'woodd')
    px(im,nx+28,99,'warm')
    # celtic cross on gable
    rect(im,nx+24,30,2,10,'K'); rect(im,nx+21,33,8,2,'K'); outline(im,nx+22,32,6,4,'K')
    return im
def hut():
    W,H=64,64; im=new(W,H)
    slate_roof(im,6,10,52,22)
    rect(im,24,18,8,5,'sm'); outline(im,24,18,8,5,'sd')  # patch
    chimney(im,46,2,10)
    rect(im,6,33,52,28,'wood')
    for j in range(33,61,4):
        for i in range(6,58): px(im,i,j,'woodd')
    outline(im,5,32,54,30)
    window(im,12,38,9,8); door(im,30,46,9,14)
    # crossed camans
    for k in range(12):
        px(im,44+k,36+k,'woodl'); px(im,55-k,36+k,'woodl')
    rect(im,42,47,3,2,'woodl'); rect(im,55,47,3,2,'woodl')
    # washing line with green jersey
    # jersey on line outside right? place under eaves left
    return im
def hut_full():
    im=new(80,64); h=hut(); im.alpha_composite(h,(0,0))
    # clothes line to the right with jersey
    rect(im,66,30,1,32,'K'); rect(im,78,30,1,32,'K')
    for i in range(66,79): px(im,i,31,'mistd')
    rect(im,68,32,9,8,'green'); rect(im,66,32,2,3,'green'); rect(im,77,32,2,3,'green')
    rect(im,68,35,9,1,'warm'); outline(im,67,32,11,9)
    # ball/bucket
    rect(im,60,56,5,5,'sd'); outline(im,59,55,7,7)
    return im
def goal():
    W,H=40,28; im=new(W,H)
    rect(im,2,4,36,20,'mist')
    for j in range(4,24,2):
        for i in range(2,38,2): px(im,i,j,'mistd')
    outline(im,1,3,38,22,'K')
    rect(im,1,3,2,25,'white'); rect(im,37,3,2,25,'white'); rect(im,1,3,38,2,'white')
    outline(im,0,2,40,26,'K')
    return im
k=kirk(); k.save('kirk.png'); h=hut_full(); h.save('dougie_hut.png'); g=goal(); g.save('shinty_goal.png')
cv=Image.new('RGBA',(80+80+40+40,120),C['grass']+(255,))
cv.alpha_composite(k,(4,4)); cv.alpha_composite(h,(92,56)); cv.alpha_composite(g,(186,90))
cv.resize((cv.width*4,cv.height*4),Image.NEAREST).save('newbuild_preview.png')
