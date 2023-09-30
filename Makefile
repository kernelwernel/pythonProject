all: run

run:	
	python3 pong.py

push:
	git add *
	git commit -m "random commit ig"
	git push
