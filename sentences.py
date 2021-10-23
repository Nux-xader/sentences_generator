import random


def get_verb(clsf):
    if clsf == "i":
        verbs = [
            'painted', 'smiled', 'accelerated', 'cried', 'floated', 'died', 
            'laughed', 'wrote', 'studied', 'played', 'sang', 'slept', 'flew', 
            'worked', 'ran', 'screamed'
            ]
    else:
        verbs = [
            'grabbed', 'slapped', 'exploded', 'hugged', 'poked', 'opened', 
            'broke', 'created', 'killed', 'admired', 'painted', 'ate', 
            'held', 'taught', 'fed', 'held', 'loved'
            ]
    return verbs[random.randint(0,len(verbs)-1)]


def get_noun():
    nouns = [
        'butter', 'bull', 'mistake', 'balloon', 'brain', 'trunk', 'ice', 
        'person', 'ferryboat', 'suit', 'lightning', 'yacht', 
        'toothbrush', 'kitchen', 'city', 'carrot', 'swing', 'fox', 
        'shelf', 'storm', 'crack', 'radish', 'comma', 'submarine', 
        'ring', 'instrument', 'banana', 'relatives', 'rooster', 'straw', 
        'hedge', 'duck', 'notebook', 'spot', 'soup', 'hamburger', 'fuel'
        ]

    return nouns[random.randint(0,len(nouns)-1)]

def get_adjectives():
    adjectives = [
        'impossible', 'thundering', 'abnormal', 'elderly', 'wrathful', 
        'statuesque', 'regular', 'ossified', 'violet', 'barbarous', 'private', 
        'difficult', 'unnatural', 'perfect', 'handsomely', 'psychedelic', 
        'fcharh', 'chilly', 'gratis', 'jumpy', 'evasive', 'ceaseless', 
        'impartial', 'eager', 'premium', 'spicy', 'actually', 'crazy', 'elated',
        ]

    return adjectives[random.randint(0,len(adjectives)-1)]


def get_determiner():
    determiners = [
        'some', 'this', 'every', 'one', 'the', 'that', 'her', 'its', 'our', 
        'my', 'your', 'their', 'another', 'his', 'no'
        ]

    return determiners[random.randint(0,len(determiners)-1)]

def get_preposition():
    prepositions = [
        'underneath', 'within', 'of', 'by', 'without', 'beside', 'opposite', 
        'into', 'about', 'for', 'across', 'since', 'against', 'throughout', 
        'between', 'to', 'above', 'past', 'with', 'via', 'except', 'up', 
        'off', 'like', 'near', 'despite', 'until', 'out', 'in', 'below'
        ]

    return prepositions[random.randint(0,len(prepositions)-1)]

def get_noun_pharse():
    char = ""
    if random.random() < 0.99: char+=f"{get_determiner()} "
    if random.random() < 0.3: char+=f"{get_adjectives()} "
    char+=get_noun()
    if random.random() < 0.03: char+=f" {get_prepositional_phrase()}"
    return char


def get_verb_pharse():
    if random.random() < 0.5:
        return f"{get_verb('')} {get_noun_pharse()}"
    else:
        return get_verb("i")


def get_prepositional_phrase():
    return f"{get_preposition()} {get_noun_pharse()}"


# main program
def main():
    for i in range(12):
        char = f"{get_noun_pharse()} {get_verb_pharse()}"
        if random.random() < 0.8:
            if random.random() < 0.5:
                char+=f" {get_prepositional_phrase()}"
            else:
                char = f"{get_prepositional_phrase()}, {char}"

        print(f"{char.capitalize()}.")


if __name__ == '__main__':
    main()