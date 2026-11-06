from charlib import *
chars={}
# RAB PIBROCH - piper: glengarry, black jacket, red kilt, white sporran, bagpipe drones
rab=dict(
hd=["....KKKKKKKK....","...KNNXwXwNNK...","...KNNNNNNNNK...","...KRSSSSSSRK...","...KSSSSSSSSK...","...KSKSSSSKSK...","...KSSSFFSSSK...","...KSRRRRRRSK...","....KSSSSSSK....","................"],
td=["..KKNNwwwwNNKK..",".KNNNNwwwwNNNNK.",".KNNNLNwwNLNNNK.",".KNNNNNNNNNNNNK.",".KSNNNLwwLNNNSK.","..KXXXwwwwXXXK..","..KXxXwwwwXxXK..","..KxXXXwwXXXxK..","..KXXxXXXXxXXK.."],
hu=["....KKKKKKKK....","...KNNNNNNNNK...","...KNNNNNNNNK...","...KRRRRRRRRK...","...KRRRRRRRRK...","...KRRRRRRRRK...","...KRRRRRRRRK...","...KSRRRRRRSK...","....KSSSSSSK....","................"],
tu=["..KKNNNNNNNNKK..",".KNNNNNNNNNNNNK.",".KNNNNNNNNNNNNK.",".KNNNNNNNNNNNNK.",".KSNNNNNNNNNNSK.","..KXXxXXxXXxXK..","..KXxXXxXXxXXK..","..KxXXxXXxXXxK..","..KXXxXXxXXxXK.."],
hl=["....KKKKKKK.....","...KNXwXwNNK....","...KNNNNNNNK....","...KSSSRRRRK....","..KSSSSSRRRK....","..KSKSSSSRRK....","..KFSSSSSSRK....","...KRRSSSSK.....","....KSSSSK......","................"],
tl=["....KNNNNNNK....","...KNNNNNNNNK...","...KNNNNKNNNK...","...KNLNNKNNNK...","...KNNNNKSNNK...","...KXXXwwXXXK...","....KXxXXxXK....","....KxXXxXXK....","....KXXxXXxK...."],
)
rab.update(legs('w'))
# drones: overlay later
# KENNY COLLIE - shepherd: flat cap, waxed olive jacket, grey stubble, crook
kenny=dict(
hd=["....KKKKKKKK....","...KAAAAAAAAK...","..KaAAAAAAAAaK..","...KHSSSSSSHK...","...KSSSSSSSSK...","...KSKSSSSKSK...","...KSSSFSSSSK...","...KqSSSSSSqK...","....KqqqqqqK....","................"],
td=["..KKOOwwwwOOKK..",".KOOOOwwwwOOOOK.",".KOOOOOOOOOOOOK.",".KOOOoOOOOoOOOK.",".KSOOOOOOOOOOSK.","..KOOOOOOOOOOK..","..KoOOOOOOOOoK..","..KNNNNNNNNNNK..","..KNNNKKKKNNNK.."],
hu=["....KKKKKKKK....","...KAAAAAAAAK...","..KaAAAAAAAAaK..","...KHHHHHHHHK...","...KHHHHHHHHK...","...KHHHHHHHHK...","...KHHHHHHHHK...","...KSHHHHHHSK...","....KSSSSSSK....","................"],
tu=["..KKOOOOOOOOKK..",".KOOOOOOOOOOOOK.",".KOOOOOOOOOOOOK.",".KOOOOOOOOOOOOK.",".KSOOOOOOOOOOSK.","..KOOOOOOOOOOK..","..KoOOOOOOOOoK..","..KNNNNNNNNNNK..","..KNNNKKKKNNNK.."],
hl=["....KKKKKKK.....","...KAAAAAAAK....",".KKaAAAAAAAK....","...KSSSHHHHK....","..KSSSSSHHHK....","..KSKSSSSHHK....","..KSSSSSSSHK....","...KqqSSSSK.....","....KqqqqK......","................"],
tl=["....KOwOOOOK....","...KOOwOOOOOK...","...KOOOOKOOOK...","...KOOOOKOOOK...","...KOOOOKSOOK...","...KOOOOOOOOK...","...KoOOOOOOoK...","....KNNNNNNK....","....KNNNNNNK...."],
)
kenny.update(legs('N','U'))
# MALCOLM SMIDDY - blacksmith: bald, big black beard, leather apron, bare arms
malc=dict(
hd=["................","....KKKKKKKK....","...KSSSSSSSSK...","...KSSSSSSSSK...","...KSSSSSSSSK...","...KSKSSSSKSK...","...KHSSFFSSHK...","...KHHHSSHHHK...","...KHHHHHHHHK...","....KHHHHHHK...."],
td=[".KKKqqHHHHqqKKK.","KSSKqqqHHqqqKSSK","KSSKaAAAAAAaKSSK","KSSKaAAAAAAaKSSK",".KSKaAAccAAaKSK.","..KKaAAAAAAaKK..","..KNaAAAAAAaNK..","..KNaAAAAAAaNK..","...KaaaaaaaaK..."],
hu=["................","....KKKKKKKK....","...KSSSSSSSSK...","...KSSSSSSSSK...","...KSSSSSSSSK...","...KSSSSSSSSK...","...KHSSSSSSHK...","...KHSSSSSSHK...","...KSSSSSSSSK...","....KSSSSSSK...."],
tu=[".KKKqqqqqqqqKKK.","KSSKqqqqqqqqKSSK","KSSKqqaqqaqqKSSK","KSSKqqqaaqqqKSSK",".KSKqqqaaqqqKSK.","..KKqqaqqaqqKK..","..KNNNNNNNNNNK..","..KNNNNNNNNNNK..","...KNNNNNNNNK..."],
hl=["................","....KKKKKKK.....","...KSSSSSSSK....","...KSSSSSSSK....","..KSSSSSSSSK....","..KSKSSSSSSK....","..KFSSSSSHHK....","..KHHHSSHHK.....","...KHHHHHHK.....","....KHHHHK......"],
tl=["....KqqHHqqK....","...KAAqqqqqqK...","..KAAAqqKSSqK...","..KAAAAqKSSqK...","..KAAAAqKSSqK...","..KAAAAqqqqqK...","..KAAAANNNNK....","...KAAANNNNK....","....KaaNNNNK...."],
)
malc.update(legs('N'))
# RORY GHILLIE - gamekeeper: tweed deerstalker, tweed jacket, plus-fours, long green socks
rory=dict(
hd=["....KKKKKKKK....","...KTtTtTtTtK...","..KTTTTTTTTTTK..","...KRSSSSSSRK...","...KSSSSSSSSK...","...KSKSSSSKSK...","...KSSSFSSSSK...","...KSSRRRRSSK...","....KSSSSSSK....","................"],
td=["..KKTTwwwwTTKK..",".KTTTTwVVwTTTTK.",".KTtTTTwwTTTtTK.",".KTTTtTTTTtTTTK.",".KSTTTTTTTTTTSK.","..KTtTTTTTTtTK..","..KAAAAAAAAAAK..","..KAAAAAAAAAAK..","..KAAAKKKKAAAK.."],
hu=["....KKKKKKKK....","...KTtTtTtTtK...","..KTTTTTTTTTTK..","...KRRRRRRRRK...","...KRRRRRRRRK...","...KRRRRRRRRK...","...KRRRRRRRRK...","...KSRRRRRRSK...","....KSSSSSSK....","................"],
tu=["..KKTTTTTTTTKK..",".KTTTTTTTTTTTTK.",".KTtTTTTTTTTtTK.",".KTTTtTTTTtTTTK.",".KSTTTTTTTTTTSK.","..KTtTTTTTTtTK..","..KAAAAAAAAAAK..","..KAAAAAAAAAAK..","..KAAAKKKKAAAK.."],
hl=["....KKKKKKK.....","...KTtTtTtTK....","..KTTTTTTTTTKK..","...KSSSRRRRK....","..KSSSSSRRRK....","..KSKSSSSRRK....","..KFSSSSSSRK....","...KSRRRSSK.....","....KSSSSK......","................"],
tl=["....KTwTTTTK....","...KTTwTTTTTK...","...KTtTTKTTTK...","...KTTTtKTTTK...","...KTTTTKSTTK...","...KTtTTTTtTK...","....KAAAAAAK....","....KAAAAAAK....","....KAAAAAAK...."],
)
rory.update(legs('V','c'))
# OLD BRIDIE - tiny old woman: white bun, green tartan shawl, long dark skirt
brid=dict(
hd=["................","................","......KKKK......",".....KwwwwK.....","....KwwwwwwK....","...KwSSSSSSwK...","...KSKSSSSKSK...","...KSsSFFSsSK...","....KSSssSSK....","................"],
td=["..KKVVVVVVVVKK..",".KVVXVVXVVXVVVK.",".KVXXXVXXXVXXVK.",".KSVVXVVXVVXVSK.","..KVVVVVVVVVVK..","..KNNNNNNNNNNK..","..KNNNNNNNNNNK..","..KNNNNNNNNNNK..","..KNNNNNNNNNNK.."],
hu=["................","................","......KKKK......",".....KwwwwK.....","....KwwwwwwK....","...KwwwwwwwwK...","...KwwwwwwwwK...","...KSwwwwwwSK...","....KSSSSSSK....","................"],
tu=["..KKVVVVVVVVKK..",".KVVXVVXVVXVVVK.",".KVXXXVXXXVXXVK.",".KVVVXVVXVVXVVK.","..KVVVVVVVVVVK..","..KNNNNNNNNNNK..","..KNNNNNNNNNNK..","..KNNNNNNNNNNK..","..KNNNNNNNNNNK.."],
hl=["................","................","........KKK.....",".......KwwwK....","....KKKwwwwK....","...KSSSSwwwK....","..KSKSSSSwwK....","..KFsSSSSSwK....","...KSSssSK......","................"],
tl=["....KVVVVVVK....","...KVXVVXVVVK...","...KVXXVKXXVK...","...KSVVVKVVVK...","....KVVVVVVK....","....KNNNNNNK....","....KNNNNNNK....","....KNNNNNNK....","....KNNNNNNK...."],
)
brid.update(dict(ls=["...KNNNNNNNNK...","....KNNNNNNK....","....KKK..KKK....","................","................"],
 l1=["...KNNNNNNNNK...","....KNNNNNNK....","....KKK.........","................","................"],
 l2=["...KNNNNNNNNK...","....KNNNNNNK....",".........KKK....","................","................"],
 sls=["....KNNNNNNK....",".....KNNNNK.....",".....KKKK.......","................","................"],
 sl1=["....KNNNNNNK....",".....KNNNNK.....","....KK...KK.....","................","................"]))
