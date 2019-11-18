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
        self.project_cache = None


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
            all_tables = wd.find_elements_by_xpath("//table[@class='width100']")
            table = all_tables[1]
            rows = table.find_elements_by_xpath(".//tr[contains(@class, 'row')]")
            del rows[0]
            for element in rows:
                cells = element.find_elements_by_tag_name("td")
                name_text = cells[0].text
                description_text = cells[4].text
               # id_n = element.find_element_by_xpath("//a[contains(@href,'manage_proj_edit_page.php?project_id')]").get_attribute("@href")
               # id = id_n[37:]

               # wd.find_element_by_xpath("//a[@href='edit.php?id=%s']" % id).click()
                self.project_cache.append(ProjectMantis(name=name_text, description=description_text))

        return list(self.project_cache)

    def delete_project(self):
        wd = self.app.wd
        self.app.open_manage_projects()
        wd.find_element_by_xpath("//a[contains(@href,'manage_proj_edit_page.php?project_id')]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Create New Project']")
        self.contact_cache = None


    #def select_project_by_index(self):
       # wd = self.app.wd
        #all_tables = wd.find_elements_by_xpath("//table[@class='width100']")
       # table = all_tables[1]
       # rows = table.find_elements_by_xpath(".//tr[contains(@class, 'row')]")
       # del rows[0]
       # rows[index].find_element_by_xpath("//a[contains(@href,'manage_proj_edit_page.php?project_id')]").click()




