from nose.tools import *
from gothonweb import planisphere
from gothonweb.planisphere import Room


def test_room():
    gold = Room("gold", "GoldRoom",
                """This room has gold in it you can grab. There's a
                door to the north.""")
    assert_equal(gold.name, "gold")
    assert_equal(gold.paths, {})

def test_room_paths():
    center = Room("center", "Center", "Test room in the center.")
    north = Room("north", "North", "Test room in the north.")
    south = Room("south", "South", "Test room in the south.")

    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    start = Room("start", "Start", "You can go west and down a hole.")
    west = Room("west", "Trees", "There are trees here, you can go east.")
    down = Room("down", "Dungeon", "It's dark down here, you can go up.")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)

def test_gothon_game_map():
    karte = planisphere.karte
    start_room = karte.load_room(karte.START)
    assert_equal(start_room.name, 'starting_cell')
    #assert_equal(start_room.go('shoot!'), karte.roomdict.get('generic_death'))
    #assert_equal(start_room.go('dodge!'), karte.load_room('generic_death'))
    #action = start_room.go('tell a joke')
    #assert_equal(action, karte.load_room('laser_weapon_armory'))

    #room = karte.load_room('laser_weapon_armory')
    #action = room.go('0132')
    #assert_equal(action, karte.load_room('the_bridge'))
    #action = room.go('*')
    #assert_equal(action, karte.load_room('generic_death'))

    #room = karte.load_room('the_bridge')
    #action = room.go('throw the bomb')
    #assert_equal(action, karte.load_room('generic_death'))
    #action = room.go('slowly place the bomb')
    #assert_equal(action, karte.load_room('escape_pod'))

    #room = karte.load_room('escape_pod')
    #action = room.go('2')
    #assert_equal(action, karte.load_room('the_end_winner'))
    #action = room.go('*')
    #assert_equal(action, karte.load_room('the_end_loser'))