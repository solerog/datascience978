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
