import gmaps2geojson

# # Uncomment below to query each direction set one by one:
# writer = gmaps2geojson.Writer()
# writer.query("2131 7th Ave, Seattle, WA 98121", "900 Poplar Pl S, Seattle, WA 98144")
# writer.query("900 Poplar Pl S, Seattle, WA 98144", "219 Broadway E, Seattle, WA 98102")
# writer.save("example.geojson")

# Query array of locations:
writer = gmaps2geojson.Writer()
directions = writer.query_array([["San Carlos, Antioquia, Colombia", "Villavicencio, Colombia"],["Villavicencio, Colombia","Cali, Colombia"],["Cali, Colombia","Quito, Ecuador"] ])
writer.save("example.geojson")