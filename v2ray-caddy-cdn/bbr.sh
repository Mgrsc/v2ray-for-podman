#!/bin/bash
set -e
su -c "bash <(wget -qO- https://github.com/teddysun/across/raw/master/bbr.sh)" root
