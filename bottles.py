class Bottles:
  def verse(self, number):
    if (number == 99):
      n = 99
    else:
      n = 3

    return (
      f'{n} bottles of beer on the wall, '
      f'{n} bottles of beer.\n'
      f'Take one down and pass it around, '
      f'{n-1} bottles of beer on the wall.\n'
    )
