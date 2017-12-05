# django-pack     

django-pack facilate the uses of bootstrap and other frontend lib using tags
# Installing
``` 
  git pip install git+https://github.com/medamines1/django-pack/
```

## How to use
after Installing 
 add this code to your app.settings.py
```
import ipack
IPACK= os.path.join(STATICFILES_DIRS[0],"codes")
```
then open urls.py and add 
```
from ipack import tags
urlpatterns = [
.
.
.
  ]
tags.boot()
```
the just use it template.html and make sure to run collectstatic
```

{% load ipack %}

{% load %} 
```
becarfull this will include all the .css and .js of the exisiting libs <br>
when using ``` {% load %} ```
make sure to specific package and third argument is the type of file (js,css)
```
existing  so far:
      {'bts':'/bootstrap',
	      'jq':'/jquery',
		   'swe':'/sweetAlert'}
```
if you like to add folder wich contient files you like access the same way just need to create file in ```../codes/```
then run collectstatic and you can use from the tag
if you want to avoid calling ```collectstatic``` just these lines 
``` 
  from django.core.management import call_command

  call_command('collectstatic', verbosity=0, interactive=False)
```
## License : MIT


Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
