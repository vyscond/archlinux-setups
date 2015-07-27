NGINXCONF='''
# {app_name}'s config for Nginx
server {
    listen 80; # Running port
    server_name {app_name}{hostname};
    location / {
        proxy_pass http://127.0.0.1:{app_port}/;
        #proxy_redirect     off;
        #proxy_set_header   Host $host;
        #proxy_set_header   X-Real-IP $remote_addr;
        #proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
        #proxy_set_header   X-Forwarded-Host $server_name;
    }
    location /static/  {
        root /home/git/{app_name}/static_root/;
    }
}
'''


app_name = input('[] app name: ')
app_port = int(input('[] app port: '))

if app_name and app_port :
    with open('/etc/hostname','r') as f:
        hostname=''.join(f)
    with open('/etc/nginx/sites-enabled/'+app_name+'.conf','w+') as f:
        f.write(
            NGINXCONF.replace('{app_name}',app_name)
                .replace('{app_port}',app_port)
                .replace('{hostname}',hostname)
        )
else :
    print("can't do anything without a valid name")
