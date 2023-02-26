# Working with APIs
# api = application programming interface
# Automatically request specific information rather than entire pages.

# Using a Web API
# Programs use very specific URLs to request information. This is an 'API call'.
# Data will be returned in an easily processed format such as JSON or CSV

# Processing an API Response

import requests

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

# Specify version of API
headers = {'Accept': 'application/vnd.github.v3+json'}

# Make the API call
# Call get() and pass the URL and headers, and assign the response to variable r
# Response object has an attribute 'status_code', which tells if request success
# 200 is a successful response
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable.
response_dict = r.json()

# Working with the Response Dictionary
print(f"Total repositories: {response_dict['total_count']}")

# Explore information about the repositories.
# Items contains a list of dictionaries, with data on each Python repo.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository.
repo_dict = repo_dicts[0]
#print(f"\nKeys: {len(repo_dict)}")
#for key in sorted(repo_dict.keys()):
#    print(key)

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")