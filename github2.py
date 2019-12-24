from github import Github

# using username and password
# g = Github("user", "password")

# or using an access token
g = Github("b55d312da577ba479f7dc4f8f3f5b1384bdf3b2e")

# Github Enterprise with custom hostname
# = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")

for repo in g.get_user("datarepresentationstudent/aPrivateOne").get_repos():
    print(repo.name)
    repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    print(dir(repo))