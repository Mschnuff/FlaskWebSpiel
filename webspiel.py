from flask import request, Flask, render_template, redirect, url_for, flash, session, escape
from gothonweb import planisphere
from gothonweb.inventar import Inventar
from gothonweb.kampf import Kampf

app = Flask(__name__)

app.config['DEBUG'] = True
karte = planisphere.karte
kampf = Kampf()
inventar = Inventar()


""" @app.cache.memoize(timeout=cache_memoize_value) """
@app.route('/')
def index():

    # this is used to "setup" the session with starting values
    session['room_name'] = karte.START
    kampf.initKampf()
    inventar.initInv()

    #inventar.inhalt.append('goldener Schlüssel')
    # inventar.inhalt.append('Kochlöffel')
    # inventar.inhalt.append('Kochtopf')
    #session['inventar'] = karte.inventar
    karte.load_room(karte.START).cur_description = karte.load_room(
        karte.START).description
    return redirect(url_for("game"))


@app.route('/game', methods=['POST', 'GET'])
def game():

    # reloaded on each submit
    room_name = session.get('room_name')

    # shows the current room before input
    if request.method == 'GET':

        # the room_name should always exist. if not the player is simply redirected to you_died.html
        if room_name:
            # sets the current room (=object of class Room) to the value found in planisphere for room_name
            room = karte.load_room(room_name)
            # if room_name == 'barracks_fight':
            #    pass
            # room.initKampf()
            return render_template("show_room.html", room=room, inventar=inventar, kampf=kampf)
        else:
            # why is there here? do you need it? for the tests?
            return render_template("you_died.html")
    # this happens when 'POST' method is active (= player clicks on the submit button)

    else:
        room = karte.load_room(room_name)
        if room_name == 'barracks_fight':
            if kampf.curOrk is not kampf.spieler:
                kampf.spieler.erleideSchaden(5)
                if kampf.spieler.amleben:
                    action = 'barracks_fight'
                else:
                    action = "ork_feast"
            else:
                try:
                    antwort = int(request.form.get('orkantwort'))
                    button = request.form.get('naction')
                except:
                    button = "faust"
                    antwort = 4
                if antwort < 4:
                    if button == "loeffel":
                        damage = 30
                    else:
                        damage = 10     
                    kampf.orklist[antwort].erleideSchaden(damage)
                else:
                    kampf.orklist[antwort].erleideSchaden(10)
                orksleben = False
                for ork in kampf.orklist:
                    ork.checked = False
                    if not ork == kampf.spieler:
                        orksleben = orksleben or ork.amleben
                kampf.orklist[antwort].checked = True
                if orksleben and kampf.spieler.amleben:
                    if not (kampf.ork2.amleben or kampf.ork3.amleben or kampf.ork4.amleben):
                        action = "flee"
                        kampf.ork1.hitpoints = -10
                        kampf.ork1.amleben = False
                        kampf.zuEnde = True
                        karte.clear_room("barracks")
                    else:
                        action = "barracks_fight"    
                elif kampf.spieler.amleben:
                    action = "victory"
                    kampf.zuEnde = True
                    karte.clear_room("barracks")
                else:
                    action = "ork_feast"
            kampf.rotateCurrentOrk()

        elif room_name == 'puzzle':
            antwort = request.form.get('raetselantwort')

            if antwort == 'C':
                action = "correct"
                karte.clear_room("puzzle")
            else:

                action = "puzzle"
        else:
            # this saves the input into a variable
            action = request.form.get('naction')
            # if room_name == 'barracks_fight2':

            #    if kampf.spieler.amleben:

            #            action = 'barracks_fight'

            #    else:
            #        action = "ork_feast"
            if room_name == 'barracks_fight_flee':
                action = "victory"
            if room_name == 'victory':
                action = "victory"
                if 'Gummiente' not in inventar.inhalt:
                    inventar.inhalt.append('Gummiente')
                if 'Kochlöffel' in inventar.inhalt:
                    inventar.inhalt.remove('Kochlöffel')

            if room_name == 'puzzle_info':
                action = "correct"
                if 'silberner Schlüssel' not in inventar.inhalt:
                    inventar.inhalt.append('silberner Schlüssel')
            if room_name == 'barracks_intermediate' and 'Kochtopf' not in inventar.inhalt:
                action = "bla"
            if room_name == 'barracks_intermediate2':
                action = "fight"
                if 'Kochtopf' in inventar.inhalt:
                    inventar.inhalt.remove('Kochtopf')
                    kampf.orklist[3].hitpoints = 0
                    kampf.orklist[3].amleben = False
                        
            if room_name == 'treasure_chamber':
                if action in ['Kochtopf', 'Kochlöffel', 'Topf',
                           'Löffel', 'kochtopf', 'kochlöffel', 'topf', 'löffel']:
                    if not ('Kochtopf' in inventar.inhalt or kampf.zuEnde):
                        inventar.inhalt.append('Kochtopf')
                        inventar.inhalt.append('Kochlöffel')
                    else:
                        action = 'bla'
                if action in ['Truhe', 'truhe', 'münzen', 'kupfermünzen', 'Münzen', 'Kupfermünzen']:
                    if not 'goldener Schlüssel' in inventar.inhalt:
                        inventar.inhalt.append('goldener Schlüssel')
                    else:
                        action = 'bla'          
            
            if room_name == 'treasure_chamber_reward' or room_name == 'treasure_chamber_reward2':
                action = 'weiter'
            if room_name == 'barracks_cleared':
                action = 'zurueck'
            if room_name == 'puzzle_cleared':
                action = 'zurueck'
            if room_name == 'silver_door':
                option = action
                if option == 'zurück!':
                    action = 'back'
                else:
                    action = 'silver_key'
                    inventar.inhalt.remove('silberner Schlüssel')
                    karte.clear_room("silver_door")

            if room_name == 'golden_door':
                option = action
                if option == 'zurück!':
                    action = 'back'
                else:
                    action = 'golden_key'
                    inventar.inhalt.remove('goldener Schlüssel')
                    karte.clear_room("golden_door")
        # checks if room_name (= str representing current room) and action (= text from the form) exist
        if room_name and action:
            # sets the current room (=object of class Room) to the value found in planisphere for room_name
            room = karte.load_room(room_name)
            # calls go function with a key. the key is compared to the keys of a paths-dict from the current room
            next_room = room.go(action)
            # if the key is found, the game proceeds with the next room
            if not next_room:
                # if not the current room is set to the current room

                room.cur_description = room.alt_description
                session['room_name'] = karte.name_room(room)
            else:
                next_room.cur_description = next_room.description
                session['room_name'] = karte.name_room(next_room)
        # the room is reloaded or changed
        print(action)
        return redirect(url_for("game"))

# @app.route('/game/kampf', methods=['POST','GET'])
# def kampf():
#    return redirect(url_for("game"))


# YOU SHOULD CHANGE THIS IF YOU PUT ON THE INTERNET
app.secret_key = 'super secret key'

if __name__ == "__main__":
    app.run()
