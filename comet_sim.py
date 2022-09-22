import random

SAMPLE_SIZE = 100000

class Doggo():
    def __init__(self, barb_class_num, barb_class_active_num, floating_mana_for_bolt):
        # initial card state
        self.loyalty = 5
        self.activations = 1
        
        # initial board state
        self.squirrels = 0
        self.spell = 0
        self.damage = 0
        self.rolls_boosting_squirrels = 0

        # extra information
        self.reroll_count = barb_class_num
        self.bonus_per_roll = 2 * barb_class_active_num
        self.mana = floating_mana_for_bolt

    def activate(self):
        # count activation
        self.activations -= 1

        # roll dice w/ advantage
        num_rolls = 1 + self.reroll_count
        die_roll = max([random.randint(1,6) for i in range(num_rolls)])

        # determine outcome
        if die_roll in [1, 2]:
            self.loyalty += 2
            self.squirrels += 2
        if die_roll in [3]:
            self.loyalty -= 1
            self.spell += 1
        if die_roll in [4, 5]:
            self.damage += self.loyalty
            self.loyalty -= 2
        if die_roll in [6]:
            self.loyalty
            self.activations += 2
        
        # if squirrels exist, increment rolls boosting squirrels
        if self.squirrels > 0:
            self.rolls_boosting_squirrels += 1
        
        return
    
    def final_damage(self):
        final_damage  = self.damage
        final_damage += self.squirrels
        final_damage += self.rolls_boosting_squirrels * self.bonus_per_roll
        final_damage += min(self.mana, self.spell) * 3  # assumes lightning bolt
        return final_damage


results = []
for i in range(SAMPLE_SIZE):
    dog = Doggo(0, 0, 0)
    while dog.activations > 0 and dog.loyalty > 0:
        dog.activate()
    results.append(dog.final_damage())

print(sum(results) / len(results))