#!/bin/bash

cd /home/alex/programs/

wget http://c758482.r82.cf2.rackcdn.com/Sublime%20Text%202.0.2%20x64.tar.bz2
echo "download OK"

tar -jxvf Sublime*.tar.bz2
echo "tar OK"


sudo mv Sublime\ Text\ 2 /usr/lib/

sudo ln -s /usr/lib/Sublime\ Text\ 2/sublime_text /usr/bin/sublime

sudo echo "[Desktop Entry]
Name=Sublime Text 2
Comment=Editor for coding
GenericName=Text Editor

Exec=sublime
Icon=/usr/lib/Sublime\ Text\ 2/Icon/48x48/sublime_text.png
StartupNotify=false
Terminal=false
Type=Application
Categories=TextEditor:IDE:Development
X-Ayatana-Desktop-Shortcuts=NewWindow

[NewWindow Shortcuts Group]
Name=New Window
Exec=sublime -n
TargetEnvironment=Unit" > /usr/share/applications/sublime.desktop


