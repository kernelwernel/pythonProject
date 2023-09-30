all: run

run:	
	python3 main.py

push:
	git add *
	git commit -m "random commit ig"
	git push
