print("x")
print("x")
print("x")
print("x")
print("x") 

'''
# Checkpoint (bikin commit)
0. pastikan di repo project udah git enabled (declare di folder(terminal) PASTIKAN DI CD YANG BENAR )
git init
git status untuk check

1. add files to staging area (declare file apa aja yang mau dibawa ke staging area) 
git add <filename> --> 1 file 
git add . --> all files 
git rm --cached <filename> 

2. bikin checkpoint 
git commit --> masuk ke code editor vm (virtual machine) 
git commit -m "Ini commit pertamaku --> message  
git log
git log --oneline 

BEBERAPA COMMAND

- checkout commit --> read_only (ngecek yang lama)
- revert commit --> balik ke masa lalu dan menghapus bbrp commit untuk edit
- reset commit --> balik ke masa lalu gak bisa lagi ke masa depan (commit setelahnya terhapus)

git checkout <id>
git revert <id> 
git reset <id>

BRANCH 

git branch 
git branch -a (all branch) 
git checkout -b <branch> (bikin branch baru (branch) dan langsung kerja disana)
git branch -D <branch> (delete)
git checkout <branch> 
git remote add origin https://github.com/glengunawan/tesGit.git
git push -u origin master


'''

print("x") 
print("x")