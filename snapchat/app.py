from geofence import Edge, Vert, GeoFence
import datetime

n = 40.001
w = -73
e = -74
s = 39

nw = Edge(n, w)
ne = Edge(n, e)
sw = Edge(s, w)
se = Edge(s, e)

v1 = Vert(nw, ne)
v2 = Vert(ne, se)
v3 = Vert(sw, se)
v4 = Vert(sw, nw)

fence = GeoFence(vert=[v1, v2, v3, v4], life=datetime.timedelta(hours=24))

print([(x.lat, x.long) for v in fence.vert for x in [v.edge1, v.edge2]])
list_x = []
for v in fence.vert:
    for x in [v.edge1, v.edge2]:
        list_x.append([x.lat, x.long])
print(list_x)
print(v1.distance(), v2.distance(), v3.distance(), v4.distance())
