# YouTube CLI - A YouTube client in the Terminal

<h2>Table of contents</h2>

- [YouTube CLI - A YouTube client in the Terminal](#youtube-cli---a-youtube-client-in-the-terminal)
  - [What is this?](#what-is-this)
  - [Installing](#installing)
  - [Building from source](#building-from-source)

## What is this?

So, let's face it. You're one of... those Linux users. You know the ones.


- The ones that use Lenovo ThinkPads because they have FOSS firmware/drivers
- The ones that daily drive a WM instead of a DE
- The ones that haven't used a mouse in 10 years
- The ones that always beat their friends in Typeracer because they exclusively use a keyboard every day.

But somehow, you still use YouTube to watch videos. And you have to use the dinky-ass GUI browser to watch a video!

Well, this program solves that! A client for YouTube used completely in the terminal!

## Installing

For this program you will need the following:

- Python 3.x (If you want to build from source)
- MPV player

Simply run this command...

```bash
wget https://github.com/CodyMarkix/Youtube-CLI/releases/download/latest/ytcli-x86-64 -O $HOME/.local/bin/ytcli
```

...and it'll be installed.

If there's a problem starting the program, check that `~/.local/bin` is in your PATH variable.

## Building from source

Clone the repository.

```bash
git clone https://github.com/CodyMarkix/Youtube-CLI
```

Cd into it, install the dependencies and run the build script.

```bash
cd Youtube-CLI && ./make installdeps && ./make build
```

If you want to install from source, run `./make install` instead of `./make build`.