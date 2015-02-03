Map locations of denied host IPs using geoip lookups and OpenLayers 3.

This product includes GeoLite2 data created by MaxMind, available from [http://www.maxmind.com](http://www.maxmind.com).

##Setup
Rename and edit config file

	mv config_SAMPLE.py config.py
	vim config.py

Create and activate a virtualenv

	virtualenv venv
	source venv/bin/activate

Install dependencies via pip

	pip install -r requirements.txt

Run it!

	python map-deny.py
