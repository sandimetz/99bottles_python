class Bottles:
  def song(self):
    return self.verses(99, 0)

  def verses(self, upper, lower):
    return '\n'.join(self.verse(i) for i in range(upper, lower-1, -1))

  def verse(self, number):
    match number:
      case 0:
        return (
          f'{self.quantity(number).capitalize()} {self.container(number)}'
            ' of beer on the wall, '
          f'{self.quantity(number)} {self.container(number)} of beer.\n'
          f'Go to the store and buy some more, '
          f'99 bottles of beer on the wall.\n'
        )
      case _:
        return (
          f'{self.quantity(number).capitalize()} {self.container(number)}'
            ' of beer on the wall, '
          f'{self.quantity(number)} {self.container(number)} of beer.\n'
          f'Take {self.pronoun(number)} down and pass it around, '
          f'{self.quantity(number-1)} {self.container(number-1)}'
            ' of beer on the wall.\n'
        )

  def quantity(self, number):
    if number == 0:
      return 'no more'
    return str(number)

  def container(self, number):
    if number == 1:
      return 'bottle'
    return 'bottles'

  def pronoun(self, number):
    if number == 1:
      return 'it'
    return 'one'
