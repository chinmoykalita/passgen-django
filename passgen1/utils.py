# this file contains utility functions

def make_hash_pass(inp: str, type: int):
    print(inp, type)

def hash_format_func(input):
    print(input)
    return input ** 3

def string_to_hash(input):
    conv = hash_format_func(input)
    print(conv)
    ad = conv * 3 - 4
    return ad