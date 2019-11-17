from model.project_mantis import ProjectMantis

class ProjectMantisHelper:
    def __init__(self, app):
        self.app = app


    def create(self, project):
        wd = self.app.wd
        self.app.open_projects_page()
        # fill group form
        self.fill_form(project)
        # submit group creation
        wd.find_element_by_xpath("//input[@value='Add Project']").click()


    def fill_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.app.open_manage_projects()

            self.project_cache = []
            #wd.find_element_by_xpath("//tr[class='row-%s']" % index)
            #for element in wd.find_elements_by_xpath("//tr[class='row']"):
            for element in wd.find_elements_by_xpath("//tr[contains(@class='row')]"):
                cells = element.find_elements_by_tag_name("td")
                name_text = cells[0].text
                description_text = cells[4].text
                self.project_cache.append(ProjectMantis(name=name_text, description=description_text))

        return list(self.project_cache)