# gmaps2geojson

Super simple python utility for getting GeoJSON from Google Maps routes.

## Setup
Written using Python 3.6. Install requirements with `pip install -r gmaps2geojson/requirements.txt`.

Get an API key for the [Google Maps Directions API](https://developers.google.com/maps/documentation/directions/start). Set this as an environment variable.
```
export GMAPS_KEY='YOUR API KEY HERE'
```

## Usage
```
>>> import gmaps2geojson
>>> writer = gmaps2geojson.Writer()
>>> directions1 = writer.query("2131 7th Ave, Seattle, WA 98121", "900 Poplar Pl S, Seattle, WA 98144")
>>> directions2 = writer.query("900 Poplar Pl S, Seattle, WA 98144", "219 Broadway E, Seattle, WA 98102")
>>> directions2
*Will output all [long,lat] coordinates of geojson line
>>> writer.save("example.geojson")
```
or
```
>>> import gmaps2geojson
>>> writer = gmaps2geojson.Writer()
>>> directions = writer.query_array([
      ["2131 7th Ave, Seattle, WA 98121", "900 Poplar Pl S, Seattle, WA 98144"],
      ["900 Poplar Pl S, Seattle, WA 98144", "219 Broadway E, Seattle, WA 98102"]
    ])
>>> directions
*Will output all [long,lat] coordinates of geojson line
>>> writer.save("example.geojson")
```

* `query(src, dest, custom_label=None)`: Use the query function to get a list of coordinates -- derived from the first result on Google Maps between the provided source and destination. Returns list of (longitude, latitude) coordinates
* `query_array(src_dest_array, custom_label=None)`: Same as the `query` function, only this accepts an array of [src, dest] string locations. Returns a list of (longitude, latitude) coordinates connecting each location. Passing an array of `[["San Carlos, Antioquia, Colombia", "Villavicencio, Colombia"],["Villavicencio, Colombia","Cali, Colombia"]]` will calculate the coordinates connecting San Carlos to Villavicencio to Cali. Write those coordinates to a file using...
* `write(filename)`: Outputs geojson of all queried routes. All routes have a `name` property in the format of `<src> to <dest>` unless a custom_label was specified when querying.

See `example.py` and `example.geojson`.
