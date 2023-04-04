import abjad

mode_strs = ['major', 'minor']
root_strs = {'major': ['c', 'g', 'd', 'a', 'e', 'b', 'fs', 'f', 'bf', 'ef', 'af', 'cs'],
             'minor': ['a', 'e', 'b', 'fs', 'cs', 'gs', 'ds', 'd', 'g', 'c', 'f', 'as'],
}
clef_strs = ['treble', 'bass']

for m in mode_strs:
    for r in root_strs[m]:
        for c in clef_strs:
            staff = abjad.Staff('r2')
            clef = abjad.Clef(c)
            key = abjad.KeySignature(
                abjad.NamedPitchClass(r), abjad.Mode(m))
            abjad.attach(clef, staff[0])
            abjad.attach(key, staff[0])

            path = f"./media/img/clefs/{c}_{m}_{r}.png"

            abjad.persist.as_png(staff, path, preview=True, resolution=600)
