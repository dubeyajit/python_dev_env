# Base image
FROM ubuntu:20.04

# Setting repository
RUN apt-get update && apt upgrade -y
RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa

# Setting env
ENV DEBIAN_FRONTEND=noninteractive 

# Python installation
RUN apt-get install python3.10 -y
RUN apt-get install python-is-python3
RUN apt install python3-pip -y
# Requirements installation
COPY workdir/requirements.txt .
RUN pip install -r requirements.txt

# User & user directory
# Set up a non-root user
RUN useradd ajitdubey

USER ajitdubey
WORKDIR /home/ajitdubey/
RUN mkdir workdir

CMD ["bash"]