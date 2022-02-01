from urllib import request
from project import Project
import tomli


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        parsed = tomli.loads(content)

        name = parsed['tool']['poetry']['name']

        description = parsed['tool']['poetry']['description']

        dependencies = parsed['tool']['poetry']['dependencies']

        dev_dependencies = parsed['tool']['poetry']['dev-dependencies']


        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, dev_dependencies)