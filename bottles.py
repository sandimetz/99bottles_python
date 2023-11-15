class Bottles:
  def verse(self, number):
    return (
      f'{number} bottles of beer on the wall, '
      f'{number} bottles of beer.\n'
      f'Take one down and pass it around, '
      f'{number-1} bottle{"s" if number-1 != 1 else ""} of beer on the wall.\n'
    )
