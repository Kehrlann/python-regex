import unittest
import re
from url import regexp_url


class TestRegexUrl(unittest.TestCase):

    def test_regex_url(self):
        cases = [
            ('http://www.google.com/a/b', {'proto': 'http', 'user': None,
                                           'password': None, 'hostname': 'www.google.com', 'port': None, 'path': 'a/b'}),
            ('HttPS://www.google.com:8080/a/b', {'proto': 'HttPS', 'user': None,
                                                 'password': None, 'hostname': 'www.google.com', 'port': '8080', 'path': 'a/b'}),
            ('http://user@www.google.com/a/b', {'proto': 'http', 'user': 'user',
                                                'password': None, 'hostname': 'www.google.com', 'port': None, 'path': 'a/b'}),
            ('FTP://username:hispass@www.google.com/', {'proto': 'FTP', 'user': 'username',
                                                        'password': 'hispass', 'hostname': 'www.google.com', 'port': None, 'path': ''}),
            ('ssh://missing.ending.slash', None),
            ('gopher://unsupported.proto.col/', None),
            ('http:///missing/hostname/', None)
        ]
        for text, expected in cases:
            match = re.match(regexp_url, text)
            if expected:
                self.assertTrue(match, f"\"{text}\" should match")
                groups = match.groupdict()
                self.assertEqual(
                    groups, expected,
                    f"\"{text}\" should match {expected}, but was {groups}"
                )
            else:
                self.assertFalse(match, f"\"{text}\" should not match")


if __name__ == '__main__':
    unittest.main()
