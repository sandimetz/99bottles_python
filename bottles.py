class Bottles:
  def song(self):
    return self.verses(99, 0)

  def verses(self, upper, lower):
    return '\n'.join(self.verse(i) for i in reversed(range(lower, upper + 1)))

  def verse(self, number):
    match number:
      case 0:
        return (
          f'{self.quantity(number).capitalize()} {self.container(number)}'
          ' of beer on the wall, '
          f'{self.quantity(number)} {self.container(number)} of beer.\n'
          f'{self.action(number)}, '
          f'{self.quantity(99)} {self.container(number-1)}'
          ' of beer on the wall.\n'
        )
      case _:
        return (
          f'{str(self.quantity(number)).capitalize()} {self.container(number)}'
          ' of beer on the wall, '
          f'{self.quantity(number)} {self.container(number)} of beer.\n'
          f'{self.action(number)}, '
          f'{self.quantity(self.successor(number))} {self.container(number-1)}'
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

  def action(self, number):
    if number == 0:
      return 'Go to the store and buy some more'
    return f'Take {self.pronoun(number)} down and pass it around'

  def pronoun(self, number):
    if number == 1:
      return 'it'
    return 'one'

  def successor(self, number):
    return number - 1
