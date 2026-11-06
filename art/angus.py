from lib import *
PAL={'.':None,'K':C['K'],'H':(58,46,42),'S':(232,194,160),'s':(201,157,126),'F':(214,124,104),
'Y':C['silver'],'y':C['silverd'],'L':C['warm'],'N':(52,52,62)}
def chk(rows,n=24):
    rows=rows+["."*16]*(n-len(rows)); assert len(rows)==n
    for r in rows: assert len(r)==16,(r,len(r))
    return rows
c=dict(
hd=["................",".....KKKKKK.....","....KHHHHHHK....","...KHHHHHHHHK...","...KHHSSSSHHK...","...KSSSSSSSSK...","...KSKSSSSKSK...","...KSSSSSSSSK...","...KSSSKKSSSK...","....KSSSSSSK...."],
td=["..KKYYLLLLYYKK..",".KSYYYYYYYYYYSK.",".KSYYYYLLYYYYSK.",".KSYYYLLLLYYYSK.",".KSYYYYLLYYYYSK.","..KYYYYYYYYYYK..","..KNNNNNNNNNNK..","..KNNNNNNNNNNK..","...KSSKKKKSSK..."],
ls=["....KYYKKYYK....","....KyyKKyyK....","....KYYKKYYK....","....KKKKKKKK....","................"],
l1=["....KYYKKYYK....","....KyyKKyyK....","....KYYK.KKK....","....KKKK........","................"],
l2=["....KYYKKYYK....","....KyyKKyyK....","....KKK.KYYK....","........KKKK....","................"],
hu=["................",".....KKKKKK.....","....KHHHHHHK....","...KHHHHHHHHK...","...KHHHHHHHHK...","...KHHHHHHHHK...","...KHHHHHHHHK...","...KSHHHHHHSK...","...KSSSSSSSSK...","....KSSSSSSK...."],
tu=["..KKYYYYYYYYKK..",".KSYYYYYYYYYYSK.",".KSYYYYLLLYYYSK.",".KSYYYYYYLYYYSK.",".KSYYYYYLYYYYSK.","..KYYYYLYYYYYK..","..KNNNNNNNNNNK..","..KNNNNNNNNNNK..","...KSSKKKKSSK..."],
hl=["................",".....KKKKKK.....","....KHHHHHHK....","...KHHHHHHHK....","...KSSSHHHHK....","..KSSSSSHHHK....","..KSKSSSSHHK....","..KSSSSSSSSK....","...KKSSSSSK.....","....KSSSSK......"],
tl=[".....KYYLYK.....","....KYYYYYYK....","...KYYYYKYYYK...","...KYLYYKYYYK...","...KYYYYKSYYK...","...KYYYYYYYYK...","....KNNNNNNK....","....KNNNNNNK....",".....KSKKSK....."],
sls=[".....KYYYK......",".....KyyyK......",".....KYYYK......","....KKKKKK......","................"],
sl1=["....KYYKYYK.....","...KyyK.KyyK....","...KYK...KYK....","..KKKK...KKK....","................"],
)
D=lambda h,t,l: chk(c[h]+c[t]+c[l])
rows={'down':[D('hd','td','ls'),D('hd','td','l1'),D('hd','td','l2')],
'up':[D('hu','tu','ls'),D('hu','tu','l2'),D('hu','tu','l1')],
'left':[D('hl','tl','sls'),D('hl','tl','sl1'),D('hl','tl','sls')]}
rows['right']=[[r[::-1] for r in f] for f in rows['left']]
sheet=new(48,96)
for ri,d in enumerate(['down','left','right','up']):
    for ci,f in enumerate(rows[d]):
        for y,r in enumerate(f):
            for x,ch in enumerate(r):
                col=PAL[ch]
                if col: sheet.putpixel((ci*16+x,ri*24+y),col+(255,))
sheet.save('angus_sheet.png')
big=sheet.resize((48*6,96*6),Image.NEAREST); bg=Image.new('RGBA',big.size,C['grass']+(255,)); bg.alpha_composite(big); bg.save('angus_preview.png')
