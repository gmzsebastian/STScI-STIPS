from __future__ import absolute_import,division
__filetype__ = "base"

#Local Modules
from .instrument import Instrument

class WfirstInstrument(Instrument):
    """
    The JwstInstrument class contains the necessary constants and modifications specific to JWST
        but independent of any specific instrument. This class is also not intended to be 
        implemented directly, but rather through its children (e.g. NirCamShort, Miri, NirCamLong).
        It contains the following constants and the following new variables:
        
        detectors : array of detectors, each an AstroImage, and each with its own RA/DEC
        filter    : string, what filter of the instrument is being observed
    """

    def __init__(self, **kwargs):
        """
        Still only a base class. Init is super init.
        """
        super(WfirstInstrument,self).__init__(**kwargs)
        self.REFS = {   'comptable': self.COMPFILES[-2],
                        'graphtable': self.GRAPHFILES[-2],
                        'thermtable': self.THERMFILES[-2],
                        'area': 45238.93416,
                        'waveset': (500,26000,10000.,'log')
                    }
    
    TELESCOPE = 'WFIRST'
    AREA = 45238.93416
    DBNAME = "IsochroneGrid.db"
    MODE = 'imaging'
    APERTURE = 'any'