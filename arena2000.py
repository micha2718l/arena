import random
import code

#Fighter class
class Fighter():
    lifeMax = 5
    attackPower = 5
    gold = 10
    stagger = 0
    stances = ['aggressive', 'balanced', 'defensive']
    
    #__init__ runs when the instance of the class is created
    def __init__(self, name='Noname'):
        self.name = name
        self.life = self.lifeMax
    
    def getStance(self):
        return random.choice(self.stances)

#by putting Fighter in the declaration, Player starts out "being" a Fighter
class Player(Fighter):
    fights = 0
    trainingCost = 5
    trainers = ['self', 'champion', 'archer', 'swordsman']

    def __init__(self, name='The Great Player 1'):
        Fighter.__init__(self, name)
        self.fights = 0
        self.trainingcost = 5

    def train(self, trainWith='self'):
        cost = self.trainingCost
        trainingPotential = 5
        trainingProbability = 0.75

        if trainWith not in self.trainers:
            trainWith = 'self'

        if trainWith == 'self':
            trainingPotential = 1
            trainingProbability = 0.5
            cost = 0

        if cost > self.gold:
            cost = 'you broke'
            attackIncrease = 0
        else:
            self.gold -= cost
            attackIncrease = trainingPotential if random.random() > trainingProbability else 0

        print('{} increased attack power by {} at a cost of {}, by training with {}.'.format(self.name, attackIncrease, cost, trainWith))
        self.attackPower += attackIncrease

    #example of overriding the default method
    def getStance(self):
        print('Choose stance, press {} for {}'.format(range(len(self.stances)),self.stances))
        try:
            return self.stances[int(input('Choice: '))]
        except:
            print('Not valid choice, try again.')
            return self.getStance()


def doTheSleep(player):
    #stuff like restore health...etc.
    pass

def doTheFightRound(player, fighter):
    coinToss = random.choice(['heads','tails'])
    if coinToss == 'heads':
        print('You win the coin toss, choose your stance to start the fight first.')
        playerStance = player.getStance()
    else:
        fighterStance = fighter.getStance()
        print('{} won the coin toss and has chosen the stance of {}.'.format(fighter.name, fighterStance))
        playerStance = player.getStance()
    print('FIGHT!')
    #ignoring all the information we actually have and just randomly deciding a winner for testing reasons...
    if random.randint(0,1) == 0:
        print('{} loses {} life.'.format(player.name, fighter.attackPower))
        player.life -= fighter.attackPower
    else:
        print('{} loses {} life.'.format(fighter.name, player.attackPower))
        fighter.life -= player.attackPower
    pass

def doTheFight(player, fighter):
    #will return -1 for player death, or >= 0 representing amount of gold won
    bothAlive = True
    while bothAlive:
        doTheFightRound(player, fighter)
        if fighter.life <= 0:
            amountWon = fighter.gold
            bothAlive = False
        elif player.life <= 0:
            amountWon = -1
            bothAlive = False
    return amountWon


gameState = 'playing'
choices = ['train', 'fight']

player = Player()
player.life = 100
maxDays = 25

