# utils/string_utils.py
def reverse_string(s):
    """Reverses a string."""
    return s[::-1]

def capitalize_words(s):
    """Capitalizes each word in the string."""
    return ' '.join(word.capitalize() for word in s.split())
