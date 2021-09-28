import os
import github

# extracting all the input from environments
version = os.environ['INPUT_VERSION']
tags = os.environ['INPUT_TAGS']
token = os.environ['INPUT_TOKEN']
labels = os.environ['INPUT_LABELS']
target = os.environ['INPUT_TARGET']

# as I said GitHub expects labels and assignees as list but we supplied as string in yaml as list are not supposed in
# .yaml format
if tags and tags != '':
    tags = tags.split(',')  # splitting by , to make a list
else:
    tags = []  # setting empty list if we get labels as '' or None

github = github.Github(token)
# GITHUB_REPOSITORY is the repo name in owner/name format in Github Workflow
repo = github.get_repo(os.environ['GITHUB_REPOSITORY'])
print(os.environ['GITHUB_REPOSITORY'])
print(version)
print(tags)
print(labels)
print(target)
