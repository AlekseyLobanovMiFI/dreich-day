from PIL import Image
PAL={'.':None,'K':(43,42,51),'S':(232,194,160),'s':(201,157,126),'F':(214,124,104),
'H':(58,46,42),'R':(181,86,46),'r':(138,63,34),'Q':(190,190,186),'q':(150,150,146),'w':(230,232,228),
'X':(163,59,59),'x':(122,43,43),'V':(78,107,58),'v':(59,82,48),'N':(52,52,62),'n':(70,70,82),
'T':(110,98,80),'t':(85,75,61),'C':(138,111,78),'c':(107,84,64),'L':(242,185,94),'G':(130,136,148),
'O':(96,104,64),'o':(74,82,50),'A':(150,110,70),'a':(118,84,52),'D':(142,106,158),'M':(62,92,112),'U':(46,70,40)}
def chk(name,rows,n=24):
    rows=rows+["."*16]*(n-len(rows))
    assert len(rows)==n,(name,len(rows))
    for r in rows: assert len(r)==16,(name,r,len(r))
    return rows
def build(name,c):
    D=lambda h,t,l: chk(name,c[h]+c[t]+c[l])
    rows={'down':[D('hd','td','ls'),D('hd','td','l1'),D('hd','td','l2')],
     'up':[D('hu','tu','ls'),D('hu','tu','l2'),D('hu','tu','l1')],
     'left':[D('hl','tl','sls'),D('hl','tl','sl1'),D('hl','tl','sls')]}
    rows['right']=[[r[::-1] for r in f] for f in rows['left']]
    sheet=Image.new('RGBA',(48,96),(0,0,0,0))
    for ri,d in enumerate(['down','left','right','up']):
        for ci,f in enumerate(rows[d]):
            for y,r in enumerate(f):
                for x,ch in enumerate(r):
                    col=PAL[ch]
                    if col: sheet.putpixel((ci*16+x,ri*24+y),col+(255,))
    sheet.save(f'{name}_sheet.png'); return sheet
def legs(fill,shoe='K'):
    f,s=fill,shoe
    return dict(
    ls=[f"....K{f}{f}KK{f}{f}K....",f"....K{f}{f}KK{f}{f}K....",f"....K{s}{s}KK{s}{s}K....","....KKKKKKKK....","................"],
    l1=[f"....K{f}{f}KK{f}{f}K....",f"....K{f}{f}KK{f}{f}K....",f"....K{s}{s}K.KKK....","....KKKK........","................"],
    l2=[f"....K{f}{f}KK{f}{f}K....",f"....K{f}{f}KK{f}{f}K....",f"....KKK.K{s}{s}K....","........KKKK....","................"],
    sls=[f".....K{f}{f}{f}K......",f".....K{f}{f}{f}K......",f".....K{s}{s}{s}K......","....KKKKKK......","................"],
    sl1=[f"....K{f}{f}K{f}{f}K.....",f"...K{f}{f}K.K{f}{f}K....",f"...K{s}K...K{s}K....","..KKKK...KKK....","................"])
