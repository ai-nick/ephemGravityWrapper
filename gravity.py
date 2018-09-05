#!/usr/bin/env python2
"""
Created on Tue Apr 25 14:32:42 2017

@author: nickwilliams
"""


import ephem
from math import pow

coredist = {'jupiter':(6.98*pow(10,7)),'moon':(1.71*pow(10,6)),
            'saturn': (120.984*pow(10,6))/2, 'mercury': (48.79*pow(10,5))/2,
            'mars': (6.792*pow(10,6))/2, 'venus': (12.104*pow(10,6))/2,
            'uranus': (51.18*pow(10,6))/2, 'neptune': 24.764*pow(10,6)}

planets = {'mars':ephem.Mars(), 'mercury':ephem.Mercury(), 'saturn':ephem.Saturn(), 'jupiter':ephem.Jupiter(),
               'neptune':ephem.Neptune(), 'uranus':ephem.Uranus(), 'venus':ephem.Venus(), 
               'moon':ephem.Moon(), 'sun':ephem.Sun()}



massdict = {'earth': (5.98*pow(10,24)), 'moon':(7.34*pow(10,22)), 'jupiter':(1.901*pow(10,27)),
                'saturn': (568*pow(10,24)), 'neptune': 102*pow(10,24), 'uranus':86.2*pow(10,24),
                'venus': (4.87*pow(10,24)), 'mars': 0.642*pow(10,24), 'mercury': 0.33*pow(10,24)}


g = 6.673 * pow(10,-11)


def planet_dist(date, planet):   
    p = planets[planet]
    p.compute(date) 
    return p.earth_distance

def dist_to_earth(dist, planet):
    return (dist + coredist[planet]+(6.38*pow(10,6)))                               #Third value is dist to earths center

def pull(date, planet):
    if planet in planets.keys:
        coredist = dist_to_earth(planet_dist(date,planet),planet)
        pull = ((g*massdict['earth']*massdict[planet])/pow(coredist,2))
        return pull
    else:
        print('error invalid planet senpai')