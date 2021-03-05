import re


def prep_search_term(search_term):
    """uses a regular expression to remove any special characters before splitting to a list
    special characters before splitting to a list"""
    clean_up = re.sub(r"[,@\'?.$%_!#]", "", search_term, flags=re.I)
    clean_up = clean_up.split()
    ready_to_search = '+'.join(clean_up)
    return ready_to_search
