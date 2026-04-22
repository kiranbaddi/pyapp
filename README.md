# Overview

This is a repository created to understand how Software is version controlled with git.

git is a a predominatnly used version control system

## Working , Staging and Repository

git considers all the changes to be in working directory. You can add the files to the staging area by using `git add <files>` and move from staging area to repository by using `git commit`



## Remote repository

you can link your local repo with a remote repository using the command
git remote add <remote_name> <repo_url>

ex: git remote add origin git@github:<org>/repo.git

You can add multiple remotes to your local repo

Can we push to repos at the same time? Le'ts try