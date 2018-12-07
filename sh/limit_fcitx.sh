#!/bin/sh

for pid in `pidof fcitx`
do 
    nohup cpulimit -p $pid -l 30 -b 1>/dev/null 2>/dev/null &
done

limit_fcitx_sh=/var/www/github/cyy-code/sh/limit_fcitx.sh
if grep "limit_fcitx.sh" /etc/rc.local; then
    echo "limit_fcitx.sh is in /etc/rc.local"
else
    sed -i "s/^exit 0$/\nexit 0/" /etc/rc.local
    sed -i "s/^exit 0$/# By alex\nexit 0/" /etc/rc.local
    sed -i "s|^exit 0$|nohup $limit_fcitx_sh \&\nexit 0|" /etc/rc.local
fi
