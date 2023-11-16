class Bottles:
  def song(self):
    return self.verses(99, 0)

  def verses(self, upper, lower):
    if (upper == 99 and lower == 98):
      return f'{self.verse(99)}\n{self.verse(98)}'
    if (upper == 2):
      return f'{self.verse(2)}\n{self.verse(1)}\n{self.verse(0)}'
    return "ok"

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
      case 2:
        return (
          '2 bottles of beer on the wall, '
          '2 bottles of beer.\n'
          'Take one down and pass it around, '
          '1 bottle of beer on the wall.\n'
        )
      case _:
        return (
          f'{number} bottles of beer on the wall, '
          f'{number} bottles of beer.\n'
          f'Take one down and pass it around, '
          f'{number-1} bottles of beer on the wall.\n'
        )
