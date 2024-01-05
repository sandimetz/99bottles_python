class Bottles:
  def song(self):
    return self.verses(99, 0)

  def verses(self, upper, lower):
    return '\n'.join(self.verse(i) for i in reversed(range(lower, upper + 1)))

  def verse(self, number):
    return (
      f'{self.quantity(number).capitalize()} {self.container(number)}'
      ' of beer on the wall, '
      f'{self.quantity(number)} {self.container(number)} of beer.\n'
      f'{self.action(number)}, '
      f'{self.quantity(self.successor(number))} '
      f'{self.container(self.successor(number))}'
      ' of beer on the wall.\n'
    )

  def quantity(self, number):
    return BottleNumber(number).quantity()

  def container(self, number):
    return BottleNumber(number).container()

  def action(self, number):
    return BottleNumber(number).action()

  def pronoun(self, number):
    return BottleNumber(number).pronoun(number)

  def successor(self, number):
    return BottleNumber(number).successor(number)


class BottleNumber:
  def __init__(self, number):
    self._number = number

  def quantity(self):
    if self._number == 0:
      return 'no more'
    return str(self._number)

  def container(self):
    if self._number == 1:
      return 'bottle'
    return 'bottles'

  def action(self):
    if self._number == 0:
      return 'Go to the store and buy some more'
    return f'Take {self.pronoun(self._number)} down and pass it around'

  def pronoun(self, number='FIXME'):
    if self._number == 1:
      return 'it'
    return 'one'

  def successor(self, number):
    if number == 0:
      return 99
    return number - 1
