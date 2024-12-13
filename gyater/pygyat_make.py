gyat_data = [
    ('try', 'hawk'),
    ('except', 'tuah'),
    ('finally', 'spit on that thang'),
    ('return', 'its giving'),
    ('-', 'fanum tax'),
    ('+', 'rizz'),
    ('print', 'yap'),
    ('True', 'Aura'),
    ('False', 'Cooked'),
    ('def', 'bop'),
    ('while', 'let him cook'),
    ('import', 'glaze'),
    ('from', 'lock in'),
    ('class', 'skibidi'),
    ('if', 'chat is this real'),
    ('elif', 'yo chat'),
    ('else', 'only in ohio'),
    ('for', 'mewing'),
    ('break', 'just put the fries in the bag bro'),
    ('continue', 'edge'),
    ('assert', 'sus'),
    ('raise', 'crashout'),
    ('in', 'diddy'),
    ('with', 'pookie'),
    ('as', 'ahh'),
    ('global', 'GOAT'),
    ('nonlocal', 'motion'),
    ('del', 'delulu'),
    ('yield', 'pause'),
    ('yield from', 'pause no diddy'),
    ('None', 'NPC'),
    ('pass', 'pluh'),
    ('self', 'unc'),
    ('range', 'huzz'),
    ('>', 'sigma'),
    ('<', 'beta'),
    ('≥', 'sigma twin'),
    ('≤', 'beta twin'),
    ('==', 'twin'),
    ('open', 'mog'),
    ('close', 'demure')
]

def gyat_make(file_path: str) -> None:
    with open(file_path, 'r') as file:
        data = file.read()
        for word, gyat in gyat_data:
            data = data.replace(word, gyat)
    file_path = file_path.replace('.py', '.gyat')
    with open(file_path, 'w') as file:
        file.write(data)

# Do the reverse of the above function
def gyat_unmake(file_path: str) -> None:
    with open(file_path, 'r') as file:
        data = file.read()
        for word, gyat in gyat_data:
            data = data.replace(gyat, word)
    file_path = file_path.replace('.gyat', '.py')
    with open(file_path, 'w') as file:
        file.write(data)

gyat_make('../2024/vicus/dag_7.py')