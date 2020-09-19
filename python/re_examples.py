import re


def delete_all_strings_after_specific_symbols():
    text = """
    <span aaaaaaaaaaaaaaaaaaaaaaaaa>
    bbbbbbbbbbbbbbbb
    </sapn cccccccccccccccccccccccc>
    """
    print(text)

    text = re.sub(r"<\w.*.", "", text)
    print(text)

    text = re.sub(r"</\w.*.", "", text)
    print(text)
