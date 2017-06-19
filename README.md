# geonames-scripts

## geonames-cities-search.py
This Python script takes a JSON containing cities, countries, and regions and looks them up via the [GeoNames Web Services API](http://www.geonames.org/export/web-services.html) and saves the results to a tab-delimited text file.

If coordinates cannot be found for a location, they'll be marked as `NULL`.

### Usage
```Bash
python geonames-cities-search.py
```

### Example Input myLocations.json
```JSON
[
  {
    "City": "Groningen",
    "Country": "The Netherlands",
    "Region": "Europe"
  },
  {
    "City": "Crete",
    "Country": "Greece",
    "Region": "Europe"
  },
  {
    "City": "EARTH (Limon)",
    "Country": "Costa Rica",
    "Region": "North America"
  }
]
```

### Example Output locations-20170619150404.txt
```
Groningen	The+Netherlands	Europe	53.21917	6.56667
Crete	Greece	Europe	35.15585	24.89502
EARTH+(Limon)	Costa+Rica	North+America	NULL	NULL
```

### Why these input/output formats?
JSON is a possible location output format from Terra Dotta Software and a tab-delimited text file is a valid input format.
