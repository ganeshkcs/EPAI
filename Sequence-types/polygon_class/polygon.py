# polygon.py

import math

_polygons = {'Triangle': (3, 60),
             'Quadrilateral': (4, 90),
             'Pentagon': (5, 108),
             'Hexagon': (6, 120),
             'Heptagon': (7, 128.57),
             'Octagon': (8, 135),
             'Nonagon': (9, 140),
             'Decagon': (10, 144),
             'Hendecagon': (11, 147.3),
             'Dodecagon': (12, 150),
             'Triskaidecagon': (13, 152.308),
             'Tetrakaidecagon': (14, 154.286),
             'Pentadecagon': (15, 156),
             'Hexakaidecagon': (16, 157.5),
             'Heptadecagon': (17, 158.824),
             'Octakaidecagon': (18, 160),
             'Enneadecagon': (19, 161.053),
             'Icosagon': (20, 162)}


class Polygon:
    """
    Polygon:- Custom Polygon Class with numerous properties including interior angle, apothem, area etc.
    """

    def __init__(self, edges: int, vertices: int, circum_radius: int):
        """
        Args:
            edges: Number of Edges
            vertices: Number of Vertices
            circum_radius: C.Radius of Polygon
        """
        self._edges = edges
        self._vertices = vertices
        self._circum_radius = circum_radius

    @property
    def name(self):
        sides = self._edges
        for key in _polygons.keys():
            try:
                if _polygons[key][0] == sides:
                    return key
            except:
                return str(sides) + '-gon'

    @property
    def edges(self):
        return self._edges

    @property
    def vertices(self):
        return self._vertices

    @property
    def interior_angle(self):
        return (self._edges - 2) * 180 / self._edges

    @property
    def edge_length(self):
        return abs(2 * self._circum_radius * math.sin(180 / self._edges))

    @property
    def apothem(self):
        return self._circum_radius * math.cos(180 / self._edges)

    @property
    def area(self):
        return self._edges * 2 * self._circum_radius * math.sin(180 / self._edges) * self._circum_radius * math.cos(
            180 / self._edges) * 0.5

    @property
    def perimeter(self):
        return self._edges * 2 * self._circum_radius * math.sin(180 / self._edges)

    def __repr__(self):
        rep_dict = {'Name': self.name, 'Sides': self.edges, 'Vertices': self.vertices,
                    'Interior Angle': self.interior_angle, 'Edge Length': self.edge_length,
                    'Apothem': self.apothem, 'Area': self.area}
        return str(rep_dict)

    def __eq__(self, other: 'Polygon'):
        return self._vertices == other._vertices & self._circum_radius == other._circum_radius

    def __gt__(self, other: 'Polygon'):
        return self._vertices > other._vertices
