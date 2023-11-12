from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        content1 = toml.loads(content)
        # Access values from the config
        name = content1["tool"]["poetry"]["name"]
        description = content1["tool"]["poetry"]["description"]
        licencse = content1["tool"]["poetry"]["license"]
        authors = content1["tool"]["poetry"]["authors"]
        dependencies = content1["tool"]["poetry"]["dependencies"]
        dev_dependencies = content1["tool"]["poetry"]["group"]["dev"]["dependencies"]
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, licencse, authors, dependencies, dev_dependencies)


