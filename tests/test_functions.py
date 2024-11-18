import unittest

from functions import (count_occurrences, find_common_elements,
                       find_second_largest, flatten_list, get_keys_with_value,
                       is_anagram, merge_sorted_lists, remove_duplicates,
                       reverse_list)


class TestDataStructures(unittest.TestCase):
    def test_reverse_list(self):
        self.assertEqual(reverse_list([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse_list([]), [])
        self.assertEqual(reverse_list([42]), [42])

    def test_count_occurrences(self):
        self.assertEqual(count_occurrences([1, 2, 2, 3], 2), 2)
        self.assertEqual(count_occurrences([1, 1, 1, 1], 1), 4)
        self.assertEqual(count_occurrences([], 5), 0)

    def test_get_keys_with_value(self):
        self.assertEqual(get_keys_with_value({'a': 1, 'b': 2, 'c': 1}, 1), ['a', 'c'])
        self.assertEqual(get_keys_with_value({'a': 3, 'b': 3, 'c': 3}, 3), ['a', 'b', 'c'])
        self.assertEqual(get_keys_with_value({}, 5), [])

    def test_merge_sorted_lists(self):
        self.assertEqual(merge_sorted_lists([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(merge_sorted_lists([], [1, 2]), [1, 2])
        self.assertEqual(merge_sorted_lists([], []), [])

    def test_find_second_largest(self):
        self.assertEqual(find_second_largest([1, 2, 3, 4]), 3)
        self.assertEqual(find_second_largest([42, 42, 42]), None)
        self.assertEqual(find_second_largest([5]), None)

    def test_is_anagram(self):
        self.assertTrue(is_anagram("listen", "silent"))
        self.assertTrue(is_anagram("anagram", "nagaram"))
        self.assertFalse(is_anagram("hello", "world"))

    def test_flatten_list(self):
        self.assertEqual(flatten_list([[1, 2], [3, 4]]), [1, 2, 3, 4])
        self.assertEqual(flatten_list([]), [])
        self.assertEqual(flatten_list([[1], [], [2, 3]]), [1, 2, 3])

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 3]), [1, 2, 3])
        self.assertEqual(remove_duplicates([1, 1, 1, 1]), [1])
        self.assertEqual(remove_duplicates([]), [])

    def test_find_common_elements(self):
        self.assertEqual(find_common_elements([1, 2, 3], [3, 4, 5]), [3])
        self.assertEqual(find_common_elements([1, 2], [3, 4]), [])
        self.assertEqual(find_common_elements([], [1, 2]), [])

if __name__ == "__main__":
    unittest.main()
