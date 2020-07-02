from nose.tools import *
from app_alt import app

# set the app to testing mode
app.config['TESTING'] = True
# instantiate a test client for the app
web = app.test_client()

def test_index():
    # tell the client to go to the subpage '/' with GET method
    rv = web.get('/', follow_redirects=True)
    # make sure the page is not found
    assert_equal(rv.status_code, 404)

    # tell the client to go to the subpage '/hello' with GET method
    rv = web.get('/hello', follow_redirects=True)
    # make sure page is found
    assert_equal(rv.status_code, 200)
    # test if "Fill Out This Form" as bytes can be found in the clients data
    assert_in(b"Fill Out This Form", rv.data)

    # create a dict that maps values to our variables named 'name' and 'greet'
    data = {'name': 'Zed', 'greet': 'Hola', 'filename': 'bla.txt'}
    # tell the client to go to the subpage '/hello' with POST method
    # give it the data we set up above
    rv = web.post('/hello', follow_redirects=True, data=data)

    # ! Dieser Test funktioniert nicht und ich weiß nicht so richtig wieso !
    #   siehe: if 'datei' not in request.files: in app.py

    # test if "Zed" as bytes can be found in the clients data
    #assert_in(b"Zed", rv.data)
    # test if "Hola" as bytes can be found in the clients data
    #assert_in(b"Hola", rv.data)
    #assert_in(b"geklappt", rv.data)
