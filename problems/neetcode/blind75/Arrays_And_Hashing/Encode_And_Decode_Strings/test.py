import unittest
from solution import Solution

class TestEncodeAndDecodeStrings(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()

    def test_encode_and_decode_strings_example1(self):
        input = ["Hello", "World"]
        expected_input = "6$Hello6$World"
        result_input = self.solution.encode(input)

        expected_output = input
        result_output = self.solution.decode(expected_input)

        self.assertEqual(expected_input, result_input)
        self.assertEqual(expected_output, result_output)

    def test_encode_and_decode_strings_example2(self):
        input = [""]
        expected_input = "1$"
        result_input = self.solution.encode(input)

        expected_output = input
        result_output = self.solution.decode(expected_input)

        self.assertEqual(expected_input, result_input)
        self.assertEqual(expected_output, result_output)

    def test_encode_and_decode_strings_one_word(self):
        input = ["aaaaaaaa"]
        expected_input = "9$aaaaaaaa"
        result_input = self.solution.encode(input)

        expected_output = input
        result_output = self.solution.decode(expected_input)

        self.assertEqual(expected_input, result_input)
        self.assertEqual(expected_output, result_output)

    def test_encode_and_decode_strings_many_words(self):
        input = ["a", "b", "c", "d", "e"]
        expected_input = "2$a2$b2$c2$d2$e"
        result_input = self.solution.encode(input)

        expected_output = input
        result_output = self.solution.decode(expected_input)

        self.assertEqual(expected_input, result_input)
        self.assertEqual(expected_output, result_output)

    def test_encode_and_decode_strings_empty_list(self):
        input = []
        expected_input = ""
        result_input = self.solution.encode(input)

        expected_output = input
        result_output = self.solution.decode(expected_input)

        self.assertEqual(expected_input, result_input)
        self.assertEqual(expected_output, result_output)

    # def test_encode_and_decode_strings_example1(self):
    #     input = ["Hello", "World"]
    #     expected_input = "🦆Hello🦆World"
    #     result_input = self.solution.encode(input)

    #     expected_output = input
    #     result_output = self.solution.decode(expected_input)

    #     self.assertEqual(expected_input, result_input)
    #     self.assertEqual(expected_output, result_output)

    # def test_encode_and_decode_strings_example2(self):
    #     input = [""]
    #     expected_input = "🦆"
    #     result_input = self.solution.encode(input)

    #     expected_output = input
    #     result_output = self.solution.decode(expected_input)

    #     self.assertEqual(expected_input, result_input)
    #     self.assertEqual(expected_output, result_output)

    # def test_encode_and_decode_strings_one_word(self):
    #     input = ["aaaaaaaa"]
    #     expected_input = "🦆aaaaaaaa"
    #     result_input = self.solution.encode(input)

    #     expected_output = input
    #     result_output = self.solution.decode(expected_input)

    #     self.assertEqual(expected_input, result_input)
    #     self.assertEqual(expected_output, result_output)

    # def test_encode_and_decode_strings_many_words(self):
    #     input = ["a", "b", "c", "d", "e"]
    #     expected_input = "🦆a🦆b🦆c🦆d🦆e"
    #     result_input = self.solution.encode(input)

    #     expected_output = input
    #     result_output = self.solution.decode(expected_input)

    #     self.assertEqual(expected_input, result_input)
    #     self.assertEqual(expected_output, result_output)

    # def test_encode_and_decode_strings_empty_list(self):
    #     input = []
    #     expected_input = ""
    #     result_input = self.solution.encode(input)

    #     expected_output = input
    #     result_output = self.solution.decode(expected_input)

    #     self.assertEqual(expected_input, result_input)
    #     self.assertEqual(expected_output, result_output)

if __name__ == "__main__":
    unittest.main()