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
<li><b><u>Soft:</u>reset</b> the HEAD pointer only without destroying anything</li>
<li><b><u>Mixed: </u>reverts</b> the changes from the staging area only. The actual changes made to the working copy of the file are <b>unaffected</b>. </li>
<li><b><u>Hard: </u>Clear</b> staging area, <b>reset</b> the HEAD pointer to the latest commit, <b>delete</b> local file changes too</li>
</ul>