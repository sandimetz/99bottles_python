class Bottles:
  def song(self):
    return self.verses(99, 0)

  def verses(self, upper, lower):
    return '\n'.join(self.verse(i) for i in reversed(range(lower, upper + 1)))

  def verse(self, number):
    bottle_number = BottleNumber(number)

    return (
      f'{bottle_number.quantity().capitalize()} {bottle_number.container()}'
      ' of beer on the wall, '
      f'{bottle_number.quantity()} {bottle_number.container()} of beer.\n'
      f'{bottle_number.action()}, '
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

  def successor(self, number):
    return BottleNumber(number).successor()


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
    return f'Take {self.pronoun()} down and pass it around'

  def pronoun(self):
    if self._number == 1:
      return 'it'
    return 'one'

  def successor(self):
    if self._number == 0:
      return 99
    return self._number - 1
