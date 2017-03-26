# coding=utf-8

"""
DCRM - Darwin Cydia Repository Manager
Copyright (C) 2017  WU Zheng <i.82@me.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import time

from django import template
from preferences import preferences
from django.contrib.sites.models import Site
register = template.Library()


@register.simple_tag(takes_context=True)
def global_settings(context):
    context['settings'] = preferences.Setting
    context['site'] = Site.objects.get(id=1)
    context['this_year'] = time.strftime('%Y',time.localtime(time.time()))
    return ''
