# TODO: Implement the following functions based on the descriptions.

def reverse_list(lst):
    """
    Reverses the given list.
    :param lst: List of integers.
    :return: A list with elements in reverse order.
    """
    return lst[::-1]
print(reverse_list([1,2,3,4]))

def count_occurrences(lst, element):
    """
    Counts how many times the given element appears in the list.
    :param lst: List of elements.
    :param element: Element to count.
    :return: Integer count of occurrences.
    """
    return lst.count(element)
print(count_occurrences([1, 2, 2, 3],2))

def get_keys_with_value(dct, value):
    """
    Returns a list of keys that have the given value in the dictionary.
    :param dct: Dictionary to search.
    :param value: Value to find.
    :return: List of keys.
    """
    list=[]
    for v in dct:
        if dct[v]==value:
            list.append(v)
    return list


def merge_sorted_lists(lst1, lst2):
    """
    Merges two sorted lists into one sorted list.
    :param lst1: First sorted list.
    :param lst2: Second sorted list.
    :return: Merged sorted list.
    """
    lst1,lst2=sorted(lst1),sorted(lst2)
    
    return sorted(lst1+lst2)
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))

def find_second_largest(numbers):
    """
    Finds the second largest number in a list.
    :param numbers: List of integers.
    :return: The second largest integer.
    """
    numbers.remove(max(numbers))
    if len(numbers)<2 or numbers.count(numbers[0])==len(numbers):
        return None
        
    return max(numbers)
print(find_second_largest([42, 42, 42]))
def is_anagram(str1, str2):
    """
    Checks if two strings are anagrams.
    
    An anagram is a word or phrase formed by rearranging the letters of another,
    using all the original letters exactly once. For example, "listen" and "silent"
    are anagrams because they use the same letters in a different order.
    
    :param str1: First string.
    :param str2: Second string.
    :return: True if the strings are anagrams, False otherwise.
    """
    if sorted(str2)==sorted(str1):
        return True
    else: 
        return False


def flatten_list(nested_list):
    """
    Flattens a nested list into a single list.
    :param nested_list: List of lists.
    :return: A flat list with all elements.
    """
    flat=[]
    for inner in nested_list:
        for x in inner:
            flat.append(x)
    return flat


def remove_duplicates(lst):
    """
    Removes duplicates from the list while maintaining order.
    :param lst: List of elements.
    :return: List without duplicates.
    """
    return list(set(lst))

def find_common_elements(lst1, lst2):
    """
    Finds common elements between two lists.
    :param lst1: First list.
    :param lst2: Second list.
    :return: List of common elements.
    """
    com=[]
    for i in lst1:
        for x in lst2:
            if x==i:
                com.append(x)
    return com