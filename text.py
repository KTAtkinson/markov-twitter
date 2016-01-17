from random import choice


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""
    first_pair = choice(chains.keys())
    text = ' '.join(first_pair)
    text = text[0].capitalize() + text[1:]


    while chains.has_key((first_pair)):
        # if not text[-1].isalpha() and not text[-1].isdigit():
        #     break
        if text[-1] in '!.?':
            if len(text) <= (140 - 13): #added hashtag
                return text
            else:
                break
        next_word = choice(chains[first_pair])
        text += ' {}'.format(next_word)
        
        first_pair = (first_pair[1], next_word)
