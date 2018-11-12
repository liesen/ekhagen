from typing import NamedTuple
import requests


class LatLng(NamedTuple):
    lat: float
    lng: float


class Marker(NamedTuple):
    title: str
    position: LatLng


ekhagen = Marker(title='Ekhagen', position=LatLng(59.37299, 18.05638))

markers = {
    1: Marker(title='Båthamnen', position=LatLng(59.37316,18.05591)),
    2: Marker(title='Klippor för kvällsbad eller grillning', position=LatLng(59.3736,18.0603)),
    3: Marker(title='Stora Lappkärrsberget med vikingagravar', position=LatLng(59.37207, 18.06361)),
    4: Marker(title='Barnbad med sandstrand', position=LatLng(59.37250,18.06925)),
    5: Marker(title='Utomhustennisbana', position=LatLng(59.36746,18.08621)),
    6: Marker(title='Betesplats för kungens får', position=LatLng(59.36410,18.08785)),
    7: Marker(title='Laduviken med Djurgårdens äldsta byggnad', position=LatLng(59.36098,18.07943)),
    8: Marker(title='4H-gården med många djur och året-runt-servering Skafferiet', position=LatLng(59.36559, 18.07105)),
    9: Marker(title='Lappkärret med rikt fågelliv', position=LatLng(59.36868,18.06843)),
    10: Marker(title='Bergianska trädgården', position=LatLng(59.36980, 18.04606)),
    11: Marker(title='"Hemlig" badplats', position=LatLng(59.37100,18.04097)),
    12: Marker(title='Badstrand', position=LatLng(59.36196,18.04873)),
    13: Marker(title='Brunnsviken med plogad skridskobana på vintern och kanotuthyrning sommartid', position=LatLng(59.3691,18.0383)),
}

center = Marker(title='', position=LatLng(59.3630,18.0630))

markers_str = '|'.join(f'{marker.position.lat},{marker.position.lng},lightblue{i}'
                       for i, marker in markers.items())
print(f'http://staticmap.openstreetmap.de/staticmap.php?center={center.position.lat},{center.position.lng}&zoom=14&size=712x712&markers={markers_str}')
