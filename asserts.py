def equals(actual, expected, message=None):
    assert actual == expected, (
        '\nExpected: {}\n'
        'Got: {}\n'
        'Additional info: {}\n'
        ''.format(expected, actual, message)
    )


def not_equal(actual, unexpected, message=None):
    assert actual != unexpected, (
        '\nRequiring a difference:\n'
        'Unexpected value: {}\n'
        'Actual value: {}\n'
        'Additional info: {}\n'
        ''.format(unexpected, actual, message)
    )


def contains(haystack, needle, message=None):
    assert needle in haystack, (
        '\n"{}" should have contained "{}"\n'
        'Additional info: {}\n'
        ''.format(haystack, needle, message)
    )
