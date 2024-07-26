ifeq ($(OS), Windows_NT)

#If you using Windows OS
run:
	python C:\Users\HP\Documents\DPythoNet\Automation\Schedule_Push_Script\mypackage\main.py 
#You can modify path directory

install: requirements.txt
	pip install -r requirements.txt

build: setup.py
	python setup.py build bdist_wheel

clean:
	if exist "./build" rd /s /q build
	if exist "./dist" rd /s /q dist
	if exist "./myprojectname.egg-info" rd /s /q myprojectname.egg-info

#IF you using Linux OS
else
run:
	python3 C:\Users\HP\Documents\DPythoNet\Automation\Schedule_Push_Script\mypackage\main.py
#You can modify path directory

install: requirements.txt
	pip3 install -r requirements.txt

build: setup.py
	python3 setup.py build bdist_wheel

clean:
	rm -rf  build
	rm- rf dist
	rm -rf myprojectname.egg-info
endif