import re

def test_password(text):

    test_length = re.match(re.compile(r'.{8,}'), text)
    test_lower = re.search(re.compile(r'[a-z]'), text)
    test_upper = re.search(re.compile(r'[A-Z]'), text)
    test_number = re.search(re.compile(r'[0-9]'), text)

    if test_length:
        print('more than 8 characters :' + 'ok')
    else:
        print('you should type more than 8 characters')
    if test_lower:
        print('include lower characters:' + 'ok' )
    else:
        print('you should include a lower character ')
    if test_upper:
        print('include upper characters: ' + 'ok')
    else:
        print('you should include an upper character')
    if test_number:
        print('include numbers:' + 'ok')
    else:
        print('you should include a number ')
    if test_length and test_lower and test_upper and test_number:
        print('that is perfect')
    return False

test_password((input('Type password : ')))
