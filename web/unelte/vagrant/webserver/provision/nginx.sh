#!/bin/bash
set -euox pipefail

echo "Deschidem portul 80."
sudo ufw allow 80

echo "Repornim serviciile."
sudo service nginx restart
sudo service php5-fpm restart
echo "Am terminat."
