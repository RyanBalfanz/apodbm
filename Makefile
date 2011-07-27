APODBM_HOME=$HOME/.apodbm

get_apod:
	python $(APODBM_HOME)/apodbm.py

get_apod_rel:
	python ./src/apodbm.py

update_link: get_apod
	FILE=`python $(APODBM_HOME)/apodbm.py`
	ln -s FILE $(APODBM_HOME)/Astronomy_Picture_of_the_Day

update_apod: get_apod update_link

create_apod_dir:
	mkdir -p ~/.apodbm
	cp src/apod.py ~/.apodbm
	chmod +x $(APODBM_HOME)/apod.py

open_apod_dir:
	open ~/.apod

open_system_prefs:
	open /Applications/System\ Preferences.app/

install_osx: create_apod_dir open_apod_dir open_system_prefs

pre_install: get_apod_rel

install: pre_install install_osx

uninstall:
	rm $(APODBM_HOME)/*
	rmdir $(APODBM_HOME)/

all: update_apod
