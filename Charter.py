class Charter:

    def __init__(self, name):
        self.name = name
    
    level = 0 

    maxHealth     = 100
    current_Health = 100

    max_mana     = 100
    current_mana = 100

    alive = True

    def useSpell(self):
        self.current_mana -=  5
        print("Use Spell")
    
    def setMaxHealth():
        if(self.level == 0):
            maxHealth = 100
        else:
            maxHealth = self.level * 100

# allows us to see all vars at once
    def __str__(self):
        return f"""
        name:           {self.name}\n
        level:          {self.level}
        current HP:     {self.current_Health}
        current mana:   {self.current_mana}
        max HP:         {self.maxHealth}
        max mana:       {self.max_mana}
        """
#testing
bob = Charter("bob")
print(bob)
bob.useSpell()
print(bob)