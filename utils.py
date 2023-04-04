import re
import yaml

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
    else:
        print(f"Error: {lily_str} is not a valid lilypond pitch string")
        return None


# abs note = C1 = 0, C#1 = 1, D1 = 2, D#1 = 3, etc.
def human_note_to_abs_note(human_node):
    pattern = re.compile(r"([A-G])([b#]?)([0-9]+)")
    match = pattern.match(human_node)
    
    if match:
        pitch_str = match.group(1)
        accidental_str = match.group(2)
        octave_str = match.group(3)
        # C = 0, D = 1, etc
        pitch = ord(pitch_str.upper()) - ord("C")
        if accidental_str == "#":
            accidental = 1
        elif accidental_str == "b":
            accidental = -1
        else:
            accidental = 0
        octave = int(octave_str)
        
        return pitch + accidental + 12 * (octave - 1)
    else:
        print(f"Error: {human_node} is not a valid human pitch string")
        return None
    

# 21 = A2, 55 = G5
def all_common_notes():
    lower = human_note_to_abs_note(human_node="A2")
    upper = human_note_to_abs_note(human_node="G5") + 1
    notes = []
    note_data = yaml.load(open("data/notes.yaml"), Loader=yaml.FullLoader)
    for i in range(lower, upper):
        octave = (i // 12) + 1
        pitch = i % 12
        notes.append({
            "abs_value": i,
            "names": list(f"{n}{octave}" for n in note_data[pitch]["names"]),
        })
        
    return notes
    
        
# A function turns 1 to '1st', 2 to '2nd', etc
def ordinal(num):
    if num == 1:
        return "1st"
    elif num == 2:
        return "2nd"
    elif num == 3:
        return "3rd"
    else:
        return f"{num}th"


def next_neutral_name(n):
    if n == 'G':
        return 'A'
    return chr(ord(n) + 1)


def append_notes_on_scales(scales):
    note_data = yaml.load(open("data/notes.yaml"), Loader=yaml.FullLoader)
    mode_data = yaml.load(open("data/modes.yaml"), Loader=yaml.FullLoader)

    for s in scales:
        notes = []

        v = -1
        for n in note_data:
            if s['key'] in n['names']:
                v = n['abs_value']
        if v == -1:
            print(f"Error: {s['key']} is not a valid note")
            return None
        
        notes.append(s['key'])
        cur_neutral = s['key'][0]
        for i in mode_data[s['mode']]:
            v += i
            v %= 12
            n = note_data[v]
            neutral = next_neutral_name(cur_neutral)
            found = False
            for name in n['names']:
                if name[0] == neutral:
                    notes.append(name)
                    cur_neutral = neutral
                    found = True
                    break
            
            if not found:
                print(f"Error: {neutral} is not a valid neutral note of value {v}")
                return None
            
        s['notes'] = notes 


def append_solfeges_on_scales(scales):
    note_data = yaml.load(open("data/notes.yaml"), Loader=yaml.FullLoader)
    mode_data = yaml.load(open("data/modes.yaml"), Loader=yaml.FullLoader)
    solfege_data = yaml.load(open("data/solfeges.yaml"), Loader=yaml.FullLoader)

    for s in scales:
        solfeges_on_scale = []

        v = 0
        cur_degree = 1
        solfeges_on_scale.append('Do')
        for i in mode_data[s['mode']]:
            v += i
            v %= 12
            cur_degree += 1
            found = False
            if cur_degree == 8:
                break

            for sol in solfege_data:
                if sol['degree'] == cur_degree:
                    for solfege in sol['solfeges']:
                        if solfege['value'] == v:
                            solfeges_on_scale.append(solfege['name'])
                            found = True
                            break
            
            if not found:
                print(f"Error: degree {cur_degree} degree and value {v} have no solfege.")
                return None
            
        s['solfeges'] = solfeges_on_scale
    
            
        
        
        

            
        
        


        
