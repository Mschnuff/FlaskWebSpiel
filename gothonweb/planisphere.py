from gothonweb import lexicon
from gothonweb.ork import Ork

import re


        
class Room(object):

    def __init__(self, name, title, description):
        
        self.name = name
        self.title = title
        self.description = description
        self.alt_description = ""
        self.paths = {}
        self.deadly = False
        self.custom_death = self
        self.isdeath = ""
        self.cur_description = description
        
        

    def go(self, direction):
        list_of_words = re.split('[,.;! :*/%]', direction)
        all_paths = self.paths.keys()
        next_room = None
        for word in list_of_words:
            if word in all_paths:
                return self.paths.get(word)
        if self.deadly:
            next_room = self.custom_death
        return next_room   
        

    def add_paths(self, pathdict):
        pfadliste = pathdict.keys()
        for pfad in pfadliste:
            alle_moeglichkeiten = pathdict.get(pfad)
            for moeglichkeit in alle_moeglichkeiten:
                self.paths[moeglichkeit] = pfad
    
                   

class Planisphere(object):
    
    def __init__(self):
        # initialising all rooms
        self.START = 'starting_cell'
        self.roomdict = {}
        
        
        
    # returns a value from the globals dict (a Room object)
    def load_room(self, name):
   
        return self.roomdict.get(name)

    # returns a key from the global dict (the name of a Room object)
    def name_room(self, room):
        """
        Same possible security problem Can you trust room?
        What's a better solution that this globals lookup?
        """
        # already found a different way for returning the name of a room
        for key, value in self.roomdict.items():
            if value == room:
                return key

    def add_room(self, room):
        #print("addroom", room.name, room)
        self.roomdict[room.name] = room

    def clear_room(self, room):
        switcher = {
            "barracks": "barracks_cleared",
            "silver_door": "treasure_chamber",
            "golden_door": "giant_racoon",
            "puzzle": "puzzle_cleared"
        }
        switcherval = switcher.get(room)
        values = CENTRAL_CORRIDOR_PATHS.get(self.load_room(room))
        CENTRAL_CORRIDOR_PATHS.pop(self.load_room(room))
        CENTRAL_CORRIDOR_PATHS[self.load_room(switcherval)] = values
        central_corridor.add_paths(CENTRAL_CORRIDOR_PATHS)
# momentan muss der room name genau gleich sein wie der variablenname. Dafür gibt es sicher eine elegantere Lösung
intermediate = Room("intermediate", "...",
"""
""")
starting_cell = Room("starting_cell", "Gefängniszelle",
"""
Du erwachst in einer kalten, kargen Zelle. Erfreulicherweise
stellst du fest, dass man dir freundlicherweise den Schlüssel
für die Handschellen, mit denen man dich an die Wand gekettet hat,
da gelassen hat.
Du öffnest die Handschellen, der Schlüssel löst sich in Luft auf.
Wie Schlüssel das halt so machen.

Die Tür steht einen Spalt offen.
""")
starting_cell.alt_description = """
Das war wohl nix. Du müsstest eigentlich nur den Raum verlassen....
"""

central_corridor = Room("central_corridor", "Zentraler Korridor",
"""
Du betrittst einen dunklen, finsteren, schlecht beleuchteten,
stockdusteren Korridor. Auf beiden Seiten befinden sich jeweils 2
Türen insgesamt 4. Eine einzelne Fackel flackert rötlich
einige Schritte entfernt an der Wand.
""")
central_corridor.alt_description = """
Das hat nicht so gut geklappt. Versuche am besten etwas anderes.
Der Gang hat 4 Türen. Falls du das schon wieder
vergessen hast...
"""
        
