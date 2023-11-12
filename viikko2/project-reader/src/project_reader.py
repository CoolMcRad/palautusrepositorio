from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        toml_str = toml.loads(content)
        toml_name = toml_str['tool']['poetry']['name']
        toml_license = toml_str['tool']['poetry']['license']
        toml_authors = toml_str['tool']['poetry']['authors']
        toml_desc = toml_str['tool']['poetry']['description']
        toml_dep = toml_str['tool']['poetry']['dependencies']
        toml_devdep = toml_str['tool']['poetry']['group']['dev']['dependencies']

        return Project(toml_name, toml_desc, toml_dep, toml_devdep, toml_license, toml_authors,)
