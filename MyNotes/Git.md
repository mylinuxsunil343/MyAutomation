# Version Control System

Types of VCS −
<ul>
<li>Centralized version control system (CVCS).</li>
<li>Distributed/Decentralized version control system (DVCS).</li>
</ul>
<hr>

# Git Terminology
<ul>
<li><b>Blobs:</b> Binary large objects, each version of a file represent blob. A blob holds the file data but doesn’t contain any metadata about the file.</li>
<li><b>Trees: </b>Tree is an object, it holds blob as well as other directories </li>
<li><b>Commits: </b>Commit holds the current state of the repository. </li>
<li><b>Branches: </b> Branches are used to create another line of development</li>
<li><b>Tags: </b>Tag assign a meaningful name with a specific version in the repository</li>
<li><b>Clone: </b>Clone operation creates the instance of the repository</li>
<li><b>Pull: </b>Pull opertaion copies the changes from a remote repository instance to a local one</li>
<li><b>Push: </b>Push operation copies changes from a local repository instance to a remote one</li>
<li><b>HEAD: </b>HEAD is a pointer, which always points to the latest commit in the branch</li>
<li><b>Revision: </b>Revision represents the version of the source code</li>
<li><b>URL: </b>URL represents the location of the Git repository. (Command: <code>cat .git/config</code>)</li>
</ul>
<hr>

# Git initial configuration
<code>git config --global user.name "your name"</code><br>
<code>git config --global user.email "your email"</code><br>
<code>git config --list</code><br>
<hr>

# Git work Flow
<img src="git-work-flow.jpg">
<hr>

# Git commands
Initilising repository: <code>git init</code><br>
Git Status: <code>git status -s</code><br>
Git add current changes: <code>git add .</code><br>
Git commit: <code>git commit -m 'Initial commit' </code><br>
Git logs & commit info: <code>git log</code><br>
Git remote origin: <code>git remote add origin gituser@git.server.com:project.git</code><br>
Git merge to origin: <code>git push origin master</code><br>
Git clone: <code>git clone gituser@git.server.com:project.git</code><br>
Commit details: <code>git log</code> to see commits. <code>git show commit-id</code><br>
To review changes: <code>git diff</code><br>
<hr>

# Git Stash commands

If you change your code but do not want to commit for some time, stash the changes, so will be stored in temporary space and commit later.<br>

Git stash the chnages: <code>git stash</code><br>
Git stash status: <code>git status -s</code><br>
List all stashes: <code>git stash list</code><br>
remove the changes from the stack and place them in the current working directory: <code>git stash pop</code><br>
<hr>

# Git move/remove commands
Moves a directory or a file from one location to another.<br>
Moving a file:<code>git mv << filename >> data/ </code><br>
Removing a file: <code>git rm << file name >> </code>

Commit and push to origin to make move or remove permenent <br>
<hr>

# Revet uncommited changes
Undo the modifications that have been made to the local repository. <br>
Suppose the user accidentally does some changes to his local repository and then wants to undo these changes. In such cases, the revert operation plays an important role.<br>

<b>Revert Uncommitted Changes</b><br>
Command: <code>git checkout << file name >></code><br>
You can use the git checkout command to: <br>
<ul>
<li>obtain a deleted file from the local repository.</li>
<li>Revert uncommitted changes</li>
</ul>
<b>Note</b> − We can perform all these operations before commit.<br>
<br>
<b>Remove changes from staging area</b><br>

when we perform an add operation, the files move from the local repository to the stating area. If a user accidently modifies a file and adds it into the staging area, he can revert his changes, by using the git checkout command.<br>

In Git, there is one HEAD pointer that always points to the latest commit. If you want to undo a change from the staged area, then you can use the git checkout command, but with the checkout command, you have to provide an additional parameter, i.e., the HEAD pointer. The additional commit pointer parameter instructs the git checkout command to reset the working tree and also to remove the staged changes.<br>
<br>
Command: <code>git checkout HEAD -- << file name >> </code><br>
<br>

<b>Git HEAD Options</b>
<ul>
<li><b>Soft:</b>reset the HEAD pointer only without destroying anything</li>
<li><b>Mixed: </b>reverts the changes from the staging area only. The actual changes made to the working copy of the file are <b>unaffected</b>. </li>
<li><b>Hard: </b>Clear staging area, <b>reset</b> the HEAD pointer to the latest commit, <b>delete</b> local file changes too</li>
</ul>
<hr>

# Git Tags
Tag operations allows giving a meaningful names to s specific version in the respoitory.<br>
Provide a tag name with -a option and provides a tag message with –m option.<br>
<b>commands:</b><br> 
Tagging the current push: <code>git tag -a 'Release_2023_Jan_08' -m 'January 2023 release' </code><br>
Push to origin: <code>git push origin Release_2023_Jan_08</code><br>
list all tags: <code>git tag -l</code><br>
More details of the tag: <code>git show Release_2023_Jan_08</code><br>
Deleting tags: <code>git tag -d Release_2023_Jan_08</code><br>
<hr>

# Git Patch operations

Patch is a text file, whose contents are similar to Git diff, but along with code, it also has metadata about commits; e.g., commit ID, date, commit message, etc. We can create a patch from commits and other people can apply them to their repository.<br>
<hr>

# Git Branches

<b>Commands:</b><br>
Create branch: <code>git branch branch-name</code><br>
Current branch: <code>git branch</code><br>
Switch between branches: <code>git checkout new_branch</code><br>
creates a new branch and immediately switches to the new branch<code>git checkout -b test_branch</code><br>
Delete branches<code>git branch -D test_branch</code><br>
Rename branch: <code>git branch -m new_branch newest_branch</code><br>
Merging branch: first switch to a branch andpush to another branch <code>git push origin newest_branch</code><br>
Check changes to other branch: <code>git log origin/newest_branch -2</code> 
 merging his branch with the master branch.<code>git merge origin/newest_branch</code><br>
<hr>

# Rebase Branches
The Git rebase command is a branch merge command, but the difference is that it modifies the order of commits.<br>
<br>
The Git merge command tries to put the commits from other branches on top of the HEAD of the current local branch. For example, your local branch has commits A−>B−>C−>D and the merge branch has commits A−>B−>X−>Y, then git merge will convert the current local branch to something like A−>B−>C−>D−>X−>Y<br>
<br>
The Git rebase command tries to find out the common ancestor between the current local branch and the merge branch. It then pushes the commits to the local branch by modifying the order of commits in the current local branch. For example, if your local branch has commits A−>B−>C−>D and the merge branch has commits A−>B−>X−>Y, then Git rebase will convert the current local branch to something like A−>B−>X−>Y−>C−>D.<br>
<br>
When multiple developers work on a single remote repository, you cannot modify the order of the commits in the remote repository. In this situation, you can use rebase operation to put your local commits on top of the remote repository commits and you can push these changes.<br>