barracks = Room("barracks", "Barracke",
"""
Brilliant! Du hast die Barracke der Orks gefunden. Sie sind
gerade dabei etwas zu zerlegen, das aussieht wie ein magerer
Katzenkadaver. Über deine Anwesenheit scheinen sie sehr er-
freut zu sein. Ein besonders hunriger Ork grunzt:

    'Endlich mal ein Happen den es lohnt zu kochen!'

Ob es wohl hilft sich einfach zu entschuldigen und 
klammheimlich den Raum wieder zu verlassen? 
""")
barracks_cleared = Room("barracks_cleared", "Barracke",
"Die Orks sind besiegt. Ansonsten gibts hier nichts zu tun.")
barracks_intermediate = Room("barracks_intermediate", "Orkfutter",
"""
Sehr unhöflich von dir! Die Orks greifen dich an. Bereite dich
vor so gut du kannst. Einer der Orks sieht wirklich hunrig aus.
""")
barracks_intermediate2 = Room("barracks_intermediate2", "Ablenkung",
"""
Ein besonders hunriger Ork reißt dir den Kochtopf aus der Hand
und beginnt den Eintopf gierig wegzuschlemmen. Ein ekelhafter
Anblick. Aber du hast gerade andere Sorgen... 
""")
barracks_fight2 = Room("barracks_fight2", "Kampf gegen die Orks",
"Die Orks greifen an:")
barracks_fight = Room("barracks_fight", "Kampf gegen die Orks",
"Genug der Vorbereitung. Versuche das Beste daraus zu machen!")
barracks_fight.alt_description = "der Kampf geht weiter... "
barracks_fight_flee = Room("barracks_fight_flee", "Flucht",
"Nachdem du seine Kameraden besiegt hast, ergreift der feige Ork die Flucht.")

victory = Room("victory", "Sieg!",
"""
Schlussendlich schaffst du es die Orks zu besiegen. Du erbeutest
eine Gummiente. Keiner weiß was das soll. Aber ein bischen stolz
bist du trotzdem.
""")
silver_door = Room("silver_door", "Silberne Tür",
"""
Du stehst vor einer silbernen Tür. Darauf steht:
    'Unermessliche Schätze erwarten ein Jeden,
    dessen Geist flink genug ist das Rätsel zu
    lösen.'
Welches Rätsel wohl gemeint ist?    
""")
golden_door = Room("golden_door", "Goldene Tür",
"""
Du stehst vor einer goldenen Tür. Sie sieht sehr wichtig aus.
Darauf steht:
    'Dies ist ein Videospiel. Wenn es eine golden Tür gibt,
    gibt es auch einen goldenen Schlüssel.'
""")
treasure_chamber = Room("treasure_chamber", "Schatzkammer",
"""
Nachdem du es geschafft hast das Schloss zu überwinden, offenbart sich
dir die jämmerlichste Schatzkammer, die je ein Mensch gesehen hat.
Auf dem Boden liegt hauptsächlich Müll.
""")
treasure_chamber_reward = Room("treasure_chamber_reward", "Schatzkammer",
"""
Du nimmst den Kochtopf und Löffel an dich. Man kann ja nie wissen, wann 
man spontan mal Hunger kriegt.
""")
treasure_chamber_reward2 = Room("treasure_chamber_reward2", "Schatzkammer",
"""
Du versuchst die Truhe an dich zu nehmen, merkst aber, dass sie zu schwer
zum tragen ist. Dann fällt dir ein, dass Kupfermünzen ohnehin nicht besonders 
wertvoll sind. Sinnlos die mitzunehmen.
Zwischen den Münzen findest du allerdings einen kleinen goldenen Schlüssel.
""")
treasure_chamber.addi_description = (
"""
Am hinteren Ende der Kammer befindet sich eine kleine Truhe mit 
Kupfermünzen. Zerissene und blutbefleckte Kleidungsstücke an der
Wand runden den armseligen Gesamteindruck ab.
""")
treasure_chamber.kochtopfdescription = (
"""
Auf einem Tisch siehst du einen Kochtopf, der aus verrostetem Blech zu 
bestehen scheint und eine übel riechende Brühe sowie einen hölzernen 
Kochlöffel enthält.
""")

treasure_chamber.alt_description =( 
"""
Das bringt nichts. Vielleicht wäre es klüger einfach wieder in den
Zentralen Korridor zurückzukehren.
Auf dem Boden liegt hauptsächlich Müll. 
""")

giant_racoon = Room("giant_racoon", "Riesenwaschbär",
"""
Du hast den Endboss gefunden :) Ein vier Meter hoher Waschbär
putzt sich sorgfältig das Fell. Als du den Raum betrittst,
hält er inne und blickt dich aus blutunterlaufenen Augen an.
Während er fauchend auf dich zustürmt, kannst du hinter dem Wasch-
bären am anderen Ende des Raumes eine kleine Tür erkennen. Sie wird
von einem goldenen Schein umhüllt, damit du verstehst, dass sie
wichtig ist.
Aber erstmal wäre da ja noch der Waschbär. Lust zu kämpfen?
""")

