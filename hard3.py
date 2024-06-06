def calculate_structure_sum(*args):
    s = 0
    for item in args:
        if isinstance(item, int):
            s += item
        elif isinstance(item, str):
            s += len(item)
        elif isinstance(item, dict):
            for key, value in item.items():
                s += calculate_structure_sum(key, value)
        elif isinstance(item, set):
            for i in item:
                s += calculate_structure_sum(i)
        elif isinstance(item, tuple):
            for i in item:
                s += calculate_structure_sum(i)
        elif isinstance(item, list):
            for i in item:
                s += calculate_structure_sum(i)
    return s


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
