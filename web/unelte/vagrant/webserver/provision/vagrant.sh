#!/bin/bash
set -euox pipefail

mkdir -p "/vagrant/.log"
mkdir -p "/vagrant/.www"

adduser vagrant www-data
export DEBIAN_FRONTEND=noninteractive

echo "Adăugăm sursa de pachete pentru PHP5."
cat <<EOF > /etc/apt/sources.list.d/php5-oldstable.list
deb http://ppa.launchpad.net/ondrej/php5-oldstable/ubuntu precise main
deb-src http://ppa.launchpad.net/ondrej/php5-oldstable/ubuntu precise main
EOF
apt-key adv -q \
    --keyserver "keyserver.ubuntu.com" \
    --recv-keys "4F4EA0AAE5267A6C" &> /dev/null

echo "Adăugăm sursa de pachete pentru nginx."
cat <<EOF > /etc/apt/sources.list.d/nginx.list
deb http://nginx.org/packages/ubuntu/ precise nginx
deb-src http://nginx.org/packages/ubuntu/ precise nginx
EOF
wget -q -O- "http://nginx.org/keys/nginx_signing.key" | apt-key add - > /dev/null

echo "Adăugăm opțiunile dorite pentru serverul de mysql."
cat << EOF > /root/.my.cnf
[client]
    user=root
    password=vagrant
EOF

cat << EOF > /home/vagrant/.my.cnf
[client]
    user=root
    password=vagrant
EOF

debconf-set-selections <<< 'mysql-server-5.5 mysql-server/root_password password vagrant'
debconf-set-selections <<< 'mysql-server-5.5 mysql-server/root_password_again password vagrant'
debconf-set-selections <<< 'phpmyadmin phpmyadmin/dbconfig-install boolean true'
debconf-set-selections <<< 'phpmyadmin phpmyadmin/mysql/admin-pass password vagrant'
debconf-set-selections <<< 'phpmyadmin phpmyadmin/app-password-confirm password vagrant'
debconf-set-selections <<< 'phpmyadmin phpmyadmin/mysql/app-pass password vagrant'
debconf-set-selections <<< 'phpmyadmin phpmyadmin/reconfigure-webserver multiselect apache2'

echo "Actualizăm lista de pachete disponibile."
apt-get update -y &> /dev/null

echo "Instalăm pachetele dorite"
apt-get -o Dpkg::Options::="--force-confold" install -qy \
    nginx php5-fpm php5-gd php5-curl php5-xdebug php5-mysql php5-cli php5-dev php-pear \
    mysql-server-5.5 build-essential avahi-daemon > /dev/null
apt-get -o Dpkg::Options::="--force-confold" install -qy phpmyadmin > /dev/null
apt-get install -qy unzip curl

echo "Configurăm serverul web."
rm -rf "/etc/nginx"
cp -r "/vagrant/provision/nginx" "/etc/nginx"

rm -f "/etc/php5/fpm/pool.d/www.conf"
cat <<EOF >/etc/php5/fpm/pool.d/vagrant.conf
[vagrant]

prefix = /vagrant/
user = vagrant
group = vagrant
listen = /var/run/php5-vagrant.sock
listen.owner = vagrant
listen.group = vagrant
listen.mode = 0660
pm = static
pm.max_children = 5
pm.max_requests = 500
pm.status_path = /gitium/fpm-status
ping.path = /gitium/fpm-ping
env[ENV] = vagrant

access.log = /vagrant/.log/php-access.log
access.format = "%R - %u %t \"%m %r%Q%q\" %s %f %{mili}d %{kilo}M %C%%"
EOF
cp "/vagrant/provision/php.ini" "/etc/php5/fpm/php.ini"