puzzle = Room("puzzle", "Rätselraum",
"""
Vor dir erblickst du einen wabernden Schemen aus Rauch, 
der plötzlich anfängt zu sprechen:

'Löse mein Rätsel und werde reichlich belohnt, versagst du so soll 
ein mysteriöser Tod dein Lohn sein. Nimm dir Zeit beim Überlegen, 
aber wähle weise:
--------
Eine Prinzessin ist so alt wie der Prinz sein wird, 
wenn die Prinzessin doppelt so alt ist,
wie der Prinz war, 
als das Alter der Prinzessin halb soviel betrug,
wie die Summe ihrer beiden jetzigen Alter.
--------
Wie alt sind die Königskinder?'
""")
puzzle_cleared = Room("puzzle_cleared", "Rätselraum",
"Das Rätsel ist gelöst. Ansonsten gibt es hier nix zu tun.")
puzzle.alt_description = """
Jaja, so ein Rätsel ist schwierig. versuch mal 'bla einzugeben'
"""
puzzle_info = Room("puzzle_info", "Richtig!",
"""
Du hast das Rätsel korrekt gelöst. Der wabernde Schemen zieht sich
zusammen und verwandelt sich dabei in einen silbernen Schlüssel.
Du nimmst den silbernen Schlüssel an dich.
""")
the_end_winner = Room("the_end_winner", "Ende",
"""
Anstatt dich zu zerfleischen spielt der Waschbär lieber mit
der Gummiente. Endlich weißt du wofür die Dinger gut sind.
Da er nun abgelenkt ist, kannst du durch die Tür in die
Freiheit entkommen. Völlig zusammenhangslos stolperst du plötz-
lich über einen Haufen Gold, halbnackte Jungfern fallen dir
um den Hals, in der Ferne schmettern Posaunen das
Deutschlandlied.
Herzlichen Glückwunsch, du Gurke! Mögest du auf ewig
in Frieden rumgurken.

     _____
     /__  _\\
     | Ö   Ô |
     c|   u   |p
     | \___/ |
     \______/
""")

the_end_loser = Room("the_end_loser", "Ende", 
"""
Waschbären töten eigentlich keine Menschen hast du mal gelernt.
Leider weiß dieser nix davon.
Er reißt dir den Kopf ab und kaut eine Weile lang auf deinem
leblosen Körper rum bevor er das Interesse verliert und weiter
sein Fell putzt.
""")
ork_feast = Room("ork_feast", "Verputzt",
"""
Ja, was soll man da groß sagen? Die Orks streiten sich eine
Weile lang um deine besten Stücke, dann braten und verputzen
sie dich. Du schmeckst vorzüglich!    
""")
mysterious_death = Room("mysterious_death", "Was zur Hölle",
"""
Du löst dich spontan in Luft auf und warst nie mehr gesehen...
Keiner weiß warum. Frag nicht. 
""")

generic_death = Room("generic_death", "Tod", 
"""
Du hast es geschafft durch außerordentliche Blödheit umzukommen.
Gut gemacht!
Deine Leiche erhält zur Belohnung einen Keks.

        _______
        /       \\
        | Ö   Ö  |
        c|   u    |p
        | ,----, |
        \_______/
""")
STARTING_CELL_PATHS = {
    central_corridor: ['verlassen', 'öffne', 'verlasse','gehen', 'gehe', 'öffne']
}
TREASURE_CHAMBER_PATHS = {
    central_corridor: ['verlassen', 'gehen', 'öffne', 'verlasse'],
    treasure_chamber_reward: ['Kochtopf', 'Kochlöffel', 'Topf', 'Löffel', 'kochtopf', 'kochlöffel', 'topf', 'löffel'],
    treasure_chamber_reward2: ['Truhe', 'truhe', 'münzen', 'kupfermünzen', 'Münzen', 'Kupfermünzen']
}
TREASURE_CHAMBER_REWARD_PATHS = {
    treasure_chamber: ['weiter']
}
CENTRAL_CORRIDOR_PATHS = {
    barracks: ['1', 'erste', 'eins'],
    puzzle: ['2', 'zweite', 'zwei'],
    golden_door: ['3', 'dritte', 'drei'],
    silver_door: ['4', 'vierte', 'vier']
}
BARRACKS_PATHS = {
    central_corridor: ['entschuldigen', 'entschuldige', 'sorry', 'sry']
}
BARRACKS_CLEARED_PATHS = {
    central_corridor: ['zurueck']
}
BARRACKS_INTERMEDIATE_PATHS = {
    barracks_intermediate2: ['topf', 'Kochtopf', 'Eintopf', 'kochtopf', 'Topf']
}
BARRACKS_INTERMEDIATE_PATHS2 = {
    barracks_fight: ['fight']
}


