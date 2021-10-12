#!/usr/bin/env bash
tmprepo=${REPOSITORY/$GITHUB_REPOSITORY_OWNER/}
repo=${tmprepo/'/'}
echo Transfering Ansible folder of service $repo  
echo "The environment is:"
echo
# env
# pwd
# cd $RUNNER_TEMP
# pwd
# ls -la
# git clone $GITHUB_SERVER_URL/ldahlke/schulcloud-server
# ls -la
# ls -la schulcloud-server
# git clone https://$GITHUB_TOKEN@github.com/ldahlke/ld-ccm.git
# cp -r schulcloud-server/ansible/ ld-ccm/
# cd ld-ccm
# git config user.email "lars.dahlke@gmx.de"
# git config user.name "ldahlke"
# git add *
# git commit -m "Added ansible folder"
# # git pull
# git push
echo
echo "Goodbye"
