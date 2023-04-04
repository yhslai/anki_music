import re
import os
import genanki

model = genanki.Model(
  4510,
  'Note Model',
  fields=[
    {'name': 'Question'},
    {'name': 'Question-Image'},
    {'name': 'Answer'},
  ],
  templates=[
  {
      'name': 'Note Card',
      'qfmt': '<div style="text-align: center;font-size: 24px;">{{Question}}<br><br>{{Question-Image}}</div>',
      'afmt': '{{FrontSide}}<br><br><div style="text-align: center;font-size: 36px;font-family: Times New Roman;">{{Answer}}</div>',
  },
])


img_dir = "media/img/notes"

# Create a list of all the notes
notes = []
# Iterate over .png files in the img_dir
for img in os.listdir(img_dir):
    # filename is like 'bass_A3.preview.png'
    pattern = re.compile(r"(bass|treble)_([A-G][b#]?[0-9]+).preview.png")
    match = pattern.match(img)
    if match:
        clef = match.group(1)
        note_name = match.group(2)

        # Create the question
        question = "Which note is this? (C, D, E...)"

        # Create the answer
        answer = f"{note_name}"
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
    8700,
    'Note Identification Deck',
)

# Add the notes to the deck
for note in notes:
    deck.add_note(note)
    
# Create the package
package = genanki.Package(deck)
package.media_files = [f'{img_dir}/{img}' for img in os.listdir(img_dir)]
package.write_to_file('decks/note_identification.apkg')
