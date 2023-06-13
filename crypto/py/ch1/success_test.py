#!/usr/bin/env python3
from solution import challenge1

def solution_works():
    result = challenge1("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
    return result == "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

if __name__ == "__main__":
    success_fail = "[++++] Success! [++++]" if solution_works() else "[----] Fail :-( [----]"
    print(success_fail)
