import unittest
import re
from phone import regexp_phone


class TestRegexPhone(unittest.TestCase):

    def test_regex_phone(self):
        cases = [
            ("0123456789", '123456789'),
            ("01234567890", None),
            ("012345678", None),
            ("1234567890", None),
            ("+33123456789", '123456789'),
            ("+3312345678", None),
            ("+330123456789", None),
        ]
        for text, expected in cases:
            match = re.match(regexp_phone, text)
            if expected:
                self.assertTrue(match, f"\"{text}\" should match")
                groups = match.groupdict()
                self.assertEqual(
                    groups['number'], expected,
                    f"\"{text}\" should have \"number\" group that is \"{expected}\", but was \"{groups['number']}\""
                )
            elif expected and not match:
                self.assertFalse(match, f"\"{text}\" should not match")


if __name__ == '__main__':
    unittest.main()
