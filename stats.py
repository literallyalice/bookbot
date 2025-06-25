def count_words(text: str):
    words = text.split()
    return len(words)

def char_occurrence(text: str):
    words = text.lower()
    occurrences = {}
    for w in words:
        if w not in occurrences:
            occurrences[w] = 1
        else:
            occurrences[w] += 1
    return occurrences

def sorted_dictionary(pairs: dict):
    dict_list = []
    for k, v in pairs.items():
        dict_list.append({'char': k, 'count': v})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def sort_on(items):
    return items["count"]
