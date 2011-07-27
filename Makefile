get_apod:
	python ~/.apod/apod.py

update_link: get_apod
	FILE=`python ~/.apod/apod.py`
	ln -s FILE ~/.apod/Astronomy_Picture_of_the_Day

update_apod: get_apod update_link

create_apod_dir:
	mkdir -p ~/.apod
	cp src/apod.py ~/.apod
	chmod +x ~/.apod/apod.py

open_apod_dir:
	open ~/.apod

open_system_prefs:
	open /Applications/System\ Preferences.app/

install_osx: create_apod_dir open_apod_dir open_system_prefs

pre_install:
	python ./src/apod.py

install: pre_install install_osx

uninstall:
	rm ~/.apod/*
	rmdir ~/.apod/

all: update_apod
