#!/usr/bin/env python3
"""
YN++ - A slang-style programming language that transpiles to Python.
"""

import re
import sys
import os

# ── Keyword Mappings ──────────────────────────────────────────────
KEYWORDS = {
    # Output / Input
    'spit':         'print',
    'yo':           'print',
    'holla':        'input',

    # Functions
    'cook':         'def',
    'drop':         'return',
    'say_less':     'return',
    'nigga':        'self',
    'yoself':       'self',

    # Conditionals
    'ifreal':       'if',
    'orcap':        'elif',
    'bet':          'else',

    # Loops
    'slide':        'for',
    'grind':        'while',
    'dip':          'break',
    'keepitmovin':  'continue',
    'run_it_back':  'continue',

    # Booleans / None
    'facts':        'True',
    'nocap':        'True',
    'ongod':        'True',
    'cap':          'False',
    'cappin':       'False',
    'ghost':        'None',

    # Logic
    'nah':          'not',
    'also':         'and',
    'eitherway':    'or',

    # Assertions
    'deadass':      'assert',
    'on_folks':     'assert',

    # Error handling
    'shootyashot':  'try',
    'trap':         'try',
    'brick':        'except',
    'fumble':       'except',
    'nomattawhat':  'finally',
    'throw':        'raise',
    'trippin':      'raise',

    # Classes / OOP
    'squad':        'class',
    'OG':           'super',
    'big_homie':    'super',

    # Imports
    'plug':         'import',
    'from':         'from',

    # Delete
    'yeet':         'del',

    # Built-in functions
    'runup':        'range',
    'count':        'len',
    'whole':        'int',
    'decimal':      'float',
    'words':        'str',
    'stack':        'list',
    'stash':        'dict',
    'peep':         'open',
    'bounce':       'exit',
    'dipped':       'exit',
    'sorted':       'sorted',
    'flipped':      'reversed',
    'snatch':       'pop',
    'toss':         'append',
    'typeof':       'type',
    'absolute':     'abs',
    'highkey':      'max',
    'lowkey':       'min',
    'mob':          'map',
    'each_one':     'enumerate',
    'link_up':      'zip',
    'check':        'isinstance',
    'fasho':        'bool',
    'round_up':     'round',
    'sum_up':       'sum',
    'any_real':     'any',
    'all_real':     'all',

    # String methods mapped as builtins
    'upper':        'upper',
    'lower':        'lower',

    # Other
    'chill':        'pass',
    'tap_in':       'with',
    'inna':         'in',
    'is':           'is',
    'posted':       'global',
    'lamba':        'lambda',
    'pull':         'yield',
    'real_one':     '__name__',
    'on_the_block': '"__main__"',
}

# Build regex: match keywords as whole words, longest first to avoid partial matches
_sorted_keys = sorted(KEYWORDS.keys(), key=len, reverse=True)
_pattern = re.compile(
    r"""('(?:[^'\\]|\\.)*'|"(?:[^"\\]|\\.)*"|'''[\s\S]*?'''|\"\"\"[\s\S]*?\"\"\"|#.*$)"""
    r'|'
    r'\b(' + '|'.join(re.escape(k) for k in _sorted_keys) + r')\b',
    re.MULTILINE
)


def transpile_line(line):
    """Transpile a single line of YN++ to Python, preserving strings and comments."""
    def replacer(match):
        # Group 1 = string literal or comment, leave it alone
        if match.group(1):
            return match.group(1)
        # Group 2 = keyword to replace
        keyword = match.group(2)
        return KEYWORDS.get(keyword, keyword)

    return _pattern.sub(replacer, line)


def transpile(source):
    """Transpile full YN++ source code to Python."""
    lines = source.split('\n')
    translated = [transpile_line(line) for line in lines]
    return '\n'.join(translated)


