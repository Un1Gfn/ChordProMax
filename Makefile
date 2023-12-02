# ./chordpromax.XXX.pdf

default: s

p:
	$(HOMEBREW_PREFIX)/opt/curl/bin/curl \
	  -X POST \
	  -H "Content-Type: text/plain; charset=utf-8" \
	  --data-binary @/Users/darren/bible.NSleadsheets/1457082236.cho \
	  -O -J \
	  http://127.0.0.1:5000

s:
	flask --debug -A hello run
