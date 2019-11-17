#задание 10
from selenium import webdriver
from fixture.project_mantis import ProjectMantisHelper
from fixture.session import SessionHelper



class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)

        self.wd.implicitly_wait(3)
        self.session = SessionHelper(self)
        self.project_mantis = ProjectMantisHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("/my_view_page.php") and len(wd.find_element_by_xpath("//a[contains(text(),'Unassigned')]")) > 0):
            wd.get(self.base_url)


    def open_projects_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("/manage_proj_create_page.php") and len (wd.find_element_by_xpath("//input[@value='Add Project']")) > 0):
            #and len(wd.find_elements_by_name("new")) > 0
            # переход в раздел "управление"
            wd.find_element_by_link_text("Manage").click()
            # переход в раздел "управление проектами"
            wd.find_element_by_link_text("Manage Projects").click()
            # нажатие кнопки "создать новый проект"
            wd.find_element_by_xpath("//input[@value='Create New Project']").click()


    def open_manage_projects(self):
        wd = self.wd
        if not (wd.current_url.endswith("/manage_proj_page.php") and len (wd.find_element_by_xpath("//input[@value='Create New Project']")) > 0):
            #and len(wd.find_elements_by_name("new")) > 0
            # переход в раздел "управление"
            wd.find_element_by_link_text("Manage").click()
            # переход в раздел "управление проектами"
            wd.find_element_by_link_text("Manage Projects").click()



    def destroy(self):
        self.wd.quit()
