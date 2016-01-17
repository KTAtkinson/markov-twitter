"""Makes markov chains and saves them to a text file in JSON format."""
import json
import os import path

def open_and_read_file(file_path, current_text=None):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    text_file = open(file_path)
    text = text_file.read().replace('\n', ' ').strip()
    if current_text:
        text = ' '.join((current_text, text))
    text_file.close()
    return text


def make_chains(text_string, gram_len):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('mary', 'hi'): ['there'], ('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi']}

    """

    chains = {}

    text_list = text_string.split(" ")
    gram = tuple(text_list[:gram_len])

    for word in text_list[gram_len:]:
        if word == '':
            continue
        if chains.has_key(gram):
            chains[gram].append(word)
        else:
            chains[gram] = [word]

        gram = gram[1:] + tuple([word])

    return chains


def make_chains_file(chains, new_file_path='chain.txt'):
    """Returns filename after writing JSON chains to given file path."""
    full_path = path.abspath(new_file_path)

    if path.exists(file_path):
        raise BufferError('File {} already exists.'.format(full_path))

    with open(full_path, 'w') as write_file:
        json_chains = json.dumps(chains)
        write_file.write(json_chains)

    return full_path
    