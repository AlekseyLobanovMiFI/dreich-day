from charlib import *
from PIL import Image
PAL.update({'B':(34,52,98),'b':(24,36,70),'G':(222,182,74)})
def make(name,hair):
    PAL['Y']=hair; PAL['y']=tuple(int(c*0.75) for c in hair)
    r=dict(
    hd=["................",".....KKKKKK.....","....KYYYYYYK....","...KYYYYYYYYK...","...KYSSSSSYYK...","...KSSSSSSSSK...","...KSKSSSSKSK...","...KSSSSSSSSK...","...KSSKKKKSSK...","....KSSSSSSK...."],
    td=["..KKBBBBBBBBKK..",".KBBBBBBBBBBBBK.",".KGGGGGGGGGGGGK.",".KBBBBBBBBBBBBK.",".KSBBBBBBBBBBSK.","..KGGGGGGGGGGK..","..KbBBBBBBBBbK..","..KBBBBBBBBBBK..","..KBBBKKKKBBBK.."],
    hu=["................",".....KKKKKK.....","....KYYYYYYK....","...KYYYYYYYYK...","...KYYYYYYYYK...","...KYYYYYYYYK...","...KYYYYYYYYK...","...KSYYYYYYSK...","...KSSSSSSSSK...","....KSSSSSSK...."],
    tu=["..KKBBBBBBBBKK..",".KBBBBBBBBBBBBK.",".KGGGGGGGGGGGGK.",".KBBBBBBBBBBBBK.",".KSBBBBBBBBBBSK.","..KGGGGGGGGGGK..","..KbBBBBBBBBbK..","..KBBBBBBBBBBK..","..KBBBKKKKBBBK.."],
    hl=["................",".....KKKKKK.....","....KYYYYYYK....","...KYYYYYYYK....","...KSSSYYYYK....","..KSSSSSYYYK....","..KSKSSSSYYK....","..KSSSSSSSSK....","...KKKSSSSK.....","....KSSSSK......"],
    tl=[".....KBBBBK.....","....KBBBBBBK....","...KGGGGGGGGK...","...KBBBBKBBBK...","...KBBBBKSBBK...","...KGGGGGGGGK...","...KbBBBBBBbK...","....KBBBBBBK....","....KBBBBBBK...."],
    )
    r.update(legs('B','K'))
    s=build(name,r); s.save(name+'_sheet.png'); return s
a=make('sillerburn_a',(120,82,50)); b=make('sillerburn_b',(52,44,40))
bg=Image.new('RGBA',(48*12+20,96*6),(122,154,79,255))
bg.alpha_composite(a.resize((288,576),Image.NEAREST),(0,0)); bg.alpha_composite(b.resize((288,576),Image.NEAREST),(308,0)); bg.save('sillerburn_preview.png')
