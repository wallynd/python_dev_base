default: clean-containers build

build:  
	docker build -t python_dev_base .


start:
	docker run  --name python_dev_base  python_dev_base

run:
	docker run -it --entrypoint="bash -c '/usr/bin/python /foo.py'" python_dev_base 

attach:
	docker run -it --entrypoint=bash python_dev_base 

clean: stop clean-containers clean-image

stop: 
	@CIDS=`docker ps -aq` && if [ -z "$$CIDS" ]; then echo "No Containers Running"; else docker stop $$CIDS; fi 

clean-containers: 
	@CIDS=`docker ps -aq` && if [ -z "$$CIDS" ]; then echo "No Containers Exited"; else docker rm $$CIDS; fi 

clean-image: clean-containers
	@echo "Removing Python Dev Base image" && docker rmi python_dev_base
