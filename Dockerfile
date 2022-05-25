FROM ubuntu:latest

# Update apt-get list, install Python, and install other appropriate dependencies
RUN apt-get update -y
RUN apt-get install -y cron
RUN apt-get install -y python3 python3-distutils python3-pip python3-apt
RUN pip3 install pyserial

# Copy over application files and grant execution rights
COPY crontab /etc/cron.d/simple-cron
COPY Binary.py .
COPY SerialSearch.py .
COPY weather-station-read.py .
COPY weather-station-read.sh .
RUN chmod +x /weather-station-read.py
RUN chmod +x /weather-station-read.sh

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/simple-cron
# Create the log file to be able to run tail
RUN touch /var/log/cron.log
# Run the command on container startup
CMD cron && tail -f /var/log/cron.log
