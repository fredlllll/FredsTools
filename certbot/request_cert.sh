set -o nounset

domain=$1
mail=$2

certbot certonly --webroot -w /var/www/html -d "$1" --non-interactive --agree-tos -m