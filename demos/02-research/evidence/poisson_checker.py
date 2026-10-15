#!/usr/bin/env python3
"""Exact rational counterexample for finite-sensor Poisson state reconstruction.

Independent mathematical fixture. Runs with Python standard library only.
It is NOT a test of a PINN training run or of a user's unpublished manuscript.
"""
from fractions import Fraction as F
import json

ONE = F(1)
HALF = F(1, 2)

def a(t: F) -> F:
    return t * (ONE - t)

def u0(x: F, y: F) -> F:
    return F(30) * a(x) * a(y)

def source(x: F, y: F) -> F:
    """-Delta u0, analytically from a''=-2."""
    return F(60) * (a(x) + a(y))

def harmonic_perturbation(x: F, y: F) -> F:
    return (x - HALF)**2 - (y - HALF)**2

def u1(x: F, y: F) -> F:
    return u0(x, y) + harmonic_perturbation(x, y)

def negative_laplacian_u0(x: F, y: F) -> F:
    return F(60) * (a(x) + a(y))

def negative_laplacian_u1(x: F, y: F) -> F:
    return negative_laplacian_u0(x, y) - (F(2) - F(2))

def run() -> dict:
    sensors = [(F(3,10),F(3,10)), (F(3,10),F(7,10)),
               (F(7,10),F(3,10)), (F(7,10),F(7,10))]
    samples = []
    for x, y in sensors:
        assert F(1,8) < x < F(7,8) and F(1,8) < y < F(7,8)
        assert harmonic_perturbation(x, y) == 0
        assert u0(x, y) == u1(x, y)
        samples.append({'x': str(x), 'y': str(y), 'u0': str(u0(x,y)),
                        'u1': str(u1(x,y)), 'h': str(harmonic_perturbation(x,y))})
    test_points = [(F(1,2),F(1,4)), (F(1,5),F(2,5)), (F(7,10),F(8,10))]
    for x, y in sensors + test_points:
        assert negative_laplacian_u0(x, y) == source(x,y)
        assert negative_laplacian_u1(x, y) == source(x,y)
    xp, yp = F(1,2), F(1,4)
    assert u1(xp, yp)-u0(xp, yp) == -F(1,16)
    xb,yb = F(0),F(1,2)
    assert u1(xb,yb)-u0(xb,yb) == F(1,4)
    return {
      'status': 'PASS', 'meaning': 'verified exact Poisson equation and indistinguishable finite sensors',
      'sensors': samples,
      'off_sensor_point': {'x':str(xp), 'y':str(yp), 'u1_minus_u0':str(u1(xp,yp)-u0(xp,yp))},
      'boundary_point': {'x':str(xb),'y':str(yb),'u1_minus_u0':str(u1(xb,yb)-u0(xb,yb))},
      'note': 'This does not contradict unique continuation from exact data on an open set; full boundary traces would also rule out this specific alternative.'
    }

if __name__ == '__main__':
    print(json.dumps(run(), ensure_ascii=False, indent=2))
