#!/usr/bin/env python2

"""
Gets a bitstring from stdin. Splits the string into groups of 7-bits, and
converts each group of 7-bits into a decimal integer. Looks up the value in
CHARS and prints to stdout for each group.

Oliver Chang, CSC314: Computer Organization and Architecture, 9/19/13
"""

# table of ASCII characters generated with the python command...
# >>> tuple([chr(x) for x in xrange(0,128)])
CHARS = ('\x00', '\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07', '\x08',
         '\t', '\n', '\x0b', '\x0c', '\r', '\x0e', '\x0f', '\x10', '\x11',
         '\x12', '\x13', '\x14', '\x15', '\x16', '\x17', '\x18', '\x19', '\x1a',
         '\x1b', '\x1c', '\x1d', '\x1e', '\x1f', ' ', '!', '"', '#', '$', '%',
         '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3',
         '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A',
         'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
         'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']',
         '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
         'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
         'z', '{', '|', '}', '~', '\x7f')


def get_bit_string():
    """Gets a string from user. Assume string is composed entirely of 0s and 1s.
    """
    bit_string = raw_input("7-bit bytes (spaces OK): ").replace(" ", "")

    # Sanitize input
    for char in bit_string:
        if char not in ("0", "1"):
            raise ValueError("Input must be entirely zeroes and ones.")

    return bit_string


def convert_to_decimal(string):
    """Implementation of the double-dabble algorithm for converting
    a binary bit string to a decimal integer.
    (Null and Lobur, Computer Organization and Architecture 1e, p. 46)

    Outline:
    For every digit of the binary number (_except_ the last digit),
    we add the digit (0 or 1) to the sum and then multiply the sum by two.
    For the last digit, we skip the multiplication step.
    Assume every bit of string is valid (i.e. string is entirely
    composed of 0 and 1).
    """
    sum_ = 0
    for char in string[:-1]:
        sum_ += int(char)
        sum_ <<= 1
    else:
        sum_ += int(string[-1])

    return sum_


def convert_bit_string(string):
    """Converts an arbitrary length binary string to a decimal int array.

    Assumptions:
        1. bit_string is a string composed entirely of 0s and 1s (no spaces!)
        2. A byte is composed of 7-bits
    """
    binary_bytes = [string[i:i+7] for i in xrange(0, len(string), 7)]
    return map(convert_to_decimal, binary_bytes)


def display_ascii(ascii_ints):
    """Convert a list of ints to ascii characters.
    """
    string = ""

    for i in ascii_ints:
        if i < 0 or i > 128:
            raise ValueError("ASCII characters must be >= 0 and <= 128.")

        # We don't have to subtract one here even though CHARS is 0-indexed.
        # This is because the ASCII chars are also 0-indexed!
        string += CHARS[i]
    else:
        # Use repr() to get the *representation* of the character, important
        # e.g. the newline character.
        # Slice to get rid of the single quotes repr() adds
        print repr(string)[1:-1]


def main():
    bit_string = get_bit_string()
    ascii_codes = convert_bit_string(bit_string)
    display_ascii(ascii_codes)


if __name__ == "__main__":
    while True:
        try:
            main()
        except ValueError as err:
            print err
        except (KeyboardInterrupt, EOFError):
            print
            raise SystemExit(0)
