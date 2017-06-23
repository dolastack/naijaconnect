import urllib, json

get_weather_info():
    get_lagos_weather = urllib.request.Request("https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22Lagos%2C%20Ng%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys")
    dt = urllib.request.urlopen(get_lagos_weather)
    raw_data = dt.read()
    json_data = json.loads(raw_data.decode())
