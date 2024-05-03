from Charter import Charter
class Enemy:
    def __init__(self,name,health):
        self.name = name
        self.health = health
    def takeDamage(self):
        self.health -= 4
    def attack(self,Charter):
        Charter.health -= 4
    def __str__(self):
        return f"""
        Name:{self.name}
        Heal:{self.health}
        """


    