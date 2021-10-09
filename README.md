# fedora-easyfix
A collection of self-contained and well-documented issues for newcomers to start contributing with

## How to setup the local development environment?

1. Clone the repository by executing `git clone https://github.com/t0xic0der/fedora-easyfix.git`.
2. Make the local repository your current working directory by executing `cd fedora-easyfix/`.
3. Create a new virtual environment by executing `virtualenv venv`.
4. Activate the newly created virtual environment by executing `source venv/bin/activate`.
5. Install the module by executing `python3 setup.py install`.
6. Fetch a personal access token from [here](https://github.com/settings/tokens) and store it in a `.env` file inside the same directory. 
   ```
   GITHUB_USERNAME = "<your-username-here>"
   GITHUB_API_KEY = "<your-personal-access-token-here>"
   PAGURE_API_KEY = ""
   GITLAB_API_KEY = ""
   RPLIST_URL = "<remote-http-repolist-file-location-in-yaml-format>"
   ```
7. Run `index-easyfix-issues` being in the same directory to index the Easyfix relevant issues from a variety of Git forges.
8. Run `start-easyfix-server -p 9696 -4` to start the Easyfix server.
