NAMED_CONF='''// vim:set ts=4 sw=4 et:
options {
    directory "/var/named";
    pid-file "/run/named/named.pid";
    // Uncomment these to enable IPv6 connections support
    // IPv4 will still work:
    //  listen-on-v6 { any; };
    // Add this for no IPv4:
    listen-on { {domain_ip}; };
    allow-recursion { {domain_ip}; };
    allow-transfer { none; };
    allow-update { none; };
    version none;
    hostname none;
    server-id none;
};

zone "{domain_name}" IN {
        type master;
        file "{domain_name}.zone";
        allow-update { none; };
        notify no;
};
zone "localhost" IN {
    type master;
    file "localhost.zone";
};

zone "0.0.127.in-addr.arpa" IN {
    type master;
    file "127.0.0.zone";
};

zone "1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa" {
    type master;
    file "localhost.ip6.zone";
};

zone "255.in-addr.arpa" IN {
    type master;
    file "empty.zone";
};

zone "0.in-addr.arpa" IN {
    type master;
    file "empty.zone";
};

zone "." IN {
    type hint;
    file "root.hint";
};

logging {
    channel xfer-log {
        file "/var/log/named.log";
            print-category yes;
            print-severity yes;
            severity info;
        };
        category xfer-in { xfer-log; };
        category xfer-out { xfer-log; };
        category notify { xfer-log; };
};
'''

ZONE='''$TTL    604800
@       IN      SOA     ns1.{domain_name}. admin.{domain_name}. (
                  3       ; Serial
             604800     ; Refresh
              86400     ; Retry
            2419200     ; Expire
             604800 )   ; Negative Cache TTL
;
; name servers - NS records
     IN      NS      ns1.{domain_name}.
;     IN      NS      ns2.nebula.com.

; name servers - A records
ns1.{domain_name}.          IN      A       {domain_ip}
; ns2.nebula.com.          IN      A       192.168.1.12

; 10.128.0.0/16 - A records
{domain_name}.        IN      A      {domain_ip}
*.{domain_name}.        IN      A      {domain_ip}
;host2.nyc3.example.com.        IN      A      10.128.200.102
'''

domain_name = input('[] domain name: ') or 'test.com'
domain_ip   = input('[] domain ip: ') or '0.0.0.0'

with open('/etc/hostname','w+') as f:
    f.write(
        domain_name
    )

with open('/etc/named.conf','w+') as f:
    f.write(
        NAMED_CONF.replace('{domain_name}',domain_name).replace('{domain_ip}',domain_ip)
    )

with open('/var/named/'+domain_name+'.zone','w+') as f:
    f.write(
        ZONE.format(domain_name=domain_name,domain_ip=domain_ip)
    )
