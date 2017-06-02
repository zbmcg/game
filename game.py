from random import randint

class Character(object):

    def __init__(self):

        self.fnames = ['Adam', 'Bob', 'Charles',
                       'Daniel', 'Earl', 'Frank',
                       'Gary', 'Hank', 'Isaac',
                       'Jack', 'Kenneth', 'Lawrence',
                       'Matthew', 'Nathaniel','Orson',
                       'Patrick', 'Quincy', 'Reginald',
                       'Samuel', 'Terrance', 'Ulysses',
                       'Vincent', 'Wesley', 'Xavier']

        self.lnames = ['Almond', 'Birmingham', 'Chesterfield',
                       'Danger', 'Eastman', 'Fandango',
                       'Gunt', 'Harper', 'Irving',
                       'Jewels', 'Kirkpatrick', 'Lance',
                       'Moneypenny', 'Norfolk', 'Oldman',
                       'Partridge', 'Quintus', 'Roth',
                       'Summerford', 'Tarp', 'Umbrage',
                       'Vetinari', 'Woolridge', 'Yank']

        self.adjs = ['amorous', 'bitchy', 'cunty',
                     'daring', 'effeminate', 'fat',
                     'gunkin', 'heroic', 'illin',
                     'jealous', 'kind', 'lame',
                     'mellow', 'narcissistic', 'opportunistic',
                     'pregnant', 'quick-witted', 'rapey',
                     'sexy', 'twatty', 'ugly',
                     'villainous', 'witty', 'zesty']

        self.jobs = ['airline pilot', 'barrista', 'chef',
                     'drug dealer', 'everyman', 'fortune teller',
                     'geisha', 'herpetologist', 'Isuzu salesman',
                     'janitor', 'killer', 'lawyer',
                     'masseur', 'necrophiliac', 'oil man',
                     'philosopher', 'quantum physicist', 'rapper',
                     'security guard', 'truck driver', 'voyeur',
                     'wedding singer', 'xenobiologist', 'zoologist']

        self.name = None
        self.adj = None
        self.job = None
        self.health = None
        self.sanity = None
        self.strength = None
        self.agility = None
        self.willpower = None
        self.status = None


    def roll(self):

        self.name = "%s %s" % (self.fnames[randint(0,23)], self.lnames[randint(0,23)])
        self.adj = self.adjs[randint(0,23)]
        self.job = self.jobs[randint(0,23)]
        self.health = randint(4,9)
        self.sanity = 13 - self.health
        self.strength = randint(4,6)
        self.agility = randint(3,5)
        self.willpower = 13 - (self.strength + self.agility)
        self.status = "Healthy"

    def create(self):

        self.name = raw_input("What do they call you?\n> ")
        self.adj = "lying"
        self.job = raw_input("What's your trade?\n> ")
        self.health = int(raw_input("Listen. You've got 13 points for Health and Sanity. How many for Health?\n> "))
        self.sanity = 13 - self.health
        print "Your Sanity is %d" % self.sanity
        self.strength = int(raw_input("Listen. You've got 13 points for Strength, Agility, and Willpower. How many for Strength?\n< "))
        self.agility = int(raw_input("How many for Agility?\n< "))
        self.willpower = 13 - (self.strength + self.agility)
        print "Your Willpower is %d" % self.willpower
        if self.willpower < 0:
            print "You're gonna regret that, smartass."

    def display(self):

        print '-' * 40
        print '| %s' % self.name
        print '| %s %s' % (self.adj, self.job)
        print '-' * 40
        print '| Health: %s' % self.health
        print '| Sanity: %s' % self.sanity
        print '-' * 40
        print '| Strength:  %s' % self.strength
        print '| Agility:   %s' % self.agility
        print '| Willpower: %s' % self.willpower
        print '-' * 40
        print '| Status: %s' % self.status
        print '-' * 40

class Dialogue(object):

    def __init__(self):

        self.intro1 = """
            Hey buddy, wake up. Wow, you really took a beating!
            What's that? Where are you? You're in my damn bar!
            Huh? How do you not even know your own name?
            I think that's your ID on the floor over there.
            """

class Game(object):

    def __init__(self):

        self.char = Character()
        self.dlg = Dialogue()

    def MainMenu(self):

        print "You're in a game now. This is the main menu."
        print "Pick something."
        print "[1. New Game]"
        print "[2. Load Save]"
        print "[3. Quit]"

        while True:

            choice = raw_input("> ")

            if choice == '1':

                a.NewGame()

            elif choice == '2':

                print "Err, I haven't written that yet."
                print "Pick something else."

            elif choice == '3':

                print "Well, bye then."
                exit(0)

            else:

                print "Type 1, 2, or 3 and then hit RETURN."
                print "It's not super complciated."

    def NewGame(self):

        print self.dlg.intro1

        self.char.roll()

        create = True

        while create:

            self.char.display()

            done = raw_input("Is that you?[Y/N]\n> ")

            if done == 'Y':

                create = False

            elif done == 'N':

                print "Alright. I think I see another ID."
                print "Do you wanna look or just tell me who you are?"
                print "[1. No idea who I am...]"
                print "[2. Just make something up]"
                choice = raw_input("> ")

                if choice == '1':

                    self.char.roll()

                elif choice == '2':

                    self.char.create()

                else:

                    print "You're not the sharpest knife. Let's see here..."
                    self.char.roll()

            else:

                print "Maybe you need to take a closer look."

        print "Well, I'm glad we could work that out. Great job."
        print "Let me call you an Uber or something."
        exit(0)


    def LoadGame(self):

        pass

a = Game()
a.MainMenu()
