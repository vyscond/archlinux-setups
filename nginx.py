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
        listen 80; # Running port
        server_name {hostname};
    }

    include sites-enabled/*.conf;

}
'''
