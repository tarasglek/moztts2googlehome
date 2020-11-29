FROM synesthesiam/mozillatts
RUN /app/bin/python3 -m pip install PyChromecast==7.5.1
ADD chromecast.py tts.py /app/

EXPOSE 5002

ENTRYPOINT ["/app/bin/python3", "/app/tts.py"]