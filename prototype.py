#!/usr/bin/env python

import geoip2.database
from geojson import Feature, Point, FeatureCollection

hosts = []

# Returns True for non-blank and non-comment lines
def is_valid_line(line):
	return line and not line.startswith('#')

# Create generator expression for valid lines
with open('hosts.deny') as hosts_file:
	lines = filter(is_valid_line, (line.rstrip() for line in hosts_file))
	count = len(lines)

# Parse each line and make dict containing protocol and ip
for line in lines:
	split_line = line.split()
	protocol = split_line[0].strip(':')
	ip = split_line[1]
	hosts.append({'protocol': protocol, 'ip': ip})

# Create geoip2 database reader
reader = geoip2.database.Reader('db/GeoLite2-City.mmdb')

host_data = []

# Query geoip2 database for each ip
for host in hosts:
	response = reader.city(host['ip'])
	host_data.append(response)

reader.close()

features = []

count = 0

# Creat feature for each ip
for entry in host_data:
	new_feature = Feature(geometry=Point((entry.location.longitude, entry.location.latitude)),
						  id=count)
	features.append(new_feature)
	count += 1

crs = {
    "type": "name",
    "properties": {
        "name": "EPSG:4326"
    }
}

# Create GeoJSON FeatureCollection from features
collection = FeatureCollection(features, crs=crs)

print collection

