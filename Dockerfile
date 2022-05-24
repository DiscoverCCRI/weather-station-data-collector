FROM ubuntu:latest

# Install Python and appropriate dependencies
RUN apt install -y python3 python3-distutils python3-pip python3-apt
RUN pip3 install pyserial

# Copy over
COPY weather-station-read.py .
COPY Binary.py .
COPY SerialSearch.py .

CMD ["python3", "weather-station-read.py"]


