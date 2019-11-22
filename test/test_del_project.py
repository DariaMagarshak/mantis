#задание 25
from model.project_mantis import ProjectMantis
import random
from random import randrange
import string

def test_delete_project(app):
    if app.project_mantis.get_project_list() == []:
        app.project_mantis.create(ProjectMantis(name="test"))

    old_list = app.project_mantis.get_project_list()
    #old_list = app.soap.get_list(username, password)

    app.project_mantis.delete_project()
    new_list = app.project_mantis.get_project_list()
    #new_list = app.soap.get_list(username, password)
    old_list[0:1] = []
    assert new_list == old_list



def random_username(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])



    #new_contacts = db.get_contact_list()
    #assert len(old_contacts) - 1 == len(new_contacts)
    #old_contacts.remove(contact)
   # assert old_contacts == new_contacts
    #if check_ui:
       # assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

        # new_list = app.project_mantis.get_project_list()
        # old_list.append(new_project)
        # assert new_list == old_list