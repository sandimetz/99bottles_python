class Bottles:
  def song(self):
    return self.verses(99, 0)

  def verses(self, upper, lower):
    return '\n'.join(self.verse(i) for i in range(upper, lower-1, -1))

  def verse(self, number):
    match number:
      case 0:
        return (
          'No more bottles of beer on the wall, '
          'no more bottles of beer.\n'
          'Go to the store and buy some more, '
          '99 bottles of beer on the wall.\n'
        )
      case 1:
        return (
          '1 bottle of beer on the wall, '
          '1 bottle of beer.\n'
          'Take it down and pass it around, '
          'no more bottles of beer on the wall.\n'
        )
      case _:
        return (
          f'{number} bottles of beer on the wall, '
          f'{number} bottles of beer.\n'
          f'Take one down and pass it around, '
          f'{number-1} {self.container(number-1)} of beer on the wall.\n'
        )

  def container(self, number):
    if number == 1:
      return 'bottle'
    return 'bottles'
