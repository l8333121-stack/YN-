# YN++ (CLI)

YN++ is a slang-style language that transpiles to Python and runs locally, for niggas, by niggas.

This repository is focused on the **language runtime**.

## Requirements

- Python 3.8+ (3.10+ recommended)

## Quick Start

```bash
git clone https://github.com/l8333121-stack/YN-.git
cd YN-
python3 ynpp.py examples/hello.ynpp
```

## Run Files

```bash
python3 ynpp.py <file.ynpp>
```

Example:

```bash
python3 ynpp.py examples/basics.ynpp
```

## Debug Transpiled Python

```bash
python3 ynpp.py examples/hello.ynpp --debug
```

## Interactive REPL

```bash
python3 ynpp.py repl
```

Type `out` to exit.

## See Available Keywords

```bash
python3 ynpp.py keywords
```

## Project Structure

- `ynpp.py` - transpiler + runtime CLI
- `examples/` - sample `.ynpp` programs


