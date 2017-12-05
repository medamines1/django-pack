from django import template
from django.utils.safestring import mark_safe
import sys,os,imp,shutil, errno
from django.conf import settings

register = template.Library()

def boot():
	loca =  settings.IPACK
	if not os.path.lexists(loca):
	  try:
		shutil.copytree(imp.find_module('ipack')[1]+'/codes',loca)
	  except Exception as e:
	  	print e 
	  	sys.exit()
	print "[*] ipack :  all files are present"

script = lambda x,y: "<script src=%scodes%s/%s></script>"%(settings.STATIC_URL,y,x)
link   = lambda x,y: """<link rel="stylesheet" type="text/css" href=%scodes%s/%s>"""%(settings.STATIC_URL,y,x)

def _type(elm,st):
	if elm.endswith(".css"):
		return link(elm,st)
	else:
		return script(elm,st)

def _filter(st,key,ref):
	dire=[]
	for i in st:
	  if key in i or key=="all":
	  	dire.append(_type(i,ref))
	return dire

@register.simple_tag
def load(st="bts",key="all"):
	ref=  {'bts':'/bootstrap',
	        'jq':'/jquery',
		   'swe':'/sweetAlert'}
	d = _filter(os.listdir(settings.IPACK+ref[st]),key,ref[st])
	return mark_safe("".join(d))








