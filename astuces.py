How can we create a varible called 'firstname' directly in a template?
	{% with firstname = "Tobias" %}
	<h1>Hello {{ firstname }}, how are you?</h1>

#------------ Filter -------------
home.html
	<a href="{% url 'home' %}?q={{topic.name}}"
url.py
    path('',views.home, name='home')
	
view.py
def home(request):
	q = request.GET.get('q') if request.GET.get('q') != None else ''
	room = Room.objects.filter(
				   Q(topic__name__icontains=q) |
	                           Q(name__icontains=q) |
				   Q(description__icontains=q)
				   )
--------------------------------------------------------------------------


fname = Member.objects.filter(firstname='Tobias').values()
mydata = Member.objects.filter(lastname='Refsnes', id=2).values()

mydata = Member.objects.filter(firstname__contains='bias').values()
mydata = Member.objects.filter(lastname__icontains='ref').values()

Fnames = Member.objects.filter(firstname__startswith='L').values()
fnames = Member.objects.filter(firstname__istartswith='L').values()

mydata = Member.objects.filter(firstname__endswith='s').values()
mydata = Member.objects.filter(firstname__iendswith='s').values()

mydata = Member.objects.filter(firstname__exact='Emil').values()
mydata = Member.objects.filter(firstname__iexact='emil').values()

mydata = Member.objects.filter(id__gt=3).values() # gt: greater than 3 (id>3) # id__lt=3,  id__lte=3 : Less than 3 , Less than or equal to 3
mydata = Member.objects.filter(id__gte=3).values() # gte: greater or equal to 3 (id>=3)

Return records where firstname is either "Emil" or Tobias":
	mydata = Member.objects.filter(firstname='Emil').values() | Member.objects.filter(firstname='Tobias').values()

#---------- Exp----------------------------------------------\\

from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q

def testing(request):
  mydata = Member.objects.filter(Q(firstname='Emil') | Q(firstname='Tobias')).values()

  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request)) 

//------------- A list of all field look up keywords: --------------\\

date		Matches a date
day		Matches a date (day of month, 1-31) (for dates)
minute		Matches a minute (for datetimes)
month		Matches a month (for dates)
hour		Matches an hour (for datetimes)
second		Matches a second (for datetimes)
time		Matches a time (for datetimes)
week		Matches a week number (1-53) (for dates)
week_day	Matches a day of week (1-7) 1 is sunday
iso_week_day	Matches a ISO 8601 day of week (1-7) 1 is monday
year		Matches a year (for dates)
iso_year	Matches an ISO 8601 year (for dates)

isnull		Matches NULL values

quarter		Matches a quarter of the year (1-4) (for dates)
range		Match between
regex		Matches a regular expression
iregex		Same as regex, but case-insensitive

#--------------- Order By -------------------------\\

mydata = Member.objects.all().order_by('firstname').values()
mydata = Member.objects.all().order_by('-firstname').values()
mydata = Member.objects.all().order_by('lastname', '-id').values()

//--------------- End Order By -------------------------\\

#-------------------------
In the settings.py file, how can you turn of debugging?

	# SECURITY WARNING: don't run with debug turned on in production!
	DEBUG = False
	ALLOWED_HOSTS = []

In the settings.py file, how can you allow your project to be hosted on ANY domain name?

	# SECURITY WARNING: don't run with debug turned on in production!
	DEBUG = False
	ALLOWED_HOSTS = ['*']


When collecting static static files for your project, you have to specify where to collect them to, this is done in the settings.py file, what is the name of the property?

	STATIC_ROOT = BASE_DIR / 'productionfiles'
	STATIC_URL = 'static/'

When collecting static static files for your project, you have to run a specific command, insert the correct command:
	py manage.py collectstatic

//--------------- Start Static Files -------------------------\\
pip install whitenoise
- Modify Settings
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',
].
DEBUG = False

- You can call the folder whatever you like, we will call it productionfiles:
py manage.py collectstatic

