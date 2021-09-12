from math import sin, cos, sqrt, atan2
import datetime


class Edge:
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long
        self.cord = (lat, long)


r = 6373


class Vert:
    def __init__(self, edge1, edge2):
        self.edge1 = edge1
        self.edge2 = edge2

    def dist_long(self):
        return self.edge1.long - self.edge2.long

    def dist_lat(self):
        return self.edge1.lat - self.edge2.lat

    def distance(self):
        a = sin(self.dist_lat() / 2) ** 2 + cos(self.edge1.lat) * \
            cos(self.edge2.lat) * sin(self.dist_long() / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        return r * c

    def Update(self, edge1=None, edge2=None):
        if all(not x for x in [edge1, edge2]):
            raise Exception('Must provide at least one edge to update')
        if edge1 and not edge2:
            return Vert(edge1, self.edge2)
        elif edge2 and not edge1:
            return Vert(self.edge1, edge2)
        else:
            return Vert(edge1, edge2)


class GeoFence:
    def __init__(self, vert, life):
        self.vert = vert
        self.life = life
        self.start_time = datetime.datetime.now()

    def exp(self):
        return datetime.datetime.now() - self.lifetime > self.start_time
