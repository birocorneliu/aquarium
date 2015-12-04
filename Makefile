NPM_BIN=./node_modules/.bin

configure:
	pip install -r requirements.txt

server:
	python server.py

.PHONY: configure server
