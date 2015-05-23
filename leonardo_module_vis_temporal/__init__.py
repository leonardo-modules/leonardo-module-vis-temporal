
import logging

from django.apps import AppConfig

LOG = logging.getLogger(__name__)

from .widget import *

default_app_config = 'leonardo_module_vis_temporal.NavConfig'


class Default(object):

    optgroup = ('Temporal visualizations')

    js_files = [
        'vis/js/analogclock.js'
        'vis/js/digitalclock.js'
        'vis/js/polarclock.js'
    ]

    @property
    def apps(self):

        return [

            'leonardo_module_vis_temporal',

        ]

    @property
    def widgets(self):
        return [
            AnalogClockWidget,
            DigitalClockWidget,
            PolarClockWidget,
        ]

class NavConfig(AppConfig, Default):

    name = 'leonardo_module_vis_temporal'
    verbose_name = "Temporal Visualization Module"


default = Default()
