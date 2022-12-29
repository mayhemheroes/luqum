#!/usr/bin/env python3

import atheris
import sys
import fuzz_helpers

with atheris.instrument_imports(include=['luqum']):
    from luqum.parser import parser

from luqum.exceptions import ParseError
from _decimal import InvalidOperation

def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    try:
        parser.parse(fdp.ConsumeRemainingString())
    except (ParseError, InvalidOperation):
        return -1

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
