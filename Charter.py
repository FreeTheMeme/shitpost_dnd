class Charter:

        
    
    def __init__(self, name, level=1):
        self.name = name
        self.level = level
        self.max_health = self.level * 64
        self.current_health = self.max_health
        self.max_mana = self.level * 64
        self.current_mana = self.max_mana
        self.alive = True

#actions 
    def useSpell(self):
        self.current_mana -=  4
        print("Use Spell")
    def atttack(self):
        self.current_health -= 4
        print("attact")
    
        


# allows us to see all vars at once
    def __str__(self):
        return f"""
        name:           {self.name}\n
        level:          {self.level}
        current HP:     {self.current_health}
        current mana:   {self.current_mana}
        max HP:         {self.max_health}
        max mana:       {self.max_mana}
        """
#testing
# bob = Charter("bob")
# print(bob)
# bob.useSpell()
# print(bob)