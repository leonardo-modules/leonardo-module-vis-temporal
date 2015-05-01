import datetime
import pytz
from django.db import models
from django.utils.translation import ugettext_lazy as _
from leonardo.module.web.models import Widget

class PolarClockWidget(Widget):
    """
    Widget which shows polar clock.
    """
    time_zone = models.CharField(max_length=127, verbose_name=_('time zone'),choices=[(x, x) for x in pytz.common_timezones], default='Europe/Prague')
    show_day_only = models.BooleanField(verbose_name=_('show day only?'), default=False)


    def widget_data(self, request):
        data = {
            'global_time': datetime.datetime.now().isoformat(),
            'local_time': datetime.datetime.now().isoformat(),
            'time_zone': self.time_zone
        }
        return data

    class Meta:
        abstract = True
        verbose_name = _("Polar clock")
        verbose_name_plural = _("Polar clocks")
