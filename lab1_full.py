class Player:
    def __init__(self, name,level, hp):
        self.name = name
        self.lvl = level
        self.hp = hp
        self.weapon = []
        self.armor = []
    
    def show_info(self):
        print(f'Player Infomation\nName: {self.name}\nLevel: {self.lvl}\nHp: {self.hp}\nWeapon: {self.weapon[0]} Damage: {self.weapon[1]}\nArmor: {self.armor[0]} Defend: {self.armor[1]}\n----------------------------------------------------------------')
    
    def equip_weapon(self, Weapon):
        self.weapon.append(Weapon.name)
        self.weapon.append(Weapon.dmg)
    
    def equip_armor(self, Armor):
        self.armor.append(Armor.name)
        self.armor.append(Armor.defend)
    
class Guild:
    def __init__(self, name):
        self.name = name
        self.leader = None
        self.member = []
    
    def show_guild(self):
        res = ''
        for i in self.member:
            res += i.name + ', '
        print(f'Guild Information\nName: {self.name}\nLeader: {self.leader.name}\nMember: {res[:-2]} \n-----------------------------')
   
    def join_guild(self, Player):
        if self.leader == None:
            self.leader = Player
        else:
            self.member.append(Player)
        
class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.dmg = damage
        
class Armor:
    def __init__(self, name, defend):
        self.name = name
        self.defend = defend
        
#player
player1 = Player('king', 1, 100)
player2 = Player('tang', 10, 1000)
player3 = Player('Khanun', 100, 10000)

weapon1 = Weapon('Iron Sword', 20)
weapon2 = Weapon('Spear', 35)
weapon3 = Weapon('Cannon', 100)

armor1 = Armor('Lether Armor', 10)
armor2 = Armor('Iron Armor', 20)
armor3 = Armor('Diamond Armor', 50)


#main
player1.equip_weapon(weapon1)
player1.equip_armor(armor2)

player2.equip_weapon(weapon2)
player2.equip_armor(armor1)

player3.equip_weapon(weapon3)
player3.equip_armor(armor2)

guild1 = Guild('test1')


guild1.join_guild(player1)
guild1.join_guild(player2)
guild1.join_guild(player3)
guild1.show_guild()

