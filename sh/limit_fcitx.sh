#!/bin/sh

for pid in `pidof fcitx`
do 
    nohup cpulimit -p $pid -l 30 -b 1>/dev/null 2>/dev/null &
done

limit_fcitx_sh=/var/www/github/cyy-code/sh/limit_fcitx.sh
limit_fcitx_sh_p="${limit_fcitx_sh//\//\\\/}"
echo $limit_fcitx_sh_p
if grep "limit_fcitx.sh" /etc/rc.local; then
    "limit_fcitx.sh had beed in /etc/rc.local"
else
    sed -i "s/^exit 0$/\nexit 0/" /etc/rc.local
    sed -i "s/^exit 0$/\n# By limit_fcitx.sh\nexit 0/" /etc/rc.local
    sed -i "s/^exit 0$/\nnohup $limit_fcitx_sh_p &\nexit 0/" /etc/rc.local
fi
