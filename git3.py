1.帮助
git --help
git [command] -h
git [command] --help

2.local和github的身份认证
git config --global user.name   
#user.name问题不大，重点是下面四个email要能对应得上;--global:作为全局变量
git config --global user.email "youremail@example.com"
ssh-keygen -t rsa -C "youremail@example.com"        # git会访问c:/users/levi/.ssh/rsa;-t:选择加密类型;-C:注释
github.com/settings/emails -> 填写Primary邮箱
github.com/settings/keys -> 填写邮箱rsa_key
#github会根据这四条信息来识别local的身份

3.git查询
git status  #状态查询
git log     #历史查询
git branch  #分支查询
git branch -a   #远程分支查询
git config --list   #变量查询

3.拷贝/更新远程仓库
git clone git@github.com:xxx/xxx.git    #第一次拷贝
git fork  git@github.com:xxx/xxx.git    #https://www.cnblogs.com/chenweichu/articles/6715521.html

git fetch ['分支名']      #获取(所有)远程分支最新版本
git pull  ['分支名']      #获取(所有)远程分支最新版本并自动合并

4.创建/切换/合并/删除/回退 本地分支/远程分支
git branch '分支名'          #创建本地分支
git push -u origin '分支名'  #创建远程分支;origin指的是远程仓库;-u:建立与远程仓库某个分支的联系
git checkout '分支名'        #切换本地分支
git merge '分支名'           #合并本地分支
git branch -d '分支名'       #删除本地分支
git push origin - '分支名'   #删除远程分支;-d:删除
git reset --hard <HEAD^ / commit码>     #回退本地分支;--hard:reset HEAD, index and working tree
git push -f                 #回退远程分支;-f:强迫更新;警告!慎用！一定要先pull再push!

5.添加和快照
git add     #添加
git commit -m 'xxx'     #快照;-m:message

6.alias
#删除变量
git config --global unset 
#优化log
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
#快速commit
git config --global alias.qc '!git add -A && git commit -m'
