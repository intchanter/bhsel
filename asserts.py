'''
Nice helper functions for making different kinds of assertions.
'''


def equal(actual, expected, message=None):
    '''
    Assert that actual equals expected.
    '''
    assert actual == expected, (
        '\nExpected: {}\n'
        'Got: {}\n'
        'Additional info: {}\n'
        ''.format(repr(expected), repr(actual), message)
    )


def not_equal(actual, unexpected, message=None):
    '''
    Assert that actual does not equal unexpected.
    '''
    assert actual != unexpected, (
        '\nRequiring a difference:\n'
        'Unexpected value: {}\n'
        'Actual value: {}\n'
        'Additional info: {}\n'
        ''.format(repr(unexpected), repr(actual), message)
    )


def contains(haystack, needle, message=None):
    '''
    Assert that haystack contains needle.
    '''
    assert needle in haystack, (
        '\n"{}" should have contained "{}"\n'
        'Additional info: {}\n'
        ''.format(repr(haystack), repr(needle), message)
    )


def ok(actual, message=None):
    '''
    Assert that actual is a true value.
    '''
    assert actual, (
        '\nExpected a value that is true\n'
        'Got: {}\n'
        'Additional info: {}\n'
        ''.format(repr(actual), message)
    )


def not_ok(actual, message=None):
    '''
    Assert that actual is a false value.
    '''
    assert not actual, (
        '\nExpected a value that is not true\n'
        'Got: {}\n'
        'Additional info: {}\n'
        ''.format(repr(actual), message)
    )
