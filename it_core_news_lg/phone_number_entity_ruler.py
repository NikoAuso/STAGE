from spacy.lang.char_classes import LIST_ELLIPSES, LIST_ICONS, ALPHA_LOWER, ALPHA_UPPER, CONCAT_QUOTES, ALPHA, HYPHENS
from spacy.lang.it.punctuation import ELISION
from spacy.util import compile_infix_regex

# infixes pattern
_infixes = (
        LIST_ELLIPSES
        + LIST_ICONS
        + [
            r"(?<=[0-9])[+\-\*^.](?=[0-9-])",
            r"(?<=[{al}{q}])\.(?=[{au}{q}])".format(
                al=ALPHA_LOWER, au=ALPHA_UPPER, q=CONCAT_QUOTES
            ),
            r"(?<=[{a}]),(?=[{a}])".format(a=ALPHA),
            r"(?<=[{a}])(?:{h})(?=[{al}])".format(a=ALPHA, h=HYPHENS, al=ALPHA_LOWER),
            r"(?<=[{a}0-9])[:<>=\/](?=[{a}])".format(a=ALPHA),
            r"(?<=[{a}][{el}])(?=[{a}0-9\"])".format(a=ALPHA, el=ELISION),
        ]
)

# Pattern per numeri di telefono mobili italiani
patterns_mobili = [
    # (0039 | +39) 312 45 67 890
    {"label": "CELL", "pattern": [
        {"TEXT": {"REGEX": "(00|\+)39"}, "OP": "*"},
        {"TEXT": {"REGEX": "[\.\s\-\/\(]"}, "OP": "*"},
        {"TEXT": {"REGEX": "3\d{2}"}},
        {"TEXT": {"REGEX": "[\.\s\-\/\)]"}, "OP": "*"},
        {"TEXT": {"REGEX": "\d{2}"}},
        {"TEXT": {"REGEX": "[\.\s\-\/]"}, "OP": "*"},
        {"TEXT": {"REGEX": "\d{2}"}},
        {"TEXT": {"REGEX": "[\.\s\-\/]"}, "OP": "*"},
        {"TEXT": {"REGEX": "\d{3}"}}
    ]},
    # (0039 | +39) 312 456 7890
    {"label": "CELL", "pattern": [
        {"TEXT": {"REGEX": "(00|\+)39"}, "OP": "*"},
        {"TEXT": {"REGEX": "[\.\s\-\/\(]"}, "OP": "*"},
        {"TEXT": {"REGEX": "3\d{2}"}},
        {"TEXT": {"REGEX": "[\.\s\-\/\)]"}, "OP": "*"},
        {"TEXT": {"REGEX": "\d{3}"}},
        {"TEXT": {"REGEX": "[\.\s\-\/]"}, "OP": "*"},
        {"TEXT": {"REGEX": "\d{4}"}}
    ]},
    # (0039 | +39) 3124567890
    {"label": "CELL", "pattern": [
        {"TEXT": {"REGEX": "(00|\+)39"}, "OP": "*"},
        {"TEXT": {"REGEX": "3\d{9}"}},
    ]},
    # (0039 | +39) 312 4567890
    {"label": "CELL", "pattern": [
        {"TEXT": {"REGEX": "(00|\+)39"}, "OP": "*"},
        {"TEXT": {"REGEX": "3\d{2}"}},
        {"TEXT": {"REGEX": "[\.\s\-\/\)]"}, "OP": "*"},
        {"TEXT": {"REGEX": "\d{7}"}},
    ]},
    # (0039 | +39)3124567890
    {"label": "CELL", "pattern": [
        {"TEXT": {"REGEX": "(00|\+)393\d{9}"}},
    ]},
    # (0039 | +39) varie con punti tutti attaccati
    {"label": "TEL", "pattern": [
        {"TEXT": {"REGEX": "(00|\+)39"}, "OP": "*"},
        {"TEXT": {"REGEX": "(3\d{2}[\.\s\-\/]*)(\d([\.\s\-\/]*)){7}"}},
    ]}
]
# Pattern per numeri di telefono fissi italiani
patterns_fissi = [
    # (0039 | +39) 012 34 56 7890
    {"label": "TEL", "pattern": [
        {"TEXT": {"REGEX": "(00|\+)39"}, "OP": "*"},
        {"TEXT": {"REGEX": "[\.\s\-\/\(]"}, "OP": "*"},
        {"TEXT": {"REGEX": "0\d{1,3}"}},
        {"TEXT": {"REGEX": "[\.\s\-\/\)]"}, "OP": "*"},
        {"TEXT": {"REGEX": "\d{2}"}},
        {"TEXT": {"REGEX": "[\.\s\-\/]"}, "OP": "*"},
        {"TEXT": {"REGEX": "\d{2}"}},
        {"TEXT": {"REGEX": "[\.\s\-\/]"}, "OP": "*"},
        {"TEXT": {"REGEX": "\d{2,4}"}}
    ]},
    # (0039 | +39) 012 345 6789
    {"label": "TEL", "pattern": [
        {"TEXT": {"REGEX": "(00|\+)39"}, "OP": "*"},
        {"TEXT": {"REGEX": "[\.\s\-\/\(]"}, "OP": "*"},
        {"TEXT": {"REGEX": "0\d{1,3}"}},
        {"TEXT": {"REGEX": "[\.\s\-\/\)]"}, "OP": "*"},
        {"TEXT": {"REGEX": "\d{3}"}},
        {"TEXT": {"REGEX": "[\.\s\-\/]"}, "OP": "*"},
        {"TEXT": {"REGEX": "\d{3,4}"}}
    ]},
    # (0039 | +39) 0123456789
    {"label": "TEL", "pattern": [
        {"TEXT": {"REGEX": "(00|\+)39"}, "OP": "*"},
        {"TEXT": {"REGEX": "0\d{9}"}},
    ]},
    # (0039 | +39) 012 3456789
    {"label": "TEL", "pattern": [
        {"TEXT": {"REGEX": "(00|\+)39"}, "OP": "*"},
        {"TEXT": {"REGEX": "[\.\s\-\/\(]"}, "OP": "*"},
        {"TEXT": {"REGEX": "0\d{1,3}"}},
        {"TEXT": {"REGEX": "[\.\s\-\/\)]"}, "OP": "*"},
        {"TEXT": {"REGEX": "\d{6,8}"}},
    ]},
    # (0039 | +39)0123456789
    {"label": "TEL", "pattern": [
        {"TEXT": {"REGEX": "(((00|\+)39)*)([\.\s\-\/(]*0\d{1,3}[\.\s\-\/)]*)(\d([\.\s\-\/]*)){6,8}"}},
    ]},
    # (0039 | +39) varie con punti tutti attaccati
    {"label": "TEL", "pattern": [
        {"TEXT": {"REGEX": "(00|\+)39"}, "OP": "*"},
        {"TEXT": {"REGEX": "([\.\s\-\/(]*0\d{1,3}[\.\s\-\/)]*)(\d([\.\s\-\/]*)){6,8}"}},
    ]}
]


def phone_number_rule(nlp):
    ruler = nlp.add_pipe("entity_ruler", before="ner")

    # modify tokenizer infix patterns
    infix_re = compile_infix_regex(_infixes)
    nlp.tokenizer.infix_finditer = infix_re.finditer

    ruler.add_patterns(patterns_mobili)
    ruler.add_patterns(patterns_fissi)

    return nlp
