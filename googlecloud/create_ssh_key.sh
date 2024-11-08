set -o nounset

filepath=$1
username=$2

ssh-keygen -t rsa -f "$filepath" -C "$username"
