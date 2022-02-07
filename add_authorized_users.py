from backend import Backend
from mydbconfig import *
backend = Backend(config, email, firstname, lastname)

backend.add_authorized_users('boshenzhang@cmail.carleton.ca')
backend.add_authorized_users('grahamcarsonbell@gmail.com')
backend.add_authorized_users('meiacopeland@cmail.carleton.ca')

