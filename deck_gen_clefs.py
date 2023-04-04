import re
import os
import genanki
import utils

model = genanki.Model(
  4511,
  'Clef Scale Model',
  fields=[
    {'name': 'Question'},
    {'name': 'Question-Image'},
    {'name': 'Answer'},
  ],
  templates=[
  {
      'name': 'Clef Card',
      'qfmt': '<div style="text-align: center;font-size: 24px;">{{Question}}<br><br>{{Question-Image}}</div>',
      'afmt': '{{FrontSide}}<br><br><div style="text-align: center;font-size: 36px;font-family: Times New Roman;">{{Answer}}</div>',
  },
])


img_dir = "media/img/clefs"

# Create a list of all the notes
notes = []

for img in os.listdir(img_dir):
    pattern = re.compile(r"(bass|treble)_(major|minor)_([a-g][sf]?).preview.png")
    match = pattern.match(img)

    if match:
        clef = match.group(1)
        mode = match.group(2)
        root = match.group(3)

        # Create the question
        question = f"Which <i>{mode}</i> scale is this? (C Major, D Minor...)"
        # Create the answer
        answer = f"{utils.lily_to_human_note(root)[:-1]} {mode.capitalize()}" 
        # Create the image
        image = f"<img src='{img}'>"

        # Create the note
        note = genanki.Note(
            model=model,
            fields=[question, image, answer],
        )

        # Append the note to the list of notes
        notes.append(note)

# Create the deck
deck = genanki.Deck(
    8701,
    'Clef Scale Identification Deck',
)

# Add the notes to the deck
for note in notes:
    deck.add_note(note)

# Write the deck to a file
package = genanki.Package(deck)
package.media_files = [f'{img_dir}/{img}' for img in os.listdir(img_dir)]
package.write_to_file('decks/clef_scale_identification.apkg')
