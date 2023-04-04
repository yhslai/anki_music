import re
import os
import genanki
import utils
import yaml

model = genanki.Model(
    4512,
    'Scale Note Model',
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

notes = []
note_orders = [1, 2, 3, 4, 5, 6] # 0 is the root
for s in common_scales:
    for i in note_orders:
        question = f"Which note is the <i><b>{utils.ordinal(i+1)}</b></i> note of the <i><b>{s['key']} {s['mode']}</b></i> scale?"
        answer = s['notes'][i]

        note = genanki.Note(
            model=model,
            fields=[question, answer],
        )
        notes.append(note)
        
deck = genanki.Deck(
    8702,
    'Scale Notes Deck'
)

for note in notes:
    deck.add_note(note)

package = genanki.Package(deck)
package.write_to_file("decks/scale_notes_deck.apkg")
        
        

