def get_index_different_char(chars):
    enumerate_chars_dict = dict(list(enumerate(chars)))

    alnum_char = []
    non_alnum_char = []

    for key, value in enumerate_chars_dict.items():
        if str(value).isalpha() or str(value).isdigit():
            alnum_char.append(key)
        else:
            non_alnum_char.append(key)

    if len(alnum_char) > len(non_alnum_char):
        return non_alnum_char[0]
    if len(alnum_char) < len(non_alnum_char):
        return alnum_char[0]
