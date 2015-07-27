echo -e "[archlinuxfr]\nSigLevel = Never\nServer = http://repo.archlinux.fr/\$arch\n" >> /etc/pacman.conf
pacman -Sy yaourt --noconfirm
