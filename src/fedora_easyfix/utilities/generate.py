"""
    Copyright (c) 2021 Fedora Websites and Apps

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""

from json import dumps
from sys import exit
from time import time

from dotenv import dotenv_values
from fedora_easyfix.__init__ import __version__
from fedora_easyfix.utilities.compose import StatusDecorator
from fedora_easyfix.utilities.github import GitHubRepositories
from fedora_easyfix.utilities.pagure import PagureRepositories
from yaml import CLoader, load

statdcrt = StatusDecorator()


def write_index_to_local_json(ticket_collection):
    try:
        tickdata = dumps(ticket_collection, indent=4)
        with open("tickdata.json", "w") as tickfile:
            tickfile.write(tickdata)
        statdcrt.section("Indexing complete!")
    except Exception as expt:
        statdcrt.failure("Could not index tickets")
        statdcrt.general("Please check if appropriate permissions are available to write in the directory")
        exit()


def mainfunc():
    statdcrt.section("Indexing tickets...")
    try:
        envrvars = dotenv_values(".env")
        github_username = envrvars["GITHUB_USERNAME"]
        github_api_key = envrvars["GITHUB_API_KEY"]
        pagure_api_key = envrvars["PAGURE_API_KEY"]
        with open("repolist.yml", "r") as yamlfile:
            yamldict = load(yamlfile.read(), Loader=CLoader)
        if yamldict["repolist_version"] == __version__:
            ticket_collection = {}
            if "github" in yamldict["forges"].keys():
                github_repository_list = yamldict["forges"]["github"]["repositories"]
                github_base_url = yamldict["forges"]["github"]["url"]
                statdcrt.warning("Found %s repositories on GitHub" %len(yamldict["forges"]["github"]["repositories"].keys()))
                ticket_collection["github"] = GitHubRepositories(
                    github_repository_list,
                    github_base_url,
                    github_api_key,
                    github_username
                ).return_repository_collection()
            if "pagure" in yamldict["forges"].keys():
                pagure_repository_list = yamldict["forges"]["pagure"]["repositories"]
                pagure_base_url = yamldict["forges"]["pagure"]["url"]
                statdcrt.warning("Found %s repositories on Pagure" %len(yamldict["forges"]["pagure"]["repositories"].keys()))
                ticket_collection["pagure"] = PagureRepositories(
                    pagure_repository_list,
                    pagure_base_url,
                    pagure_api_key
                ).return_repository_collection()
            ticket_collection["collection_updated_at"] = time()
            write_index_to_local_json(ticket_collection)
        else:
            statdcrt.failure("Could not index tickets")
            statdcrt.general("Repolist version does not correspond with the Easyfix version")
    except Exception as expt:
        statdcrt.failure("Could not index tickets")
        statdcrt.general("Please check if the repolist.yml and .env are present in the same directory")
        exit()


if __name__ == "__main__":
    mainfunc()
