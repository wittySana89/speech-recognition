import speech_recognition as sr
import pyaudio
import serial

r = sr.Recognizer()
r.dynamic_energy_threshold=False

with sr.Microphone() as source:
    while True:
        print("Waiting: ")
        ser=serial.Serial('/dev/ttyACMO', 9600)
        ser.write("8".encode())
        audio=r.listen(source)
        print("done")
        try:
            print("You said:"+ r.recognize_google(audio))
            if r.recognize_google(audio)==("forward"):
                print("okay")
                ser=serial.Serial('/dev/ttyACMO',9600)
                ser.write("7".encode())

            if r.recognize_google(audio)==("backward"):
                print("okay")
                ser=serial.Serial('/dev/ttyACMO',9600)
                ser.write("6".encode())

            if r.recognize_google(audio)==("left"):
                print("okay")
                ser=serial.Serial('/dev/ttyACMO',9600)
                ser.write("5".encode())

            if r.recognize_google(audio)==("right"):
                print("okay")
                ser=serial.Serial('/dev/ttyACMO',9600)
                ser.write("4".encode())

            if r.recognize_google(audio)==("stop"):
                print("okay")
                ser=serial.Serial('/dev/ttyACMO',9600)
                ser.write("3".encode())

            else:
                ser=serial.Serial('/dev/ttyACMO',9600)
                ser.write("2".encode())