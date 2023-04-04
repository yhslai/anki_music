import re

def lily_to_human_note(lily_str):

    pattern = re.compile(r"([a-g])([sf]?)([',]*)")

    match = pattern.match(lily_str)

    if match:

        pitch_str = match.group(1)

        accidental_str = match.group(2)

        octave_str = match.group(3)

        pitch = pitch_str.upper()

        if accidental_str == "s":

            accidental = "#"

        elif accidental_str == "f":

            accidental = "b"

        else:
            accidental = ""

        octave_offset = len(octave_str)

        if octave_str.startswith(","):

            octave_offset *= -1

        return pitch + accidental + str(3+octave_offset)