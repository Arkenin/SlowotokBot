
import re

class Solver():

    def __init__(self):
        #self.all_words = set(word.rstrip('\n') for word in open('C:/Users/arkni/Desktop/Pracka/PY - kodowanie/2022/slowotok/slowa.txt'))
        self.all_words = set(word.rstrip('\n') for word in open('data/selected.txt'))

    def splitter(self, text, n = 4):
        return [text[i:i+n] for i in range(0,len(text),n)]

    def solve(self, letters):
        grid = self.splitter(letters)
        alphabet = ''.join(set(letters))
        bogglable = re.compile('[' + alphabet + ']{3,}$', re.I).match
        words = set(word for word in self.all_words if bogglable(word))

        prefixes = set(word[:i] for word in words
            for i in range(2, len(word)+1))

        nrows, ncols = len(grid), len(grid[0])


        def solve():
            for y, row in enumerate(grid):
                for x, letter in enumerate(row):
                    for result in extending(letter, ((x, y),)):
                        yield result[0]

        def extending(prefix, path):
            if prefix in words:
                yield (prefix, path)
            for (nx, ny) in neighbors(*path[-1]):
                if (nx, ny) not in path:
                    prefix1 = prefix + grid[ny][nx]
                    if prefix1 in prefixes:
                        for result in extending(prefix1, path + ((nx, ny),)):
                            yield result

        def neighbors(x, y):
            for nx in range(max(0, x-1), min(x+2, ncols)):
                for ny in range(max(0, y-1), min(y+2, nrows)):
                    yield (nx, ny)

        yield from solve()

# Print a maximal-length word and its path:

'''
solver = Solver()
lista = list(solver.solve('JNPJYYJEPZSRAWFT'.lower()))
print(sorted(lista, key=len, reverse=True))

pass
'''