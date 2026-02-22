# YN++ Skill Spec

Use this document as the source of truth for generating, debugging, and teaching YN++ code.

## What YN++ Is

YN++ is a Python-transpiling language with slang-style keywords.

- Write code in `.ynpp` files.
- Execute via `ynpp.py`.
- Keep syntax Python-like except for mapped keywords.

## Runtime Commands

```bash
python3 ynpp.py <file.ynpp>
python3 ynpp.py <file.ynpp> --debug
python3 ynpp.py repl
python3 ynpp.py keywords
```

## Agent Rules

1. Output YN++ code by default unless Python is explicitly requested.
2. Preserve keyword mappings exactly; do not invent new keywords.
3. Use `.ynpp` filenames in examples and commands.
4. When debugging, provide:
   - likely cause,
   - corrected YN++ code,
   - short explanation.
5. Keep explanations concise unless asked for deep detail.

## Core Keyword Mappings

### Output / Input

- `spit` -> `print`
- `yo` -> `print`
- `holla` -> `input`

### Functions

- `cook` -> `def`
- `drop` -> `return`
- `say_less` -> `return`
- `nigga` -> `self`
- `yoself` -> `self`

### Conditionals

- `ifreal` -> `if`
- `orcap` -> `elif`
- `bet` -> `else`

### Loops

- `slide` -> `for`
- `grind` -> `while`
- `dip` -> `break`
- `keepitmovin` -> `continue`
- `run_it_back` -> `continue`

### Booleans / None

- `facts` -> `True`
- `nocap` -> `True`
- `ongod` -> `True`
- `cap` -> `False`
- `cappin` -> `False`
- `ghost` -> `None`

### Logic

- `nah` -> `not`
- `also` -> `and`
- `eitherway` -> `or`

### Errors / Assertions

- `deadass` -> `assert`
- `on_folks` -> `assert`
- `shootyashot` -> `try`
- `trap` -> `try`
- `brick` -> `except`
- `fumble` -> `except`
- `nomattawhat` -> `finally`
- `throw` -> `raise`
- `trippin` -> `raise`

### Classes / Imports / Other

- `squad` -> `class`
- `OG` -> `super`
- `big_homie` -> `super`
- `plug` -> `import`
- `yeet` -> `del`
- `inna` -> `in`
- `tap_in` -> `with`
- `posted` -> `global`
- `lamba` -> `lambda`
- `pull` -> `yield`
- `real_one` -> `__name__`
- `on_the_block` -> `"__main__"`

### Common Built-ins

- `runup` -> `range`
- `count` -> `len`
- `whole` -> `int`
- `decimal` -> `float`
- `words` -> `str`
- `stack` -> `list`
- `stash` -> `dict`
- `peep` -> `open`
- `highkey` -> `max`
- `lowkey` -> `min`
- `toss` -> `append`
- `snatch` -> `pop`
- `typeof` -> `type`
- `absolute` -> `abs`
- `mob` -> `map`
- `each_one` -> `enumerate`
- `link_up` -> `zip`
- `check` -> `isinstance`
- `fasho` -> `bool`
- `round_up` -> `round`
- `sum_up` -> `sum`
- `any_real` -> `any`
- `all_real` -> `all`

## Minimal Example

```ynpp
spit("Wassup world!")

name = "King"
ifreal name == "King":
    spit("Respect, " + name + "!")
bet:
    spit("What's good " + name)
```

Run:

```bash
python3 ynpp.py hello.ynpp
```

## Debug Workflow

When debugging, run with transpiled output:

```bash
python3 ynpp.py broken.ynpp --debug
```

Then compare YN++ vs transpiled Python and fix syntax/keyword misuse.


