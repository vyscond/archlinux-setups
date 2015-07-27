NGINXCONF='''
#user html;
worker_processes  1;

events {
    worker_connections  5;
}


http {

    include       mime.types;
    default_type  application/octet-stream;
    #access_log  logs/access.log  main;
    sendfile        on;
    #tcp_nopush     on;
    keepalive_timeout  0;
    gzip              on;
    gzip_http_version 1.0;
    gzip_proxied      any;
    gzip_min_length   500;
    gzip_disable      "MSIE [1-6]\.";
    gzip_types        text/plain text/xml text/css
        text/comma-separated-values
        text/javascript
        application/x-javascript
        application/atom+xml;

    server {
        listen       80;
        server_name  {hostname};
        #charset koi8-r;
        #access_log  logs/host.access.log  main;
        location / {
            root   /usr/share/nginx/html;
            index  index.html index.htm;
        }
        #error_page  404              /404.html;
        # redirect server error pages to the static page /50x.html
        #
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   /usr/share/nginx/html;
        }
    }

    include sites-enabled/*.conf;

}
'''

with open('/etc/hostname','r') as f:
    hostname=''.join(f)
with open('/etc/nginx/nginx.conf','w+') as f:
    f.write(
        NGINXCONF.replace('{hostname}',hostname)
    )
