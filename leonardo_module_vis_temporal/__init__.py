
import logging

from django.apps import AppConfig

LOG = logging.getLogger(__name__)

from .widget import *

default_app_config = 'leonardo_module_vis_temporal.Config'


class Default(object):

    optgroup = 'Temporal visualizations'

    js_files = [
        'vis/js/analogclock.js',
        'vis/js/digitalclock.js',
        'vis/js/polarclock.js',
    ]

    apps = [
        'leonardo_module_vis_temporal',
    ]

    widgets = [
        AnalogClockWidget,
        DigitalClockWidget,
        PolarClockWidget,
    ]


class Config(AppConfig, Default):

    name = 'leonardo_module_vis_temporal'
    verbose_name = _("Temporal Visualization Module")


default = Default()
