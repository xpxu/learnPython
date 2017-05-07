
def partition(predicate, values):
    """
    Splits the values into two sets, based on the return value of the function
    (True/False).
    """
    results = ([], [])
    for item in values:
        print predicate(item)
        results[predicate(item)].append(item)
    return results[True]

print partition(lambda x: x > 3, range(5))