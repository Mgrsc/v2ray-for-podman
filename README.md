# V2ray Podman or Kubernetes or Docker

This is based on a modification of v2ray-caddy-cdn in this [repository](https://github.com/miladrahimi/v2ray-docker-compose/tree/master/v2ray-caddy-cdn), podman  pod YAML file

# V2ray-server

## USE

In this solution, you need one server (upstream) and a domain/subdomain added to a CDN service.

- Upstream Server: A server that has free access to the Internet.
- CDN Service: A Content delivery network like [Cloudflare](https://cloudflare.com/), [ArvanCloud](https://arvancloud.ir/) or [DerakCloud](https://derak.cloud/).

```
(Client) <-> [ CDN Service ] <-> [ Upstream Server ] <-> (Internet)
```

This solution provides VMESS over Websockets + TLS + CDN. 

Here is the complete step-by-step guide to set up V2Ray + Caddy (Web server) + CDN:

1. Create an `A` record in your CDN and point it to your server's IP address. Make sure to disable the proxy option.

2. Run the `./bbr.sh` script to accelerate your server's network.

3. Execute the `./setup.py` script to generate a UUID. You can use the following command:

   ```shell
   ./setup.py
   ```

4. Replace `<EXAMPLE.COM>` with your domain/subdomain in the `caddy/Caddyfile` file.

5. Run the `./deploy.sh` script to deploy V2Ray, Caddy, and CDN. Use the following command:

   ```shell
   ./deploy.sh
   ```

6. (Optional) Enable the proxy option in your CDN to activate the CDN functionality.

7. Run the `./vmess.py` script to generate client configuration files and links. Use the following command:

   ```shell
   ./vmess.py
   ```

By following these steps, you will be able to build a solution using VMESS over Websockets + TLS + CDN.





# V2ray-client

## USE

1. Use the . /vmess to generate the URL in v2ray windows desktop client to generate the config.json client file
2. Move the generated config.json to the /etc/v2ray/ directory to overwrite the original file
3. Finally, use `podman-compose up -d` or `docker-compose up -d` to run

## [Proxychains](https://github.com/rofl0r/proxychains-ng)

```
 ProxyChains is a UNIX program, that hooks network-related libc functions
  in DYNAMICALLY LINKED programs via a preloaded DLL (dlsym(), LD_PRELOAD)
  and redirects the connections through SOCKS4a/5 or HTTP proxies.
  It supports TCP only (no UDP/ICMP etc).

  The way it works is basically a HACK; so it is possible that it doesn't
  work with your program, especially when it's a script, or starts
  numerous processes like background daemons or uses dlopen() to load
  "modules" (bug in glibc dynlinker).
  It should work with simple compiled (C/C++) dynamically linked programs
  though.

  If your program doesn't work with proxychains, consider using an
  iptables based solution instead; this is much more robust.

  Supported Platforms: Linux, BSD, Mac, Haiku.
```

## USE

`proxychains.sh`in `/v2ray-podman/v2ray-client`

If you want to change the port number, please change it in the last line of /etc/proxychains.conf file

Finally you can use `xy` to let the programs that need it go through the proxy

such as ` xy curl cip.cc`