def run_file(filepath):
    """Transpile and execute a .ynpp file."""
    if not os.path.exists(filepath):
        print(f"Yo, can't find that file: {filepath}")
        sys.exit(1)

    with open(filepath, 'r') as f:
        source = f.read()

    python_code = transpile(source)

    # Show the transpiled code if --debug flag
    if '--debug' in sys.argv:
        print("── Transpiled Python ─────────────────")
        for i, line in enumerate(python_code.split('\n'), 1):
            print(f"  {i:3d} | {line}")
        print("──────────────────────────────────────\n")

    exec(compile(python_code, filepath, 'exec'), {'__name__': '__main__'})


def run_repl():
    """Interactive YN++ REPL."""
    print("YN++ REPL v1.0")
    print("Type your code. Type 'out' to exit.\n")

    env = {}
    while True:
        try:
            line = input("yn++>> ")
        except (EOFError, KeyboardInterrupt):
            print("\nLater!")
            break

        if line.strip() == 'out':
            print("Later!")
            break

        if not line.strip():
            continue

        python_code = transpile(line)
        try:
            # Try eval first (for expressions)
            result = eval(compile(python_code, '<repl>', 'eval'), env)
            if result is not None:
                print(result)
        except SyntaxError:
            # Fall back to exec (for statements)
            try:
                exec(compile(python_code, '<repl>', 'exec'), env)
            except Exception as e:
                print(f"You bricked it: {e}")
        except Exception as e:
            print(f"You bricked it: {e}")


def show_keywords():
    """Print all keyword mappings."""
    print("\nYN++ Keywords")
    print("=" * 45)
    # Group keywords by category
    categories = {
        'Output / Input':     ['spit', 'yo', 'holla'],
        'Functions':          ['cook', 'drop', 'say_less', 'nigga', 'yoself'],
        'Conditionals':       ['ifreal', 'orcap', 'bet'],
        'Loops':              ['slide', 'grind', 'dip', 'keepitmovin', 'run_it_back'],
        'Booleans':           ['facts', 'nocap', 'ongod', 'cap', 'cappin', 'ghost'],
        'Logic':              ['nah', 'also', 'eitherway'],
        'Assertions':         ['deadass', 'on_folks'],
        'Error Handling':     ['shootyashot', 'trap', 'brick', 'fumble', 'nomattawhat', 'throw', 'trippin'],
        'OOP':                ['squad', 'nigga', 'yoself', 'OG', 'big_homie'],
        'Imports':            ['plug'],
        'Delete':             ['yeet'],
        'Types':              ['whole', 'decimal', 'words', 'stack', 'stash', 'fasho'],
        'Built-ins':          ['runup', 'count', 'peep', 'bounce', 'dipped', 'highkey',
                               'lowkey', 'toss', 'snatch', 'typeof', 'absolute', 'mob',
                               'each_one', 'link_up', 'check', 'round_up', 'sum_up',
                               'any_real', 'all_real', 'flipped', 'sorted'],
        'Other':              ['chill', 'tap_in', 'inna', 'posted', 'lamba', 'pull',
                               'real_one', 'on_the_block'],
    }
    for cat, keys in categories.items():
        print(f"\n  {cat}:")
        for k in keys:
            if k in KEYWORDS:
                print(f"    {k:20s} ->  {KEYWORDS[k]}")
    print()


# ── CLI ───────────────────────────────────────────────────────────
if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] in ('-h', '--help'):
        print("YN++ - YN's favorite coding language\n")
        print("Usage:")
        print("  python ynpp.py <file.ynpp>          Run a .ynpp file")
        print("  python ynpp.py <file.ynpp> --debug   Run with transpiled output")
        print("  python ynpp.py repl                  Start interactive mode")
        print("  python ynpp.py keywords              Show all keywords")
        sys.exit(0)

    if sys.argv[1] == 'repl':
        run_repl()
    elif sys.argv[1] == 'keywords':
        show_keywords()
    else:
        run_file(sys.argv[1])
