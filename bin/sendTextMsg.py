import serial
from curses import ascii

connection = '/dev/ttyUSB0'                    # port
pin = '1234'                                   # pin

def sendSMS(message, telephoneNumber):
    """Send a SMS"""
    ser = serial.Serial(connection, 9600, timeout=5)  # open port

    ser.write('AT+CPIN="%s"\r\n' %pin)                # PIN-Code
    ser.write('AT+CMGF=1\r\n')                        # to TEXTMODE

    ser.write('AT+CMGS="%s"\r\n' %telephoneNumber)    # tel number
    ser.write(message)                                # message
    ser.write(ascii.ctrl('z'))                        # end session

sendSMS('Fire - exclamation mark - fire - exclamation mark - \
         help me - exclamation mark. 123 Cavendon Road. Looking \
         forward to hearing from you. Yours truly, Maurice Moss.',
         '+4312345678')
#curl http://textmachina:5555/txtmsg/send/+431234567/Message
