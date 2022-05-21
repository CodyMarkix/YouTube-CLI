#!/usr/bin/env bash

pyfiles=(
    ../../src/main.py
    ../../src/api/__init__.py
    ../../src/api/ytapi.py
    ../../src/frontend/__init__.py
    ../../src/frontend/menus.py
    ../../src/oobe/__init__.py
    ../../src/oobe/firstsetup.py
)

build () {
    mkdir bin && mkdir bin/Linux
    cd bin/Linux || exit 1

    pyinstaller --onefile -n "ytcli" ${pyfiles[*]}
    mv dist/ytcli ./ytcli
    rm -r build dist ytcli.spec
}

install () {
    build
    mv "ytcli" "$HOME/.local/bin/ytcli"
}

remove () {
    rm "$HOME/.local/bin/ytcli"
}

installdeps () {
    sudo apt install mpv python3-pip || sudo pacman -S mpv python-pip || sudo dnf install mpv python3-pip
    pip install requests
}

if [[ "$1" == "build" ]]; then
    build
elif [[ "$1" == "installdeps" ]]; then
    installdeps
fi