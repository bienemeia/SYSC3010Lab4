from backend import Backend
from mydbconfig import *
backend = Backend(config, email, firstname, lastname)

backend.add_authorized_users('boshenzhang@cmail.carleton.ca')
backend.add_authorized_users('grahamcbell@cmail.carleton.ca')
