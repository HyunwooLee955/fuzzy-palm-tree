# contents of refraction.py
import numpy as np


def snell(theta_inc: float, n1: float, n2: float) -> float:
    """
    Compute the refraction angle using Snell's Law.

    See https://en.wikipedia.org/wiki/Snell%27s_law
    
    Parameters
    ----------
    theta_inc : float
        Incident angle in radians.
    n1 : float
        Refractive index of the incident medium.
    n2 : float
        Refractive index of the transmitted medium.
    
    Returns
    -------
    theta : float
        Refraction angle in radians.
    
    Examples
    --------
    A ray enters an air--water boundary at pi/4 radians (45 degrees).

    >>> snell(np.pi/4, 1.00, 1.33)
    0.5605584137424605
    """
    return np.arcsin(n1 / n2 * np.sin(theta_inc))