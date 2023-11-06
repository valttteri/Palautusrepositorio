from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        parsed_content = toml.loads(content)["tool"]["poetry"]
    
        test_name = parsed_content["name"]
        description = parsed_content["description"]
        dependencies = parsed_content["dependencies"]
        dev_dependencies = parsed_content["group"]["dev"]["dependencies"]
        content_license = parsed_content["license"]
        authors = parsed_content["authors"]
        

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(test_name, description, dependencies, dev_dependencies, content_license, authors)
