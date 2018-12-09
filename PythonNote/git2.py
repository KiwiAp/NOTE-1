一、本地基础操作
1.下载

2.注册信息
git config --global user.name "Your Name"
git config --global user.email "email@example.com"

3.建立git仓库
git init

4.新文件
git status
↓
git add <文件名>    ||  git add -A(提交所有变化)
↓
git commit -m "commit版本"

5.修改文件
git status
↓
git diff
↓
git add <文件名>    ||  git add -A(提交所有变化)
↓
git commit -m "commit版本"

6.版本回退
git log     ||  git log --pretty=oneline    ||  git reflog
↓
git reset --hard HEAD^  ||HEAD^^    ||HEAD~3

6.2 指定版本
git log     ||  git log --pretty=oneline    ||  git reflog
↓
git reset --hard <版本号>

7.撤销工作区修改
git checkout -- <文件名>    ||  git checkout -- .(撤销所有修改)

8.从暂存区回退工作区
git reset HEAD <文件名>



二、github远程库操作
0.申请公私钥
$ ssh-keygen -t rsa -C "youremail@example.com"

1.找到公私钥
用户主目录 → .ssh → id_rsa(私钥)+id_rsa.pub(公钥，记事本打开)

2.github上添加SSH key
github → Account setting → SSH keys → New SSH key → 粘贴id_rsa.pub内容

3.新建远程库关联本地
在github上建一个仓库
↓
git remote add origin git@github.com:Levi-Hope/test.git
↓
git push -u origin master

3.2从已有远程库克隆至本地
git clone git@github.com:Levi-Hope/test.git

4.推送至远程库
git push origin master

5.查看远程库信息
git remote  ||  git remote -v

6.将分支与远程库分支关联
git branch --set-upstream-to=origin/dev dev

7.建立与远程库分支关联的分支
git checkout -b branch-name origin/branch-name

8.抓取远程库分支
git pull



三、分支管理
1.创建新分支
git branch
↓
gir branch <分支名>
↓
git checkout <分支名>

2.合并分支
git merge <分支名>  ||  git merge --no-ff -m "merge with no-ff" dev(取消快速合并，保留分支信息)

2.2查看分支合并情况
git log --graph ||    git log --graph --pretty=oneline --abbrev-commit

3.删除分支
git branch -d <分支名>

4.stash保存现场
git stash

5.stash恢复现场
git stash list
↓
git stash apply + git stash drop    ||  git stash pop



四、标签
1.添加标签
git tag(查看标签)
↓
git tag v1.0    ||  git tag v1.0 <版本号>

2.查看标签详情
git show <标签名>

3.删除标签
git tag -d <标签名>

4.推送标签
git push origin <标签名>    ||  git push origin --tags

5.删除远程库标签
先在本地删除
↓
git push origin :refs/tags/<标签名>



五、参与开源项目、.gitignore、
https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/00137628548491051ccfaef0ccb470894c858999603fedf000
