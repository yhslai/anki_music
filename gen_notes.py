import abjad
import utils

clef_strs = ['treble', 'bass']
note_strs = {
    'treble': [
        "a", "b",
        "c'", "d'", "e'", "f'", "g'", "a'", "b'",
        "c''", "d''", "e''", "f''", "g''", "a''", "b''",
        "c'''"
    ],
    'bass': [
        "c,", "d,", "e,", "f,", "g,", "a,", "b,",
        "c", "d", "e", "f", "g", "a", "b",
        "c'", "d'", "e'",
    ],
}

for c in clef_strs:
    for n in note_strs[c]:
        clef = abjad.Clef(c)
        staff = abjad.Staff(f"{n}4")
        abjad.attach(clef, staff[0])
        note_human = utils.lily_to_human_note(n)

        path = f"./media/img/notes/{c}_{note_human}.png"

        abjad.persist.as_png(staff, path, preview=True, resolution=600)
