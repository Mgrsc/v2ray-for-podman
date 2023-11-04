#!/bin/bash

# 停止并删除 caddy 容器
podman stop caddy-2.6.2
podman rm -f caddy-2.6.2

# 停止并删除 v2ray 容器
podman stop v2ray
podman rm -f v2ray

