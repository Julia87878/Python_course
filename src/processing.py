def filter_by_state(dict_list: list[dict], state_1: str = "EXECUTED") -> list[dict]:
    """Функция, которая фильтрует словари"""
    new_dict_list = []
    for dic in dict_list:
        if dic.get("state") == state_1:
            new_dict_list.append(dic)
    return new_dict_list


def sort_by_date(dict_list: list, assortment: bool = True) -> list:
    """Функция, которая сортирует по дате"""
    return sorted(dict_list, key=lambda dic: dic.get("date"), reverse=assortment)
