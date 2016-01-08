from random import randint

class Character(object):
    def __init__(self,name,hp,atk,defence,exp,coin):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defence = defence
        self.exp = exp
        self.coin = coin
        self.x = 0
        self.y = 0
        
    def attack(self,monster):
        if self.atk < monster.defence:
            return '%s was not hurt their defence is too high' %(monster.name)
        else:
            monster.hp = monster.hp -(self.atk - monster.defence)
        if monster.hp < 1:
            self.exp = self.exp + monster.exp
            self.coin = self.coin + monster.coin
            return '%s died and gave %s exp and %s coins.' %(monster.name,monster.exp,monster.coin)

        return '%s was attacked for %s HP = %s' %(monster.name,(self.atk-monster.defence),monster.hp)

    def run(self,monster):
        chance = randint(1,2)
        if chance%2 == 0:
            return '%s ran sucessfully.' %(self.name)
        else:
            return '%s was too fast %s could not get away.' %(monster.name,self.name)

    def walkR(self):
        self.x = self.x + 1
        area = randint(0,1)
        if  area == 1:
            self.monster = Monster()
            self.battle(self.monster)
        return 'coord(%s,%s)' %(self.x,self.y)
    def walkL(self):
        self.x = self.x - 1
        area = randint(0,1)
        if  area == 1:
            self.monster = Monster()
            self.battle(self.monster)
        return 'coord(%s,%s)' %(self.x,self.y)
    def walkU(self):
        self.y = self.y + 1
        area = randint(0,1)
        if  area == 1:
            self.monster = Monster()
            self.battle(self.monster)
        return 'coord(%s,%s)' %(self.x,self.y)
    def walkD(self):
        self.y = self.y - 1
        area = randint(0,1)
        if  area == 1:
            self.monster = Monster()
            self.battle(self.monster)
        return 'coord(%s,%s)' %(self.x,self.y)
    def battle(self,monster):
        while monster.hp > 1:
            print self.attack(monster)
            print monster.attack(player)
        self.monster = None
    def status(self):
        return 'hp = %s, atk = %s, def = %s, exp = %s, coins = %s' %(player.hp,player.atk,player.defence,player.exp,player.coin)
    def help(self):
        return ''' Here are the controls for the game:
        up - moves character up one pixel
        down - moves character down one pixel
        left - moves character left one pixel
        right - moves character right one pixel
        status - shows status of character
                '''

                
class Monster(Character):
    def __init__(self):
        Character.__init__(self,'Monster',10,2,2,1,1)
        #equip has name of weapon, atk value
        self.equip = ['Rubber Sword',1]
        self.atk = self.atk + self.equip[1]
        
player = Character('Ryan',100,10,4,0,0)

Commands = {
    'up': player.walkU,
    'down': player.walkD,
    'left': player.walkL,
    'right': player.walkR,
    'status': player.status,
    'help': player.help,
    }

while(player.hp > 0):
    line = raw_input("> ")
    args = line.split()
    if len(args) > 0:
        commandFound = False
        for c in Commands.keys():
            if args[0] == c[:len(args[0])]:
                print Commands[c]()
                commandFound = True
                break
        if not commandFound:
            print "%s doesn't understand the suggestion." % player.name
