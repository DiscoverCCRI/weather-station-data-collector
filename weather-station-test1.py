import serial
import time
import binascii
import Binary


class WeatherStation:
    def __init__(self, portx, bps, timex):
        self.portx = portx  # set port name
        self.bps = bps  # set port baud rate
        self.timex = timex  # set timeout limit
        self.TemperatureRTU = bytes.fromhex('26 04 00 00 00 02 77 1C')  # Request for Air temperature
        self.HumidityRTU = bytes.fromhex('26 04 00 02 00 02 D6 DC')  # Request for Air humidity
        self.PressureRTU = bytes.fromhex('26 04 00 04 00 02 36 DD')  # Request for barometric pressure
        self.LightRTU = bytes.fromhex('26 04 00 06 00 02 97 1D')  # Request for Light intensity
        self.MinDirectionRTU = bytes.fromhex('26 04 00 08 00 02 F6 DE')  # Request for Minimum wind direction
        self.MaxDirectionRTU = bytes.fromhex('26 04 00 0A 00 02 57 1E')  # Request for Maximum wind direction
        self.AvgDirectionRTU = bytes.fromhex('26 04 00 0C 00 02 B7 1F')  # Request for Average wind direction
        self.MinSpeedRTU = bytes.fromhex('26 04 00 0E 00 02 16 DF')  # Request for Minimum wind speed
        self.MaxSpeedRTU = bytes.fromhex('26 04 00 10 00 02 76 D9')  # Request for Maximum wind speed
        self.AvgSpeedRTU = bytes.fromhex('26 04 00 12 00 02 D7 19')  # Request for Average wind speed
        self.AccRainRTU = bytes.fromhex('26 04 00 14 00 02 37 18')  # Request for Accumulated rainfall
        self.AccDurationRTU = bytes.fromhex('26 04 00 16 00 02 96 D8')  # Request for Accumulated rainfall duration
        self.RainIntensityRTU = bytes.fromhex('26 04 00 18 00 02 F7 1B')  # Request for Rain intensity
        self.MaxRainIntensityRTU = bytes.fromhex('26 04 00 1A 00 02 56 DB')  # Request for Maximum rainfall intensity
        self.ser = serial.Serial(self.portx, self.bps, timeout=self.timex)  # initialize serial port
        self.ser.close()  # close the port

    def Readhex(self, rtu):
        """
        Function: Read hex value from serial port
        :param rtu: 8 bytes hex value Request sent by host
        :return: 9 bytes hex value in string format
        """
        # self.ser.open()
        self.ser.write(rtu)
        time.sleep(0.2)
        data_len = self.ser.inWaiting()
        if data_len:
            rec_datahex = str(binascii.b2a_hex(self.ser.read(data_len)))[2:-1]
            # print("Read Success")
            # self.ser.close()
            return rec_datahex
        else:
            # self.ser.close()
            print("Read Timeout!")

    def Readbin(self, rtu):
        """
        Function: Read binary value from serial port
        :param rtu: 8 bytes hex value. Request sent by host
        :return: 72 bits binary value in string format
        """
        rec_databin = Binary.tobin(self.Readhex(rtu))
        return rec_databin

    def Getdata(self, rtu):
        """
        Function: Get measurement data like humidity, light intensity, etc.
        rec_databin = big endian Data format int32. Divide the data value by 1000 to get the true measurements.
        :param rtu: 8 bytes hex value. Request sent by host.
        :return: True measurement value
        """
        if rtu == self.TemperatureRTU:
            rec_databin = self.Readbin(self.TemperatureRTU)
            data = Binary.twos(rec_databin[24:56]) / 1000
        else:
            rec_datahex = self.Readhex(rtu)
            data = int(rec_datahex[6:14], 16) / 1000
        return data


if __name__ == "__main__":
    w = WeatherStation("/dev/ttyUSB0", 9600, 5)
    while True:
        w.ser.open()
        t = w.Getdata(w.TemperatureRTU)
        print("Temperature:", "%.3f" % t, "C")
        h = w.Getdata(w.HumidityRTU)
        print("Humidity:", "%.3f" % h, "%RH")
        p = w.Getdata(w.PressureRTU)
        print("Pressure:", "%.3f" % p, "Pa")
        l = w.Getdata(w.LightRTU)
        print("Light Intensity:", "%.3f" % l, "cd")
        print("")
        w.ser.close()
        time.sleep(1)
