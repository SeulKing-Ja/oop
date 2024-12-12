class Player:
    def __init__(self, name, level, hp):
        self.name = name
        self.level = level
        self.hp = hp
        self.weapon_owner = []
        self.armor_owner = []
        self.guild_member = []
        
    def info(self):
        print(f'Name: {self.name} \nLevel: {self.level} \nHp: {self.hp} \nWeapon: {self.weapon_owner[0]} \nDamage: {self.weapon_owner[1]}\nArmor: {self.armor_owner[0]} Defend: {self.armor_owner[1]}\nGuild: {self.guild_member[0]} Position: {self.guild_member[1]} \n ------------------------------')
         
    def walk(self):
        pass
    
    def sprint(self):
        pass

    def punch(self):
        pass
    
    def hp_regen(self):
        pass
    
    def mana_regen(self):
        pass
    
    def level_up(self):
        pass
    
class Weapon:
    def __init__(self, name, type, damage):
        self.name = name
        self.type = type
        self.dmg = damage
    
    def attack(self):
        pass

    def attack_range(self):
        pass

    def skill(self):
        pass
    
    def skill_slots(self):
        pass

class Armor:
    def __init__(self, name, defend):
        self.name = name
        self.defend = defend
    
    def endurance(self):
        pass
    
    def element_def(self):
        pass
    
class Guild():
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def create_guild(self):
        pass
    
    def join_guild(self):
        pass
    
    def permission_manage(self):
        pass
    
    def delete_guild(self):
        pass

#----- Player
player1 = Player('Hero_01', 1, 100)
player2 = Player('Archer_01', 2, 120)
player3 = Player('Wizard_01', 50, 1100)

#----- Weapon
weapon1 = Weapon('Iron Sword', 'Melee', 10)
weapon2 = Weapon('Wooden Bow', 'Range', 8)
weapon3 = Weapon('Staff', 'Magic', 12)

player1.weapon_owner.append(weapon1.name)
player1.weapon_owner.append(weapon1.dmg)
player2.weapon_owner.append(weapon2.name)
player2.weapon_owner.append(weapon2.dmg)
player3.weapon_owner.append(weapon3.name)
player3.weapon_owner.append(weapon3.dmg)

#----- Armor  
armor1 = Armor('Lether Armor', 5)
armor2 = Armor('Chain Mail', 10)
armor3 = Armor('Hood', 2)

player1.armor_owner.append(armor1.name)
player1.armor_owner.append(armor1.defend)
player2.armor_owner.append(armor2.name)  
player2.armor_owner.append(armor2.defend)
player3.armor_owner.append(armor3.name)  
player3.armor_owner.append(armor3.defend)

#----- Guild
guild1 = Guild('Newbie Eiei', 'Member')
guild2 = Guild('Advance Eiei', 'Member')

player1.guild_member.append(guild1.name)
player1.guild_member.append(guild1.position)
player2.guild_member.append(guild1.name)
player2.guild_member.append(guild1.position)
player3.guild_member.append(guild2.name)
player3.guild_member.append(guild2.position)

player2.guild_member[1] = 'Leader'
player3.guild_member[1] = 'Leader'

#----- Test
player1.info()
player2.info()
player3.info()
