#задание 25
from model.project_mantis import ProjectMantis
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters+string.digits +""*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def test_add_project(app):
    app.project_mantis.get_project_list()
    app.project_mantis.create(ProjectMantis(name=random_string("name",4), description=random_string("description",4)))


    #new_list = app.project_mantis.get_project_list()
    #old_list.append(new_project)
    #assert new_list == old_list
