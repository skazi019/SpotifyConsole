from django import template
from django.template.defaultfilters import register

import datetime

register = template.Library()

def human_format(num):
    num = float('{:.3g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])

@register.filter(name='ms_to_m_s')
def ms_to_m_s(value):
	# if len(value) < 1:
	# 	return value
	# print(f"Type of value {value} in Custom Filter is: {type(value)}")
	sec = (value/1000)
	minutes = int((sec/60))
	return "{0}:{1}".format(minutes, str(sec)[:2])

@register.filter(name='follower_readable')
def follower_readable(value):
	return human_format(value)

@register.filter(name='get_release_year')
def get_release_year(value):
	return value.split("-")[0]

@register.filter(name='get_total_duration')
def get_total_duration(data):
	total_time = 0
	for track in data['tracks']['items']:
		total_time += track['duration_ms']
	sec = int(total_time/1000)
	minutes = int(sec/60)
	return f"{minutes} min {int(sec/60)} sec"

@register.filter(name='get_album_release_date')
def get_album_release_date(value):
	release_date = datetime.datetime.strptime(value, '%Y-%m-%d').strftime('%B %d, %Y')
	return release_date