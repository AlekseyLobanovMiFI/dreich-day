from charlib import *
PAL.update({'B':(48,58,92),'b':(36,44,72),'Y':(214,180,110),'y':(170,140,80)})
r=dict(
hd=["................",".....KKKKKK.....","....KYYYYYYK....","...KYYYYYYYYK...","...KYSSSSSYYK...","...KSSSSSSSSK...","...KSKSSSSKSK...","...KSSSFSSSSK...","...KSSKKKKSSK...","....KSSSSSSK...."],
td=["..KKBBwXXwBBKK..",".KBBBBwXXwBBBBK.",".KBBBBBXXBBBBBK.",".KBBBBBXXBBBBBK.",".KSBBBBBBBBBBSK.","..KBBBBBBBBBBK..","..KbBBBBBBBBbK..","..KBBBBBBBBBBK..","..KBBBKKKKBBBK.."],
hu=["................",".....KKKKKK.....","....KYYYYYYK....","...KYYYYYYYYK...","...KYYYYYYYYK...","...KYYYYYYYYK...","...KYYYYYYYYK...","...KSYYYYYYSK...","...KSSSSSSSSK...","....KSSSSSSK...."],
tu=["..KKBBBBBBBBKK..",".KBBBBBBBBBBBBK.",".KBBBBBBBBBBBBK.",".KBBBBBBBBBBBBK.",".KSBBBBBBBBBBSK.","..KBBBBBBBBBBK..","..KbBBBBbBBBbK..","..KBBBBBbBBBBK..","..KBBBKKKKBBBK.."],
hl=["................",".....KKKKKK.....","....KYYYYYYK....","...KYYYYYYYK....","...KSSSYYYYK....","..KSSSSSYYYK....","..KSKSSSSYYK....","..KSSSSSSSSK....","...KKKSSSSK.....","....KSSSSK......"],
tl=[".....KwBBBK.....","....KXwBBBBK....","...KBXBBKBBBK...","...KBBBBKBBBK...","...KBBBBKSBBK...","...KBBBBBBBBK...","...KbBBBBBBbK...","....KBBBBBBK....","....KBBBBBBK...."],
)
r.update(legs('B','K'))
s=build('rupert',r)
from PIL import Image
def put(im,pts,col):
    for x,y in pts: im.putpixel((x,y),col+(255,))
br=(92,62,40)
for ci in range(3):
    for ri,x0 in ((0,12),(3,1)):
        ox,oy=ci*16,ri*24
        for i in range(4):
            for j in range(4): put(s,[(ox+x0+i,oy+14+j)],br)
        put(s,[(ox+x0+1,oy+13),(ox+x0+2,oy+13)],(43,42,51))
s.save('rupert_sheet.png')
big=s.resize((48*6,96*6),Image.NEAREST); bg=Image.new('RGBA',big.size,(122,154,79,255)); bg.alpha_composite(big); bg.save('rupert_preview.png')
