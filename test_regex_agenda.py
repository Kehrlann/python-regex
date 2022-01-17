import unittest
import re
from agenda import regexp_agenda


class TestRegexAgenda(unittest.TestCase):

    def test_regex_agenda(self):
        cases = [
            ('Daniel:Durand', {'prenom': 'Daniel', 'nom': 'Durand'}),
            ('Jean:Dupont:', {'prenom': 'Jean', 'nom': 'Dupont'}),
            ('Jean:Dupont::', None),
            (':Dupontel:', {'prenom': '', 'nom': 'Dupontel'}),
            ('Jean-Noël:Dupont-Nemours',
             {'prenom': 'Jean-Noël', 'nom': 'Dupont-Nemours'}),
            ('Charles-Henri:Du Pré', None),
            ('Charles Henri:DuPré', None)
        ]
        for text, expected in cases:
            match = re.match(regexp_agenda, text)
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
