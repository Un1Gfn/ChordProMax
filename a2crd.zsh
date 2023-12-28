#!/usr/bin/env zsh

echo

code $1


C=(
  chordpro
  # -x +5
  --a2crd $1
)

echo
echo
echo

eval "$($HOMEBREW_PREFIX/bin/perl -I$HOME/perl5/lib/perl5 -Mlocal::lib=$HOME/perl5)"
$C[@]

echo
echo
echo
