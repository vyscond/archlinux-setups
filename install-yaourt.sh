echo '
[archlinuxfr]
SigLevel = Never
Server = http://repo.archlinux.fr/\$arch\n
' >> /etc/pacman.conf
pacman -Sy yaourt --noconfirm
