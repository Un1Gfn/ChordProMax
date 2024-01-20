#!/usr/bin/env zsh

cd ~/ChordProMax

if [[ Darwin == `uname -s` ]]; then
  source venv/bin/activate
fi

eval "$($HOMEBREW_PREFIX/bin/perl -I$HOME/perl5/lib/perl5 -Mlocal::lib=$HOME/perl5)"

export CHORDPRO=$HOME/perl5/bin/chordpro

flask $@