sheets={}
for n,c in (('rab',rab),('kenny',kenny),('malcolm',malc),('rory',rory),('bridie',brid)):
    sheets[n]=build(n,c)
# extras: bagpipe drones for rab (front/side), crook for kenny, stick for bridie
from PIL import ImageDraw
def put(im,pts,col):
    for x,y in pts:
        if 0<=x<im.width and 0<=y<im.height: im.putpixel((x,y),col+(255,))
r=sheets['rab']
for ci in range(3):
    for ri,dx in ((0,12),(1,10),(2,4),(3,3)):
        ox,oy=ci*16,ri*24
        for k,(x0,top) in enumerate(((dx,1),(dx+1,3),(dx+2,5))):
            put(r,[(ox+x0,oy+top+j) for j in range(9)],PAL['c']); put(r,[(ox+x0,oy+top)],PAL['w'])
        put(r,[(ox+dx+i,oy+11) for i in range(3)],PAL['X'])
r.save('rab_sheet.png')
k=sheets['kenny']
for ci in range(3):
    for ri,x in ((0,14),(1,2),(2,13),(3,1)):
        ox,oy=ci*16,ri*24
        put(k,[(ox+x,oy+j) for j in range(3,22)],PAL['c'])
        hx=x-1 if ri in (0,2) else x+1
        put(k,[(ox+x,oy+2),(ox+hx,oy+1),(ox+hx+(hx-x),oy+2)],PAL['c'])
k.save('kenny_sheet.png')
b=sheets['bridie']
for ci in range(3):
    for ri,x in ((0,13),(1,2),(2,13),(3,2)):
        ox,oy=ci*16,ri*24
        put(b,[(ox+x,oy+j) for j in range(12,22)],PAL['C'])
        put(b,[(ox+x,oy+11),(ox+x+(1 if ri!=1 else -1),oy+11)],PAL['c'])
b.save('bridie_sheet.png')
names=['rab','kenny','malcolm','rory','bridie']
W=56*5
cv=Image.new('RGBA',(W,96),(0,0,0,0))
for i,n in enumerate(names): cv.alpha_composite(Image.open(f'{n}_sheet.png'),(i*56,0))
big=cv.resize((W*5,96*5),Image.NEAREST); bg=Image.new('RGBA',big.size,(122,154,79,255)); bg.alpha_composite(big); bg.save('villagers3_preview.png')
