calls = 0
def count_calls():
    global calls
    calls += 1


def string_info(string):
    str_ = str(string)
    result = (len(str_), str_.upper(), str_.lower())
    count_calls()
    return result


def is_contains(string, list_to_search):
    count_calls()
    lower_string = string.lower()
    lower_list = [item.lower() for item in list_to_search]
    return lower_string in lower_list


print(string_info("Taranis"))
print(string_info("Vanargand"))
print(is_contains("Urban", ["BanaN", "UrBAN", "Ananas"]))
print(is_contains("Taranis", ["Tarascus", "Belenus", "Matir"]))
print(calls)
