from common.input_handling import import_input_file, read_input
import unittest


def solution_part_a(input_txt: str):
    result = 1
    lines = input_txt.splitlines()
    for line in lines:
        pass
    return result


def solution_part_b(input_txt: str):
    result = 1
    lines = input_txt.splitlines()
    for line in lines:
        pass
    return result


class Test(unittest.TestCase):
    def test_example_a(self):
        input_example_1 = """\
        """
        expected = 1
        result = solution_part_a(input_example_1)
        self.assertEqual(result, expected, "Example 1: Expected is " + str(expected))

    def test_solution_a(self):
        input_file = read_input(__file__)
        expected = 1
        result = solution_part_a(input_file)
        self.assertEqual(result, expected, "Riddle a: Expected is " + str(expected))

    def test_example_b(self):
        input_example_2 = """\
        """
        expected = 1
        result = solution_part_a(input_example_2)
        self.assertEqual(result, expected, "Example 2: Expected is " + str(expected))

    def test_solution_b(self):
        input_file = read_input(__file__)
        expected = 1
        result = solution_part_a(input_file)
        self.assertEqual(result, expected, "Riddle b: Expected is " + str(expected))