BARRACKS_FIGHT_PATHS = {
    barracks_fight_flee: ['flee'],
    barracks_fight: ['barracks_fight'],
    ork_feast: ['ork_feast'],
    victory: ['victory']
}
BARRACKS_FIGHT_FLEE_PATHS = {
    victory: ['victory']
}
VICTORY_PATHS = {
    central_corridor: ['victory']
}
PUZZLE_PATHS = {
    puzzle_info: ['correct']
}
PUZZLE_INFO_PATHS = {
    central_corridor: ['correct']
}
PUZZLE_CLEARED_PATHS = {
    central_corridor: ['zurueck']
}
SILVER_DOOR_PATHS = {
    central_corridor: ['back'],
    treasure_chamber: ['silver_key']
}
GOLDEN_DOOR_PATHS = {
    central_corridor: ['back'],
    giant_racoon: ['golden_key']
}
GIANT_RACOON_PATHS = {
    the_end_winner: ['gummiente', 'Gummiente', 'Ente']
}

treasure_chamber_reward.add_paths(TREASURE_CHAMBER_REWARD_PATHS)
treasure_chamber_reward2.add_paths(TREASURE_CHAMBER_REWARD_PATHS)
puzzle_cleared.add_paths(PUZZLE_CLEARED_PATHS)
barracks_fight_flee.add_paths(BARRACKS_FIGHT_FLEE_PATHS)
barracks_cleared.add_paths(BARRACKS_CLEARED_PATHS)
barracks_intermediate.add_paths(BARRACKS_INTERMEDIATE_PATHS)
barracks_intermediate2.add_paths(BARRACKS_INTERMEDIATE_PATHS2)
starting_cell.add_paths(STARTING_CELL_PATHS)
silver_door.add_paths(SILVER_DOOR_PATHS)
golden_door.add_paths(GOLDEN_DOOR_PATHS)
puzzle_info.add_paths(PUZZLE_INFO_PATHS)
giant_racoon.add_paths(GIANT_RACOON_PATHS)
treasure_chamber.add_paths(TREASURE_CHAMBER_PATHS)
central_corridor.add_paths(CENTRAL_CORRIDOR_PATHS)
barracks.add_paths(BARRACKS_PATHS)
barracks_fight.add_paths(BARRACKS_FIGHT_PATHS)

victory.add_paths(VICTORY_PATHS)
puzzle.add_paths(PUZZLE_PATHS)
death_text = """

Du hast es geschafft durch außerordentliche Blödheit umzukommen.
Gut gemacht!
Deine Leiche erhält zur Belohnung einen Keks.

        _______
        /       \\
        | Ö   Ö  |
        c|   u    |p
        | ,----, |
        \_______/
"""

giant_racoon.deadly = True
giant_racoon.custom_death = the_end_loser
the_end_loser.isdeath = death_text

barracks.deadly = True
barracks.custom_death = barracks_intermediate

barracks_intermediate.deadly = True
barracks_intermediate.custom_death = barracks_fight

""" barracks_fight.deadly = True
barracks_fight.custom_death = ork_feast
ork_feast.isdeath = death_text """

puzzle.deadly = True
puzzle.custom_death = mysterious_death
mysterious_death.isdeath = death_text



karte = Planisphere()

karte.add_room(barracks_fight_flee)
karte.add_room(treasure_chamber_reward2)
karte.add_room(treasure_chamber_reward)
karte.add_room(puzzle_cleared)
karte.add_room(barracks_cleared)
karte.add_room(barracks_intermediate)
karte.add_room(barracks_intermediate2)
karte.add_room(starting_cell)
karte.add_room(silver_door)
karte.add_room(golden_door)
karte.add_room(puzzle_info)
karte.add_room(mysterious_death)
karte.add_room(ork_feast)
karte.add_room(central_corridor)
karte.add_room(giant_racoon)
karte.add_room(treasure_chamber)
karte.add_room(barracks)
karte.add_room(puzzle)
karte.add_room(the_end_winner)
karte.add_room(the_end_loser)
karte.add_room(generic_death)
karte.add_room(barracks_fight)
#karte.add_room(barracks_fight2)
karte.add_room(victory)
for name in karte.roomdict:
    room = karte.load_room(name)
    room.add_paths({
        generic_death: ['selbstmord']
    })
   
#print(karte.START)
#print(karte.roomdict)                    