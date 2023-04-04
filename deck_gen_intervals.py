import re
import os
import genanki
import yaml
import random

import utils

model = genanki.Model(
  4513,
  'Interval Calculation Model',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
  ],
  templates=[
  {
      'name': 'Interval Calculation Card',
      'qfmt': """<div style="text-align: center;font-size: 24px;">Calculate this interval:<br><br>
        <spn style="font-size: 36px;font-family: Times New Roman;">{{Question}}</span>
        </div>
      """,
      'afmt': '{{FrontSide}}<br><br><div style="text-align: center;font-size: 36px;font-family: Times New Roman;">{{Answer}}</div>',
  },
])

notes = []

intervals = yaml.load(open("data/intervals.yaml", "r"), Loader=yaml.FullLoader)
interval_dict = {}
for interval in intervals:
    interval_dict[interval["abs_value"]] = interval["names"][0]

for a in range(1, 11):
    for b in range(1, a):
        c = a + b
        question = f"{interval_dict[a]} + {interval_dict[b]} = ?"
        if c > 12:
            answer = f"{interval_dict[12]} + {interval_dict[c-12]}"
        else:
            answer = interval_dict[c]

        note = genanki.Note(
            model=model,
            fields=[question, answer],
        )
        notes.append(note)


count = 0

while count < 200:
    # randomly choose between A2 and G5
    mns = utils.all_common_notes()
    a = random.choice(mns)
    b = random.choice(mns)

    if a['abs_value'] == b['abs_value']:
        continue
    if b['abs_value'] > a['abs_value']:
        a, b = b, a
    if a['abs_value'] - b['abs_value'] >= 24:
        continue
    if a['abs_value'] - b['abs_value'] == 12:
        continue

    question = f"{a['names'][0]} - {b['names'][0]} = ?"
    if a['abs_value'] - b['abs_value'] > 12:
        answer = f"{interval_dict[12]} + {interval_dict[a['abs_value'] - b['abs_value'] - 12]}"
    else:
        answer = interval_dict[a['abs_value'] - b['abs_value']]

    note = genanki.Note(
        model=model,
        fields=[question, answer],
    )
    notes.append(note)

    count += 1


# Create the deck
deck = genanki.Deck(
    8703,
    'Interval Calculation Deck',
)

for note in notes:
    deck.add_note(note)

package = genanki.Package(deck)
package.write_to_file("decks/interval_calculation.apkg")


    
