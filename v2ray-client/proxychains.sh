#!/bin/bash
git clone https://github.com/rofl0r/proxychains-ng.git
cd proxychains-ng/
./configure --prefix=/usr --sysconfdir=/etc
make && make install && make install-config
sed -i 's/socks4\s*127.0.0.1\s*9050/socks5 127.0.0.1 40808/g' /etc/proxychains.conf
echo 'alias xy="proxychains4"' >> /etc/profile
source /etc/profile

