#!/usr/bin/env zsh

C_A=(
  chordpro
  # -x +2
  --a2crd
  $1
)

C_T=(
  chordpro
  -x +2
  --generate=ChordPro
  $1
)

echo
echo
echo

eval "$($HOMEBREW_PREFIX/bin/perl -I$HOME/perl5/lib/perl5 -Mlocal::lib=$HOME/perl5)"

$C_A[@]
# $C_T[@]

echo
echo
echo
