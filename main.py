from Charter import Charter
from Enemy import Enemy
bob = Charter('bob 2')
en1 = Enemy('Enemy 1',12)
print(bob)
print(en1)
bob.useSpell(en1)
print(bob)
print(en1)

