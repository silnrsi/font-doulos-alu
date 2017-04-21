VERSION="0.130"
APPNAME="doulosalu"
out='results'

basefont='LIBFONTS/Sildl'
tmap = {
    'r' : 'Regular',
    'b' : 'Bold',
    'i' : 'Italic',
    'bi' : 'BoldItalic'}

for n in ('r', 'i', 'b', 'bi') :
    tonefont = 'font-source/AkhaLahuTones-' + ('Bold' if 'b' in n else 'Regular') + '.ttf'
    t = n
    f = font(target = process('doulosSILALU-'+tmap[n]+'.ttf', cmd('../tools/cpglyphs ${DEP} ${SRC[0]} ${TGT}', [tonefont]), name('Doulos SIL ALU'),
                                                    cmd('hackos2 -u 43 -c 1 ${DEP} ${TGT}')),
            source = legacy('src/doulos_'+n+'.ttf', source = basefont + n + '.ttf', xml='font-source/akha_unicodecst.xml', noap=1),
            copyright = "Copyright (c) 2016, SIL International (http://www.sil.org/)",
            license = ofl("Doulos", "Doulos SIL"),
            version = VERSION,
            fret = fret(params='-r')
        )

