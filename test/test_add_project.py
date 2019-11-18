from model.project_mantis import ProjectMantis

def test_add_project(app):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
    old_list = app.project_mantis.get_project_list()
    #project = ProjectMantis(name="8", description="123")
    new_project = app.project_mantis.create(ProjectMantis(name="8", description="123"))
    new_list = app.project_mantis.get_project_list()
    old_list.append(new_project)
    assert new_list == old_list