numberOfEnemies = 5
fighterNames = ['Bernardo','Pierre','Ulysses','Rudy','Gilbert','Ashley','Chung','Byron','Ronald','Ben','Kerry','Noe','Haywood','Dusty','Anton','Darren','Juan','Bruno','Sam','Trenton','Vance','Jamal','Harold','Wilson','Cesar','Ian','Garth','Buddy','Devon','Russ','Joseph','Hoyt','Scotty','Tomas','Wilburn','Cecil','Amado','Brain','Elmer','Manual','Scottie','Rob','Everett','Dorian','Chet','Warren','Arnulfo','Val','Alvaro','Frederic','Huey','Herb','Elvin','Danial','Rolando','Simon','Garrett','Elmo','Horace','Orlando','Patrick','Carter','Delbert','Reggie','Nathaniel','Edwin','Dane','Joey','Numbers','Chi','Gil','Tomas','Lincoln','Jeffrey','Otha','Clair','Lenny','Darwin','Alexander','Ahmed','Spencer','Guy','Hank','Elias','Marcelo','Charlie','Clayton','Stan','Jerry','Harrison','Arnulfo','Wayne','Merle','Jonah','Abram','Gerardo','Johnie','Neville','Rudolph','Manuel','Bennie','Tony','Wilber','Fabian','Demetrius','Clement','Perry','Rufus','Cruz','Arturo','Ethan','Archie','Elvin','Luis','Riley','Edwin','Javier','Harrison','Shaun','Antony','Willard','Vito','Spencer','Russ','Adolfo','Tim','Kraig','Duncan','Al','Lino','Emery','Douglass','Cleveland','Haywood','Micheal','Curt','Freddy','Bernard','Merle','Logan','Steven','Truman','Erik','Tobias','Porter','Alva','Rogelio','Eddy','Warren','Hipolito','Refugio','Chang','Claudio','Sheldon','Harris','Maynard','Stephen','Barry','Weldon','Arnulfo','Bobby','Johnathan','Reginald','Carroll','Earnest','Loren','Lincoln','Darryl','Vincenzo','Alfred','Darren','Kent','Rusty','Virgilio','Elton','Claud','Mervin','Alejandro','Jerrell','Jae','William','Elden','Bruce','Malcolm','Leif','Bart','Waldo','Van','Jonah','Leon','Will','Zachary','Denver','Cedrick','Shawn','Darrel','Joey','Benton','Freddy','Cleo']
enemyPool = [Fighter(random.choice(fighterNames)) for i in range(numberOfEnemies)]
day = 0

player.name = str(input('What is your name: '))
print('Cool, {} has entered the arena. The four ways to leave are to buy out with 100 gold, defeat the {} enemies, last {} days, or die.'.format(player.name, numberOfEnemies, maxDays))
print('The potential enemies are {}.'.format(', '.join([e.name for e in enemyPool])))

while gameState == 'playing':
    currentEnemy = random.choice(enemyPool)
    #choose fight or train
    print('There are {} fighters left out of {}. {} has {} gold, need {} more to buy out of the arena.'.format(len(enemyPool), numberOfEnemies, player.name, player.gold, 100-player.gold))
    print('It is a new day, do you want to train [0] or fight {} [1]?'.format(currentEnemy.name))
    choice = False
    while choice is False:
        try:
            choice = choices[int(input('Choice: '))]
        except:
            print('Invalid choice, try again.')
            pass
    if choice == 'train':
        print('Who would you like to train with? (free for with self, {} for others), choose {} for {}.'.format(player.trainingCost, range(len(player.trainers)), player.trainers))
        trainChoice = False
        while trainChoice is False:
            try:
                trainChoice = player.trainers[int(input('Choice: '))]
            except:
                print('Invalid choice, try again.')
                pass
        player.train(trainWith=trainChoice)
    elif choice == 'fight':
        fightResult = doTheFight(player, currentEnemy)
        if fightResult == -1:
            gameState = 'died'
        else:
            print('{} has defeated {} and won {} gold.'.format(player.name, currentEnemy.name, fightResult))
            player.gold += fightResult
            enemyPool.remove(currentEnemy)
            if len(enemyPool) == 0:
                gameState = 'beat everyone'
            if player.gold >= 100:
                gameState = '100 gold, bought way out'

    doTheSleep(player)
    endOfDayMsg = 'Day number {} has ended, {} has {} gold, {} life, and {} attack power.'.format(day, player.name, player.gold, player.life, player.attackPower)

    print('\n\n' + '*'*(len(endOfDayMsg)+4))
    print('* {} *'.format(endOfDayMsg))
    print('*'*(len(endOfDayMsg)+4) + '\n\n')
    
    #print([e.name for e in enemyPool])
    #print([e.life for e in enemyPool])
    
    day += 1

#end of game message
print('Game ended for reason of {}'.format(gameState))


#uncomment this line to drop into an interactive python console with all the variables and everything else available
#type exit() into the prompt to exit it
#code.interact(local=locals())
