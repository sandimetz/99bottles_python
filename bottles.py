class Bottles:
  def verse(self, number):
    if (number == 2):
      return (
        '2 bottles of beer on the wall, '
        '2 bottles of beer.\n'
        'Take one down and pass it around, '
        '1 bottle of beer on the wall.\n'
      )
    return (
      f'{number} bottles of beer on the wall, '
      f'{number} bottles of beer.\n'
      f'Take one down and pass it around, '
      f'{number-1} bottles of beer on the wall.\n'
    )
