import unittest
import re
from pythonid import regexp_pythonid


class TestRegexPythonId(unittest.TestCase):

    def test_regex_pythonid(self):
        cases = [
            ('a', True),
            ('_', True),
            ('__', True),
            ('-', False),
            ('aa1', True),
            ('A1a', True),
            ('1Aa', False),
            ('-aa1', False),
            ('_aa1', True),
            ('a-a1', True),
            ('a_a1', True),
            ('aa-1', True),
            ('aa_1', True),
            ('-A1a', False),
            ('_A1a', True),
            ('A-1a', True),
            ('A_1a', True),
            ('A1-a', True),
            ('A1_a', True),
            ('-1Aa', False),
            ('_1Aa', True),
            ('1-Aa', False),
            ('1_Aa', False),
            ('1A-a', False),
            ('1A_a', False)
        ]
        for text, expected in cases:
            self.assertEqual(
                re.match(regexp_pythonid, text) is not None,
                expected,
                f"\"{text}\" should{'' if expected else ' not'} match"
            )


if __name__ == '__main__':
    unittest.main()
