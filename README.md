# WordscapesSolver
A simple solver for Wordscapes. Not always perfect, but it gets the job done.

# Installation
```commandline
pip install https://github.com/HoqueUM/WordscapesSolver.git
```
# Example Usage
```python
from WordscapesSolver import WordscapesSolver

solver = WordscapesSolver()

letters = 'abcdefg'
solutions = solver.generate_solutions(letters=letters)
output = solver.format_output(solutions)
print(output)
```
# Output
```commandline
Words of length 3:
ace
ade
age
bac
bad
bae
bag
bed
beg
cab
cad
cag
dab
dae
dag
deb
deg
fad
fae
fed
gab
gad
ged

Words of length 4:
abed
aged
bade
bead
cade
cage
dace
deaf
ecad
egad
face
fade
fage
gade

Words of length 5:
badge
begad
cadge
caged
faced
fadge
```
# Disclaimer
This currently uses the nltk words module, which is not a comprehensive english dictionary. Plural words (cars, dogs, beds, etc) are not printed. The same goes for borrowed words (taco, pinot, crepe, etc). I am working on transitioning to the Wordnik API directly, which is what Wordscapes uses. For now, however, this works for most cases.
