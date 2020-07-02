from nose.tools import *
from app import app
from gothonweb import planisphere

# set the app to testing mode
app.config['TESTING'] = True
# instantiate a test client for the app
web = app.test_client()

def test_index():
    # tell the client to go to the subpage '/' with GET method
    rv = web.get('/', follow_redirects=True)
    # make sure the page is not found
    assert_equal(rv.status_code, 200)

    # tell the client to go to the subpage '/hello' with GET method
    rv = web.get('/game', follow_redirects=True)
    # make sure page is found
    assert_equal(rv.status_code, 200)
    # test if "Fill Out This Form" as bytes can be found in the clients data
    assert_in(b"Gothons", rv.data)
    assert_in(b"Zelle", rv.data)
    
    
    # ich teste hier erstmal nix mehr. läuft alles über session

    #rv = web.post('/game', follow_redirects=True, action='bla')
    #assert_in(b"Central Corridor", rv.data)
    #rv = web.post('/game', follow_redirects=True, action='dodge!')
    #assert_in(b"You died", rv.data)
    #rv = web.post('/game', follow_redirects=True, action='tell a joke')
    #assert_in(b"Laser", rv.data)

    # create a dict that maps values to our variables named 'name' and 'greet'
    #data = {'name': 'Zed', 'greet': 'Hola', 'filename': 'bla.txt'}
    
    #roomname = web.session['room_name']
    # tell the client to go to the subpage '/hello' with POST method
    # give it the data we set up above
    #rv = web.get('/game', follow_redirects=True)
    #assert_in(b(roomname), rv.data)
    #assert_in(b"bla", rv.data)
    # ! Dieser Test funktioniert nicht und ich weiß nicht so richtig wieso !
    #   siehe: if 'datei' not in request.files: in app.py
    
    # test if "Zed" as bytes can be found in the clients data
    #assert_in(b"Zed", rv.data)
    # test if "Hola" as bytes can be found in the clients data
    #assert_in(b"Hola", rv.data)
    #assert_in(b"geklappt", rv.data)
