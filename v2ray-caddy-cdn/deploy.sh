#!/bin/bash
mkdir $(pwd)/caddy/{data,config}
mkdir $(pwd)/v2ray/logs
podman run -d --net host --volume "$(pwd)/caddy/Caddyfile:/etc/caddy/Caddyfile" \
  --volume "$(pwd)/caddy/web/:/usr/share/caddy" \
  --volume "$(pwd)/caddy/data/:/data/caddy/" \
  --volume "$(pwd)/caddy/config/:/config/caddy" \
  --name caddy-2.6.2 ghcr.io/getimages/caddy:2.6.2-alpine

podman run -d --name v2ray \
  -p 127.0.0.1:51310:1310 \
  --volume "$(pwd)/v2ray/config/:/etc/v2ray/" \
  --volume "$(pwd)/v2ray/logs/:/var/log/v2ray/" \
  ghcr.io/getimages/v2fly-core:v4.45.2

