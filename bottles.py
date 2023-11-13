class Bottles:
  def song(self):
    return self.verses(99, 0)

  def verses(self, hi, lo):
    return '\n'.join(self.verse(n) for n in range(hi, lo - 1, -1))

  def verse(self, n):
    return (
      f'{"No more" if n == 0 else n} bottle{"s" if n != 1 else ""}'
      f' of beer on the wall, '
      f'{"no more" if n == 0 else n} bottle{"s" if n != 1 else ""} of beer.\n' +
      (f'Go to the store and buy some more, ' if n == 0 else f'Take {"one" if n != 1 else "it"} down and pass it around, ') +
      f'{"99" if n - 1 < 0 else ("no more" if n - 1 == 0 else n - 1)} bottle{"s" if n - 1 != 1 else ""}'
      f' of beer on the wall.\n'
    )
