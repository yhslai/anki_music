import re
import os
import genanki
import utils
import yaml

model = genanki.Model(
    4514,
    'Scale Solfege Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[
        {
            'name': 'Scale Note Card',
            'qfmt': """<div style="text-align: center;font-size: 36px;font-family: Times New Roman;">{{Question}}</div>""",
            'afmt': '{{FrontSide}}<br><br><div style="text-align: center;font-size: 36px;font-family: Times New Roman;">{{Answer}}</div>',
        },
])

common_scales = yaml.load(open("data/common_scales.yaml", "r"), Loader=yaml.FullLoader)
utils.append_notes_on_scales(common_scales)
utils.append_solfeges_on_scales(common_scales)

notes = []
note_orders = [1, 2, 3, 4, 5, 6] # 0 is the root
for s in common_scales:
    for i in note_orders:
        solfege = s['solfeges'][i]
        n = s['notes'][i]
        question = f"Which note is the <i><b>{solfege}</b></i> solfege of the <i><b>{s['key']} {s['mode']}</b></i> scale?"
        answer = n

        note = genanki.Note(
            model=model,
            fields=[question, answer],
        )
        notes.append(note)

        question = f"Which solfege is the <i><b>{n}</b></i> note of the <i><b>{s['key']} {s['mode']}</b></i> scale?"
        answer = solfege
        
        note = genanki.Note(
            model=model,
            fields=[question, answer],
        )
        notes.append(note)
        

deck = genanki.Deck(
    8704,
    'Scale Solfeges Deck'
)

for note in notes:
    deck.add_note(note)

package = genanki.Package(deck)
package.write_to_file("decks/scale_solfeges_deck.apkg")
        
        

