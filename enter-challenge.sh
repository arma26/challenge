#!/usr/bin/env bash

# make logging into different challenge sites easier
# requires: sshpass, levels.txt
# levels.txt contain 1 triplet per line, in the format of "<url> <user> <password>"

# the pair of URL and USER should be unique
# ssh USER@URL should be a valid login

URL="$1"
LEVEL="$2"
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

CREDS="$(cat "$DIR/level-logins.txt" |
  grep $URL |
  grep $LEVEL)"
# shellcheck disable=2046
read site user pass <<< $(echo "$CREDS")
echo "login: $CREDS"
eval "sshpass -p $pass ssh $user@$site"