STATIC_ROOT = BASE_DIR / 'productionfiles'

STATIC_URL = 'static/'

.
.
//--------------- End Static Files -------------------------\\
//--------------- Start Slug -------------------------\\
in  models.py +
 	slug = models.SlugField(default="", null=False)
in admin.py

	class MemberAdmin(admin.ModelAdmin):
  		list_display = ("firstname", "lastname", "joined_date",)
  		prepopulated_fields = {"slug": ("firstname", "lastname")}
  
	admin.site.register(Member, MemberAdmin)

	
//--------------- End Slug -------------------------\\

//--------------- Start Bootstrap 5 v5 --------------\\

pip install django-bootstrap-v5

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'members',
    'bootstrap5',
]

<!DOCTYPE html>
<html>
<head>
  <title>{% block title %}{% endblock %}</title>

  {% load bootstrap5 %}
  {% bootstrap_css %}
  {% bootstrap_javascript %}

</head>
<body>

	{% for p in prices %}
  		<h1>The price is {{ p|add:"10" }} dollars.</h1>
	{% endfor %}

	{% for x in fruits %}
  		<h1>{{ x|add:"-CHECK" }}</h1> #==> Apple--CHECK , Banana-CHECK,...
	{% endfor %}

	{% filter upper %}
  		<p>Have a great day!</p>  # ==> HAVE A GREAT DAY!
	{% endfilter %}

        -------------------------------------------------
	{{ fruits|add:vegetables }} # views.py  context = {
   						 'fruits': ['Apple', 'Banana', 'Cherry'],   
    						 'vegetables': ['Asparagus', 'Broccoli', 'Carrot'],
  						  }
        --------------------------------------------------
	# views.py 
		context = {'name': 'Emil Refsnes',}
	<h1>{{ name|cut:"snes" }}</h1> ==> Emil Ref

 	 --------------------------------------------------
	# views.py 
	context = {'colors': ['Red', 'Green', 'Blue', '', 'Yellow']}
	{% for x in colors %}
  		<h1>{{ x|default:"nocolor" }}</h1> ==> Red, Green Blue, nocolor,Yellow
	{% endfor %}

 	--------------------------------------------------
	# views.py 
	 context = {
    		'fruits': ['Apple', 'Banana', 'Cherry', 'Orange']
    		}
	<h1>{{ fruits|join:"#" }}</h1> ==> Apple#Banana#Cherry#Orange
	<h1>{{ fruits|last }}</h1>     ==> Orange

	context = {
    		'firstname': 'Emil',   
    		'lastname': 'Refsnes',   
  		}
	<h1>{{ firstname|last }}</h1> ==> l

	--------------------------------------------------
	# views.py 
	 context = {
   		 'mytext': 'Hello\nmy name is Leo.\n\nI am a student.',   
 		 }

	<h3>Without linebreaks filter:</h3>

		{{ mytext }} ==> Hello my name is Leo. I am a student.

	<h3>With linebreaks filter:</h3>

		{{ mytext|linebreaks }} ==> 	Hello
						my name is Leo.

						I am a student.

	--------------------------------------------------
	# views.py 
	 context = {
    		'cars': [
    		  {'brand': 'Ford', 'model': 'Mustang', 'year': 1964},
    		]
  		}
	{{ cars|json_script:"mycars" }}
	--------------------------------------------------
	# views.py 
	 context = {
   		 'x': 'Volvo',
    		'y': 'Ford',
    		'z': 'BMW',
    		}
	<h1>{% firstof x y z %}</h1> ==> Volvo

	--------------------------------------------------
	# views.py 
	context = {
    		'mylist': [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 5]
    		}
	<ul>
  		{% for x in mylist %}         * 1
    		    {% ifchanged %}	      * 2
      			<li>{{ x }}</li>      * 3
    		    {% endifchanged %}        * 4
  		{% endfor %}                  * 5
</ul>



</body>
</html>

//--------------- End Bootstrap 5 v5 --------------\\

