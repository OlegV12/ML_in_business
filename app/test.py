import urllib.request
import json


def get_prediction(zip_code, area, room, lon, lat):
    body = {'Zip': zip_code,
            'Area': area,
            'Room': room,
            'Lon': lon,
            'Lat': lat}

    myurl = "http://0.0.0.0:8180/predict"
    req = urllib.request.Request(myurl)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')  # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    print(jsondataasbytes)
    response = urllib.request.urlopen(req, jsondataasbytes)
    return json.loads(response.read())


get_prediction(1102, 120, 5, 4.956167, 52.317822)
