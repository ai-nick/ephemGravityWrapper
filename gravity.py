#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 14:32:42 2017

@author: nickwilliams
"""
import ephem


def planet_dist(date, planet):
    planets = {'mars':ephem.Mars(date), 'mercury':ephem.Mercury(date), 'saturn':ephem.Saturn(date), 'jupiter':ephem.Jupiter(date),
               'neptune':ephem.Neptune(date), 'uranus':ephem.Uranus(date), 'venus':ephem.Venus(date), 
               'moon':ephem.Moon(date), 'sun':ephem.Sun(date)}
    p = planets[planet]
    p.compute() 
    return p.earth_distance

def dist_to_earth(dist, planet):
    coredist = {'jupiter':(6.98*pow(10,7)),'moon':(1.71*pow(10,6)),
                'saturn': (120.984*pow(10,6))/2, 'mercury': (48.79*pow(10,5))/2,
                'mars': (6.792*pow(10,6))/2, 'venus': (12.104*pow(10,6))/2,
                'uranus': (51.18*pow(10,6))/2, 'neptune': 24.764*pow(10,6)}
    return (dist + coredist[planet]+(6.38*pow(10,6)))                               #Third value is dist to earths center

def pull(date, planet):
    coredist = dist_to_earth(planet_dist(date,planet),planet)
    massdict = {'earth': (5.98*pow(10,24)), 'moon':(7.34*pow(10,22)), 'jupiter':(1.901*pow(10,27)),
                'saturn': (568*pow(10,24)), 'neptune': 102*pow(10,24), 'uranus':86.2*pow(10,24),
                'venus': (4.87*pow(10,24)), 'mars': 0.642*pow(10,24), 'mercury': 0.33*pow(10,24)}
    g = 6.673 * pow(10,-11)
    pull = ((g*massdict['earth']*massdict[planet])/pow(coredist,2))
    return pull