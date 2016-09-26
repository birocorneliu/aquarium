NPM_BIN=./node_modules/.bin

configure:
	pip install -r requirements.txt

server:
	python raspberry/server.py

.PHONY: configure server
