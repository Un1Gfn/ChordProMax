#!/usr/bin/env zsh

CMD=(
  $HOMEBREW_PREFIX/opt/curl/bin/curl
  -X POST
  -H "Content-Type: text/plain; charset=utf-8"
  --data-binary @$3
  # -O -J
  --output $2
  http://$1
)

for i in $CMD[@]; do echo $i; done

$CMD[@] $@; exit
