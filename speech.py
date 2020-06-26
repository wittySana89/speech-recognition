import speech_recognition as sr
import pyaudio
import serial

r = sr.Recognizer()
r.dynamic_energy_threshold=False