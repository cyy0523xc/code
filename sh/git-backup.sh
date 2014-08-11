#!/bin/bash

# 代码库的自动备份脚本
# 每天有计划任务执行（cron）
# @author cyy0523xc@gmail

# git.url="git@git.ibbd.net"
backup.path=""

git_clone_mirror() {
    url="git@git.ibbd.net"
    git clone --mirror $url:$project/$repo  
    pushd $repo
    git remote update  
    popd
}

# 备份根目录
cd /home/code/backup-ibbd/

# 执行配置文件
. sh git-backup-config.sh






