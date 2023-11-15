import unittest
from bottles import Bottles


class BottlesTest(unittest.TestCase):
  def test_the_first_verse(self):
    expected = (
      '99 bottles of beer on the wall, '
      '99 bottles of beer.\n'
      'Take one down and pass it around, '
      '98 bottles of beer on the wall.\n'
    )
    self.assertEqual(Bottles().verse(99), expected)

  def test_another_verse(self):
    expected = (
      '3 bottles of beer on the wall, '
      '3 bottles of beer.\n'
      'Take one down and pass it around, '
      '2 bottles of beer on the wall.\n'
    )
    self.assertEqual(Bottles().verse(3), expected)

  def test_verse_2(self):
    expected = (
      '2 bottles of beer on the wall, '
      '2 bottles of beer.\n'
      'Take one down and pass it around, '
      '1 bottle of beer on the wall.\n'
    )
    self.assertEqual(Bottles().verse(2), expected)
