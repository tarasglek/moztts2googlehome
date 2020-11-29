```

docker build -t moztts2googlehome .
docker run -it -p 5002:5002 --net host moztts2googlehome
curl http://localhost:5002/api/chromecast?text=Hello&myip=192.168.1.205&chromecast=Garage%20speaker
python media_example.py --phrase Oh gosh, what time is it? --cast Bathroom speaker --myip 192.168.1.205
```
