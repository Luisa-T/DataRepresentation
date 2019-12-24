from github import Github 
 
# remove the minus sign from the key 
g = Github("b55d312da577ba479f7dc4f8f3f5b1384bdf3b2e") 
 
for repo in g.get_user().get_repos():     
    print(repo.name)