from __future__ import annotations

beatles = {
    'john': {
        'instruments': ['drums', 'bass'],
        'age': 24
    },
    'paul': {
        'instruments': ['guitar', 'vocals'],
        'age': 29
    }
}

print(beatles['paul']['instruments'][1])

letters = ['a', 'b', 'c']
[print(l.upper()) for l in letters]


def full_name(first, last, capitalize=True):
    if capitalize:
        return ' '.join([first.capitalize(), last.capitalize()])
    return ' '.join([first, last])


print(full_name('roger', 'sole'))
print(full_name('roger', 'sole', False))


def luhn_checksum(number: str) -> bool:

    def digits_of(num: str) -> list[int]:
        return [int(d) for d in num]

    digits = digits_of(number)
    odd_digits = digits[-1::2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for digit in even_digits:
        checksum += sum(digits_of(str(digit * 2)))
    return checksum % 10 == 0
