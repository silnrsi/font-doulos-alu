#!/usr/bin/python
# this is a smith configuration file

# set the default output folders
out = "results"
DOCDIR = ["documentation", "web"]
OUTDIR = "installers"
ZIPDIR = "releases"
TESTDIR = "tests"
TESTRESULTSDIR = "tests"
STANDARDS = "reference"

# set the font name, version, licensing and description
APPNAME = "DoulosSILALU"
VERSION = "0.130"
# BUILDLABEL = "alpha1"

basefont='source/LIBFONTS/Sildl'
tmap = {
    'r' : 'Regular',
    'b' : 'Bold',
    'i' : 'Italic',
    'bi' : 'BoldItalic'}

for n in ('r', 'i', 'b', 'bi') :
    tonefont = 'source/AkhaLahuTones-' + ('Bold' if 'b' in n else 'Regular') + '.ttf'
    t = n
    f = font(target = process('Doulos-SIL-ALU-'+tmap[n]+'.ttf', cmd('../tools/cpglyphs ${DEP} ${SRC[0]} ${TGT}', [tonefont]), name('Doulos SIL ALU'),
                                                    cmd('hackos2 -u 43 -c 1 ${DEP} ${TGT}')),
            source = legacy('src/doulos_'+n+'.ttf', source = basefont + n + '.ttf', xml='source/akha_unicodecst.xml', noap=1),
            version = VERSION,
            fret = fret(params='-r')
        )

