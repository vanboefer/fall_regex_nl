import re
import pandas as pd


def find_matches(regexes, sentence):
    """
    Return a list of all `regexes` matches found in the `sentence`.

    Arguments
    =========
    regexes : iterable (list-like) of regex patterns
    sentence : str

    Returns
    =======
    found_matches : list of re.Match objects (if any)
    """

    found_matches = list()
    for regex in regexes:
        pattern = re.compile(r'{}'.format(regex), re.I)
        matches = pattern.finditer(sentence)
        for match in matches:
            found_matches.append(match)
    return found_matches


def process_sentence(sentence, vocab, pp_rules=None):
    """
    Check if there is a fall mentioned in the `sentence` based on the provided `vocab`. Presence of one of the `pp_rules` patterns (if provided) in the `sentence` will turn a 'fall' outcome to 'no fall'.

    Arguments
    =========
    sentence : str
    vocab : iterable (list-like) of regex patterns
        Vocabulary of patterns indicating a fall.
    pp_rules : iterable (list-like) of regex patterns, default=None
        Vocabulary of patterns indicating that there is no fall despite a vocab match.

    Returns
    =======
    output : dict
        - fall: True if there is a vocab match and no pp_rules match, else False
        - vocab_found: True if there is a vocab match, else False
        - pp_found: True if there is a pp_rules match, False if no match, None if no pp_rules are provided
        - vocab_matches: list of re.Match objects (if any)
        - pp_matches: list of re.Match objects (if any)
    """

    output = {
        'fall':             None,
        'vocab_found':      None,
        'pp_found':         None,
        'vocab_matches':    list(),
        'pp_matches':       list(),
    }

    # find vocabulary matches
    output['vocab_matches'] = find_matches(vocab, sentence)
    output['vocab_found'] = bool(output['vocab_matches'])

    # find post-processing matches
    if pp_rules is not None:
        output['pp_matches'] = find_matches(pp_rules, sentence)
        output['pp_found'] = bool(output['pp_matches'])

    # fall outcome
    output['fall'] = output['vocab_found'] and not output['pp_found']

    return output
