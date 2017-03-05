FROM ubuntu:16.04

MAINTAINER Walter Tuholski <wtuholski@vigilent.com>

# Update apt
RUN apt-get -y update 

#------------------------------------------------
# Install python 
#------------------------------------------------
# Install python 2.7 and development tools
RUN apt-get -y install python2.7 python-dev python-pip 

RUN apt-get -y update 

# Install Numpy and Pandas dependencies
RUN apt-get -y install python-pandas        

RUN mkdir -p /var/lib/python_dev_base

#------------------------------------------------
# Copy the application 
#------------------------------------------------
COPY ./src/foo.py /foo.py

#------------------------------------------------
# Run python application
#------------------------------------------------

# default command
CMD ["/usr/bin/python", "/foo.py"]


