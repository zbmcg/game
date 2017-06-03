from random import randint
import pickle
import os


class Character(object):

    def __init__(self):

        self.fnames = ['Adam', 'Bob', 'Charles',
                       'Daniel', 'Earl', 'Frank',
                       'Gary', 'Hank', 'Isaac',
                       'Jack', 'Kenneth', 'Lawrence',
                       'Matthew', 'Nathaniel', 'Orson',
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

        self.dict = {
            'name': '',
            'adj': '',
            'job': '',
            'health': 0,
            'wits': 0,
            'strength': 0,
            'cunning': 0,
            'status': '',
            'location': '',
            'inventory': []
        }

    def roll(self):

        self.dict['name'] = "%s %s" % (self.fnames[randint(0, 23)], self.lnames[randint(0, 23)])
        self.dict['adj'] = self.adjs[randint(0, 23)]
        self.dict['job'] = self.jobs[randint(0, 23)]
        self.dict['health'] = randint(4, 9)
        self.dict['wits'] = 13 - self.dict['health']
        self.dict['strength'] = randint(2, 6)
        self.dict['cunning'] = 8 - self.dict['strength']
        self.dict['status'] = "Healthy"
        self.dict['location'] = "Bar"
        self.dict['inventory'] = ['an empty wallet', 'a strange rock']

    def create(self):

        self.dict['name'] = raw_input("What do they call you?\n> ")
        self.dict['adj'] = "lying"
        self.dict['job'] = raw_input("What's your trade?\n> ")
        self.dict['health'] = int(raw_input(
            "Listen. You've got 13 points for Health and Wits. How many for Health?\n> "))
        self.dict['wits'] = 13 - int(self.dict['health'])
        print "Your wits are %d" % self.dict['wits']
        if self.dict['wits'] < 0:
            print "You're gonna regret that, smartass."
        self.dict['strength'] = int(raw_input(
            "Listen. You've got 8 points for Strength and Cunning. How many for Strength?\n< "))
        self.dict['cunning'] = 8 - self.dict['strength']
        print "Your Cunning is %d" % self.dict['cunning']
        if self.dict['cunning'] < 0:
            print "You're gonna regret that, smartass."

    def display(self):

        print '-' * 40
        print '| %s' % self.dict['name']
        print '| %s %s' % (self.dict['adj'], self.dict['job'])
        print '-' * 40
        print '| Health: %s' % self.dict['health']
        print '| Wits: %s' % self.dict['wits']
        print '-' * 40
        print '| Strength:  %s' % self.dict['strength']
        print '| Cunning:   %s' % self.dict['cunning']
        print '-' * 40
        print '| Status: %s' % self.dict['status']
        print '| Location: %s' % self.dict['location']
        print '-' * 40
        print '| Inventory'
        for i in self.dict['inventory']:
            print "| - %s" % i
        print '-' * 40


class Dialogue(object):

    def __init__(self):

        self.intro1 = """
            Hey buddy, wake up. Wow, you really took a beating!
            What's that? Where are you? You're in my damn bar!
            Huh? How do you not even know your own name?
            I think that's your ID on the floor over there.
            """


class Objects(object):

    def __init__(self):

        pass


class Persons(object):

    def __init__(self):

        pass


class Location(object):

    def __init__(self):

        self.dict = {
            'name': None,
            'entry': None,
            'desc': None,
            'north': None,
            'south': None,
            'east': None,
            'west': None,
            'persons': [],
            'objects': []
        }

    def help(self):

        print "[look] - Have a look around"
        print "[go] - Lists where you can go"
        print "[go north|south|east|west] - Go in that direction"
        print "[inspect <noun>] - Look closer at something"
        print "[interact <noun>] - Interact with something"
        print "[char] - Display your character information"
        print "[quit] - Go to the main menu"

    def look(self, desc, persons, objects):

        print desc
        for p in persons:
            print "You see %s" % p
        for o in objects:
            print "You notice %s" % o

    def go(self):

        pass

    def inspect(self):

        pass

    def interact(self):

        pass

    def quit(self):

        pass


class Map(object):

    def __init__(self):

        self.apartment = Location()
        self.bar = Location()
        self.street = Location()

    def f_apartment(self):

        if self.apartment.dict['name'] is None:
            self.apartment.dict['name'] = 'Apartment'
            self.apartment.dict['entry'] = """
                A %s %s walks into an apartment.
                """ % (a_game.char.dict['adj'], a_game.char.dict['job'])
            self.apartment.dict['desc'] = "The apartment smells like copper and electricity."
            self.apartment.dict['north'] = None
            self.apartment.dict['south'] = None
            self.apartment.dict['east'] = "the street"
            self.apartment.dict['west'] = None
            self.apartment.dict['persons'] = ['an old white cat']
            self.apartment.dict['objects'] = ['some papers', 'a table']

        a_game.char.dict['location'] = "Apartment"
        print self.apartment.dict['entry']

        choosing = True

        while choosing:

            choice = raw_input("> ")

            if choice.lower() == 'help':

                self.apartment.help()

            elif choice.lower() == 'look':

                self.apartment.look(self.apartment.dict['desc'],
                                    self.apartment.dict['persons'],
                                    self.apartment.dict['objects'])

            elif choice.lower() == 'go':

                print "To the east is the street"

            elif choice.lower() == 'go north' \
                    or choice.lower() == 'go south' \
                    or choice.lower() == 'go west':

                print "You can't go that way."

            elif choice.lower() == 'go east':

                print "You head out to the street"
                a_game.map.f_street()

            elif choice.lower() == 'inspect cat':

                print "The cat purrs at you."

            elif choice.lower() == 'inspect papers':

                print "The papers appear to be news clippings",
                print "about a string of local murders."

            elif choice.lower() == 'inspect table':

                print "It's just a table."

            elif choice.lower() == 'interact cat':

                if 'a statuette' in a_game.char.dict['inventory']:

                    print "You're boring the cat."

                else:

                    print "The cat walks over to a weird statuette"

                    if 'a statuette' not in self.apartment.dict['objects']:

                        self.apartment.dict['objects'].append('a statuette')

            elif choice.lower() == 'inspect statuette' \
                    and 'a statuette' in self.apartment.dict['objects']:

                print "The statuette appears to be made",
                print "of jade and depicts some sort of",
                print "six-legged animal."

            elif choice.lower() == 'interact statuette' \
                    and 'a statuette' in self.apartment.dict['objects']:

                print "You take the statuette."
                self.apartment.dict['objects'].remove('a statuette')
                a_game.char.dict['inventory'].append('a statuette')

            elif choice.lower() == 'char':

                a_game.char.display()

            elif choice.lower() == 'quit':

                a_game.savegame()
                a_game.mainmenu()

            else:

                print "Invalid input. Try asking for [help]."

    def f_bar(self):

        if self.bar.dict['name'] is None:
            self.bar.dict['name'] = 'Bar'
            self.bar.dict['entry'] = """
                A %s %s walks into a bar.
                """ % (a_game.char.dict['adj'], a_game.char.dict['job'])
            self.bar.dict['desc'] = "The bar smells like old beer."
            self.bar.dict['north'] = 'the back alley'
            self.bar.dict['south'] = 'the street'
            self.bar.dict['east'] = None
            self.bar.dict['west'] = None
            self.bar.dict['persons'] = ['the bartender']
            self.bar.dict['objects'] = ['a hammer', 'a jukebox']

        a_game.char.dict['location'] = "Bar"
        print self.bar.dict['entry']

        choosing = True

        while choosing:

            choice = raw_input("> ")

            if choice.lower() == 'help':

                self.bar.help()

            elif choice.lower() == 'look':

                self.bar.look(self.bar.dict['desc'],
                              self.bar.dict['persons'],
                              self.bar.dict['objects'])

            elif choice.lower() == 'go':

                print "To the north is the back alley"
                print "To the south is the street"

            elif choice.lower() == 'go north':

                print "You go to the back alley."
                print "Just kidding, I haven't written that yet."

            elif choice.lower() == 'go east' \
                    or choice.lower() == 'go west':

                print "You can't go that way."

            elif choice.lower() == 'go south':

                print "You head out to the street"
                a_game.map.f_street()

            elif choice.lower() == 'inspect bartender' \
                    or choice.lower() == 'interact bartender':

                print "The bartender wants you to leave."

            elif choice.lower() == 'inspect hammer':

                print "It's just an ordinary hammer."

            elif choice.lower() == 'inspect jukebox':

                print "The jukebox is unplugged."

            elif choice.lower() == 'interact hammer':

                print "You take the hammer."
                a_game.char.dict['inventory'].append('a hammer')
                self.bar.dict['objects'].remove('a hammer')

            elif choice.lower() == 'interact jukebox':

                print "You plug in the jukebox."
                print "It begins to play 80s pop."

            elif choice.lower() == 'char':

                a_game.char.display()

            elif choice.lower() == 'quit':

                a_game.savegame()
                a_game.mainmenu()

            else:

                print "Invalid input. Try asking for [help]."

    def f_street(self):

        if self.street.dict['name'] is None:
            self.street.dict['name'] = 'Street'
            self.street.dict['entry'] = """
                A %s %s walks into a street.
                """ % (a_game.char.dict['adj'], a_game.char.dict['job'])
            self.street.dict['desc'] = "The street smells like piss."
            self.street.dict['north'] = 'the bar'
            self.street.dict['south'] = None
            self.street.dict['east'] = None
            self.street.dict['west'] = 'your apartment'
            self.street.dict['persons'] = ['a bum']
            self.street.dict['objects'] = ['a fire hydrant', 'a truck']

        a_game.char.dict['location'] = "Street"
        print self.street.dict['entry']

        choosing = True

        while choosing:

            choice = raw_input("> ")

            if choice.lower() == 'help':

                self.street.help()

            elif choice.lower() == 'look':

                self.street.look(self.street.dict['desc'],
                                 self.street.dict['persons'],
                                 self.street.dict['objects'])

            elif choice.lower() == 'go':

                print "To the north is the bar"
                print "To the west is your apartment"

            elif choice.lower() == 'go north':

                print "You go to the bar."
                a_game.map.f_bar()

            elif choice.lower() == 'go east' \
                    or choice.lower() == 'go south':

                print "You can't go that way."

            elif choice.lower() == 'go west':

                print "You go to your apartment"
                a_game.map.f_apartment()

            elif choice.lower() == 'inspect bum' \
                    or choice.lower() == 'interact bum':

                print "Spare change?."

            elif choice.lower() == 'inspect fire hydrant':

                print "It's your average red fire hydrant."

            elif choice.lower() == 'interact fire hydrant':

                if 'a hammer' in a_game.char.dict['inventory'] \
                        and 'a fire hydrant' in self.street.dict['objects']:

                    print "You strike the fire hydrant with your hammer."
                    print "Water erupts out of the top and floods the area."

                    self.street.dict['objects'].remove('a fire hydrant')
                    self.street.dict['objects'].append('a busted fire hydrant')

                elif 'a fire hydrant' in self.street.dict['objects']:

                    print "You slap the fire hydrant like an idiot."

                else:

                    print "You've already broken this."


            elif choice.lower() == 'inspect truck':

                print "It looks like an old, rusted Ford."

            elif choice.lower() == 'interact truck':

                print "You open the door and climb into the cabin."
                print "You can't find any keys inside, so you get back out."

            elif choice.lower() == 'char':

                a_game.char.display()

            elif choice.lower() == 'quit':

                a_game.savegame()
                a_game.mainmenu()

            else:

                print "Invalid input. Try asking for [help]."


class Game(object):

    def __init__(self):

        self.char = Character()
        self.obj = Objects()
        self.prs = Persons()
        self.map = Map()
        self.dlg = Dialogue()

    def mainmenu(self):

        print "You're in a game now. This is the main menu."
        print "Pick something."
        print "[1. New Game]"
        print "[2. Load Save]"
        print "[3. Quit]"

        choosing = True

        while choosing:

            choice = raw_input("> ")

            if choice == '1':

                a_game.newgame()

            elif choice == '2':

                a_game.loadgame()

            elif choice == '3':

                print "Well, bye then."
                
                exit(0)

            else:

                print "Type 1, 2, or 3 and then hit RETURN."
                print "It's not super complciated."

    def newgame(self):

        print self.dlg.intro1

        self.char.roll()

        create = True

        while create:

            self.char.display()

            done = raw_input("Is that you?[Y/N]\n> ")

            if done.lower() == 'y':

                create = False

            elif done.lower() == 'n':

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

        a_game.savegame()

        a_game.map.f_bar()

    def loadgame(self):

        saves = []

        for f in os.listdir("."):

            if f.endswith(".dat"):

                f = f.split('.')

                saves.append(f[0])

        print "Welcome back, uhh....What's your name?"

        for i in saves:

            print " * %s" % i

        print " * Nevermind"

        choosing = True

        while choosing:

            save_file = raw_input("> ") + '.dat'

            if os.path.isfile(save_file):

                choosing = False

                with open(save_file, "rb") as f:

                    a_game.char.dict = pickle.load(f)
                    a_game.map.apartment.dict = pickle.load(f)
                    a_game.map.bar.dict = pickle.load(f)
                    a_game.map.street.dict = pickle.load(f)

            elif save_file == 'Nevermind.dat':

                a_game.mainmenu()

            else:

                print "Invalid save."

        print "This is you:"

        a_game.char.display()

        print "Returning you to last known location."

        f_loc = "a_game.map.f_" + \
            a_game.char.dict['location'].lower() + \
            "()"

        eval(f_loc)

    def savegame(self):

        # need to figute out how to save my other objects as well
        # may have to convert every class to a dictionary

        save_file = a_game.char.dict['name'] + '.dat'

        with open(save_file, "wb") as f:

            pickle.dump(a_game.char.dict, f)
            pickle.dump(a_game.map.apartment.dict, f)
            pickle.dump(a_game.map.bar.dict, f)
            pickle.dump(a_game.map.street.dict, f)


a_game = Game()
a_game.mainmenu()
