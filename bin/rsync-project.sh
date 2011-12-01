#!/bin/sh
workspace=/home/yaoms/work/devel/workspace
target_prefix=/home/yaoms/work/devel/git_
project_name=$1

echo "[ -d ${target_prefix}${project_name} ] || mkdir -p ${target_prefix}${project_name}"

[ -d ${target_prefix}${project_name} ] || mkdir -p ${target_prefix}${project_name}

echo rsync --exclude=assets \
    --exclude=bin \
    --exclude=.classpath \
    --exclude=gen \
    --exclude=.project \
    --exclude=.settings \
    --exclude=proguard \
    -avP ${workspace}/${project_name}/ ${target_prefix}${project_name}/${project_name}/

rsync --exclude=assets \
    --exclude=bin \
    --exclude=.classpath \
    --exclude=gen \
    --exclude=.project \
    --exclude=.settings \
    --exclude=proguard \
    -avP ${workspace}/${project_name}/ ${target_prefix}${project_name}/${project_name}/


