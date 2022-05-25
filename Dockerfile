FROM ubuntu:latest

# Update apt-get list, install Python, and other appropriate dependencies
RUN apt-get update -y
RUN apt-get install -y python3 python3-distutils python3-pip python3-apt
RUN pip3 install pyserial

# Copy over application files
COPY weather-station-read.py .
COPY Binary.py .
COPY SerialSearch.py .

CMD ["python3", "weather-station-read.py"]


