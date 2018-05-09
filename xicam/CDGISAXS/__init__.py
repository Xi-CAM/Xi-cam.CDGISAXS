from xicam.plugins import GUIPlugin, GUILayout
from xicam.plugins import manager as pluginmanager

from qtpy.QtWidgets import *


class CDGISAXSPlugin(GUIPlugin):
    name = 'CDGISAXS'

    def __init__(self):


        # Setup layout
        self.stages = {'Terminal': GUILayout(QWidget())}


        super(CDGISAXSPlugin, self).__init__()

    