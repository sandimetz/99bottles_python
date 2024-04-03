class BottleVerse:
  @classmethod
  def lyrics(cls, number):
    return cls(BottleNumber(number))._lyrics()

  def __init__(self, bottle_number):
    self._bottle_number = bottle_number

  def _lyrics(self):
    return (
      f'{self._bottle_number} of beer on the wall, '.capitalize() +
      f'{self._bottle_number} of beer.\n'
      f'{self._bottle_number.action()}, '
      f'{self._bottle_number.successor()} of beer on the wall.\n'
    )


class CountdownSong:
  def __init__(self, verse_template=BottleVerse, max=99, min=0):
    self._verse_template = verse_template

  def song(self):
    return self.verses(99, 0)

  def verses(self, upper, lower):
    return '\n'.join(self.verse(i) for i in reversed(range(lower, upper + 1)))

  def verse(self, number):
    return self._verse_template.lyrics(number)


class BottleNumber:
  def __new__(cls, number):
    match number:
      case 0:
        cls = BottleNumber0
      case 1:
        cls = BottleNumber1
      case 6:
        cls = BottleNumber6
      case _:
        cls = BottleNumber
    return super().__new__(cls)

  def __init__(self, number):
    self._number = number

  def __str__(self):
    return f'{self.quantity()} {self.container()}'

  def quantity(self):
    return str(self._number)

  def container(self):
    return 'bottles'

  def action(self):
    return f'Take {self.pronoun()} down and pass it around'

  def pronoun(self):
    return 'one'

  def successor(self):
    return BottleNumber(self._number - 1)


class BottleNumber0(BottleNumber):
  def quantity(self):
    return 'no more'

  def action(self):
    return 'Go to the store and buy some more'

  def successor(self):
    return BottleNumber(99)


class BottleNumber1(BottleNumber):
  def container(self):
    return 'bottle'

  def pronoun(self):
    return 'it'


class BottleNumber6(BottleNumber):
  def quantity(self):
    return '1'

  def container(self):
    return 'six-pack'
