
from django.utils.translation import ugettext_lazy as _

from django.apps import AppConfig

from .widget import *

default_app_config = 'leonardo_module_vis_temporal.Config'


class Default(object):

    optgroup = 'Temporal visualizations'

    js_files = [
        'vis/js/analogclock.js',
        'vis/js/digitalclock.js',
        'vis/js/polarclock.js',
    ]

    scss_files = [
        'vis/scss/analogclock.scss',
        'vis/scss/polarclock.scss'
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
