import sys

ROMAN_NUMERALS = {
    1:   'I',
    5:   'V',
    10:  'X',
    50:  'L',
    100: 'C',
    500: 'D',
    1000: 'M',
    5000: 'V'
}

ROMAN_MAP = ({'low': (1, 'I'),
              'mid': (5, 'V')},
             {'low': (10, 'X'),
              'mid': (50, 'L')},
             {'low': (100, 'C'),
              'mid': (500, 'D')},
             {'low': (1000, 'M'),
              'mid': (5000, 'V')})

ARABIC = 0
ROMAN = 1


def convert(digit, place):
    number = digit * 10**place

    # Check for direct conversion
    if number in ROMAN_NUMERALS:
        return ROMAN_NUMERALS[number]

    base = ROMAN_MAP[place]['low']
    middle = ROMAN_MAP[place]['mid']

    # check border case below middle
    if number == base[ARABIC] * 5 - base[ARABIC]:
        return '{0}{1}'.format(base[ROMAN], middle[ROMAN])

    # check border case below upper base (just before upper base)
    if number == base[ARABIC] * 10 - base[ARABIC]:
        upper_base = ROMAN_MAP[place + 1]['low']
        return '{0}{1}'.format(base[ROMAN], upper_base[ROMAN])

    result = ''
    if number >= base[ARABIC] * 5:
        result = middle[ROMAN]
        digit = (number - middle[ARABIC])/10**place

    result = '{0}{1}'.format(result, base[ROMAN] * digit)

    return result


def convert_to_roman(number):
    if int(number) >= 9000:
        print "Cannot convert numbers larger than 8999"
        sys.exit(0)
    final = ''
    for pos, num in enumerate(reversed(number)):
        result = convert(int(num), pos)
        final = '{0}{1}'.format(result, final)

    return final


def main():
    input_number = ''
    while input_number != 'q':
        input_number = raw_input("Enter a number (or 'q' to quit): ")
        if not input_number.isdigit():
            continue
        print '%s is %s' % (input_number, convert_to_roman(input_number))
        

if __name__ == '__main__':
    main()
