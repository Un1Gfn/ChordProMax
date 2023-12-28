# ./chordpromax.XXX.pdf

# conflict with AirPlay receiver
PORT:=5000
IP:=127.0.0.1
CHO:=tmp.cho
PDF:=tmp.pdf

.SILENT: help
.PHONY: help
help:
	echo
	echo $(MAKE) a - a2crd
	echo $(MAKE) c - delete PDF
	echo $(MAKE) s - flask
	echo $(MAKE) e - entr
	echo $(MAKE) o - open
	echo
	@ # echo '$(MAKE) 0 - code + a2crd'
	echo '$(MAKE) 2 -               flask + entr'
	echo '$(MAKE) 3 -        open + flask + entr'
	echo '$(MAKE) 4 - code + open + flask + entr'
	echo

4:
	code tmp.cho
	$(MAKE) emptypdf
	$(MAKE) o
	$(MAKE) -j2 s e

3:
	$(MAKE) o
	$(MAKE) emptypdf
	$(MAKE) -j2 s e

2:
	$(MAKE) -j2 s e

# 0:
# 	code tmp.txt a2crd.zsh

o:
	open $(PDF)

e:
	ls -1 tmp.cho conf.prp | entr -p ./post.zsh $(IP):$(PORT) $(PDF) $(CHO)

s:
	./flask.zsh -A myapp run -h $(IP) -p $(PORT) --debug

c:
	rm -fv $(PDF)

# https://unix.stackexchange.com/questions/277892/how-do-i-create-a-blank-pdf-from-the-command-line
emptypdf:
	gs -sDEVICE=pdfwrite -o $(PDF) -g5950x8420 -c showpage

a:
	@./a2crd.zsh tmp.txt
