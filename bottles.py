class Bottles:
  def song(self):
    return self.verses(99, 0)

  def verses(self, upper, lower):
    return '\n'.join(self.verse(i) for i in range(upper, lower-1, -1))

  def verse(self, number):
    return (
      f'{self.quantity(number).capitalize()} {self.container(number)}'
        ' of beer on the wall, '
      f'{self.quantity(number)} {self.container(number)} of beer.\n'
      f'{self.action(number)}, '
      f'{self.quantity(self.successor(number))} {self.container(self.successor(number))}'
        ' of beer on the wall.\n'
    )

  def quantity(self, number):
    return BottleNumber(number).quantity()

  def container(self, number):
    return BottleNumber(number).container()

  def action(self, number):
    return BottleNumber(number).action()

  def successor(self, number):
    return BottleNumber(number).successor(number)

class BottleNumber:
  def __init__(self, number):
    self.number = number

  def quantity(self):
    if self.number == 0:
      return 'no more'
    return str(self.number)

  def container(self):
    if self.number == 1:
      return 'bottle'
    return 'bottles'

  def action(self):
    if self.number == 0:
        return 'Go to the store and buy some more'
    return f'Take {self.pronoun()} down and pass it around'

  def pronoun(self):
    if self.number == 1:
      return 'it'
    return 'one'

  def successor(self, number):
    if self.number == 0:
      return 99
    return self.number - 1
