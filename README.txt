clear                                                                   #To clear all
cd ..                                                                   #come back one folder

#POST
select folder
git init
git add .
git commit -m 'first commit'
git remote add origin https://github.com/shubham326/djangonotes.git       #project post/upload on github
git push origin master

#Update
git status
git add .
git commit -m 'updates'
git remote add origin https://github.com/shubham326/djangonotes.git       #update push on github
git push -u origin master


#get 
git remote -v
git remote set-url origin
git remote -v                                                             #get project from github repository
git pull https://github.com/shubham326/djangonotes.git                  

