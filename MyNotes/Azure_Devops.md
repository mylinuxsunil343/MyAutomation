<h3>Azure Boards</h3>
Choose a process flow or process template to work in Azure Boards<br>
<ol>
<li>Basic</li>
<li>Agile</li>
<li>Scrum</li>
<li>Capability Maturity Model Integration (CMMI)</li>
</ol>

# Azure Repos

Open azure devops board -> Repos -> Select the repo name from dropdown
1. Open the repo in visual studio code.
2. Add files / changes to the repo
3. git add, commit in VS Code
4. copy paste git push command from azure devops & merge. (It may ask password, you canm generate in azure devops)

<b>Azure Devops - Branches</b>
VSCode
- git checkout -b FeatureB
- Do necessary changes to the code
- git stage, commit
- check out to main using <code>git ceckout main</code>
- Push using <code>git push -u origin --all</code>

Azure devops:<br>
You can select featureB branch from dropdown and check changes<br>

<b>Azure devops - Pull Request</b>

- Select : in the line featureB branch in Azure devops
- Create "New pull request "
- Click complete to merge featureB branch changes main branch
Process completed. After merged, featureB branch will be deleted<br>