# Pomodoro Blog Testing

## Functional Testing

## Display Posts by Topic

| Use Case # | As Persona | Want to | Expected Results | Pass/Fail |
| --- | --- | --- | ---| --- |
| | As a user | I want to click on blog post view the detail | Click on post renders post detail page | Pass |
| | As a user | I want to display blog post by topic | Render published post by topic | Pass |
| | As a non authenticated user | I want to display blog post excerpt by topic | Render published post excerpt by topic | Pass |
| | As an authenticated user | I want to display blog post by topic | Render post by topic  includes posts in published and draft status with delete and update buttons| Pass |

## Post Detail Page
| Use Case # | As Persona | Want to | Expected Results | Pass/Fail |
| --- | --- | --- | ---| --- |
| | As a user | I want to view the post detail | The post Title and content is rendered | Pass |
| --- | --- | --- | ---| --- |
| | As a user | I want to click on button to return to post page | Click on Return to Posts button renders blog post page | Pass |

## Automated Unit Testing

## Testing views

```
from django.test import TestCase
​
# Create your tests here.
class TestViews(TestCase):
    def test_home_page(self):
        """ Test home page renders correct page """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self. assertTemplateUsed(response, 'home/index.html')
```

```
check redirects the same way, only you'll be looking for a 302 status code to say you've been directed away from the original route
```

## Coverage

- pip install coverage
- coverage run --source=profiles  manage.py test
- coverage report

## Validate Modified Allauth templates

- accounts/signup/
- accounts/login/
- accounts/logout/
- accounts/password/change/
- accounts/password/set/
- accounts/inactive/
- accounts/email/
- accounts/confirm-email/
- accounts/^confirm-email/(?P<key>[-:\w]+)/$ 
- accounts/password/reset/
- accounts/password/reset/done/
- accounts/^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$ 
- accounts/password/reset/key/done/
- accounts/social/

## Home

### test_home_page

python manage.py test home.test_views

- TDD fail test

```
(venv) C:\Users\user\Downloads\MS4PomodoroBlogChat\django-blogchat-tech>python manage.py test home.test_views
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
E
======================================================================
ERROR: test_home_page (home.test_views.TestViews)
Test home page renders correct page
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\user\Downloads\MS4PomodoroBlogChat\django-blogchat-tech\home\test_views.py", line 7, in test_home_page
    response = self.client.get('/')
  File "C:\Users\user\Downloads\MS4PomodoroBlogChat\django-blogchat-tech\venv\lib\site-packages\django\test\client.py", line 742, in get
    response = super().get(path, data=data, secure=secure, **extra)
  File "C:\Users\user\Downloads\MS4PomodoroBlogChat\django-blogchat-tech\venv\lib\site-packages\django\test\client.py", line 396, in get
    return self.generic('GET', path, secure=secure, **{
  File "C:\Users\user\Downloads\MS4PomodoroBlogChat\django-blogchat-tech\venv\lib\site-packages\django\test\client.py", line 473, in generic
    return self.request(**r)
  File "C:\Users\user\Downloads\MS4PomodoroBlogChat\django-blogchat-tech\venv\lib\site-packages\django\test\client.py", line 719, in request
    self.check_exception(response)
  File "C:\Users\user\Downloads\MS4PomodoroBlogChat\django-blogchat-tech\venv\lib\site-packages\django\test\client.py", line 580, in check_exception
    raise exc_value
  File "C:\Users\user\Downloads\MS4PomodoroBlogChat\django-blogchat-tech\venv\lib\site-packages\django\core\handlers\exception.py", 
line 47, in inner
    response = get_response(request)
  File "C:\Users\user\Downloads\MS4PomodoroBlogChat\django-blogchat-tech\venv\lib\site-packages\django\core\handlers\base.py", line 
181, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\user\Downloads\MS4PomodoroBlogChat\django-blogchat-tech\home\views.py", line 7, in index
    return render(request, "home/index1.html")
  File "C:\Users\user\Downloads\MS4PomodoroBlogChat\django-blogchat-tech\venv\lib\site-packages\django\shortcuts.py", line 19, in render
    content = loader.render_to_string(template_name, context, request, using=using)
  File "C:\Users\user\Downloads\MS4PomodoroBlogChat\django-blogchat-tech\venv\lib\site-packages\django\template\loader.py", line 61, in render_to_string
    template = get_template(template_name, using=using)
  File "C:\Users\user\Downloads\MS4PomodoroBlogChat\django-blogchat-tech\venv\lib\site-packages\django\template\loader.py", line 19, in get_template
    raise TemplateDoesNotExist(template_name, chain=chain)
django.template.exceptions.TemplateDoesNotExist: home/index1.html

----------------------------------------------------------------------
Ran 1 test in 1.259s

FAILED (errors=1)
Destroying test database for alias 'default'...
```

- Pass test

```
(venv) C:\Users\user\Downloads\MS4PomodoroBlogChat\django-blogchat-tech>python manage.py test home.test_views
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.
----------------------------------------------------------------------
Ran 1 test in 0.041s

OK
Destroying test database for alias 'default'...
```

### Test_donate_page

- TDD Create fail test donate page

  python manage.py test donate/

```
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
F
======================================================================
FAIL: test_fail_donate_page (donate.test_views.TestViews)
Test donate page renders when user click on donate button
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\user\Downloads\MS4PomodoroBlogChat\django-blogchat-tech\donate\test_views.py", line 8, in test_fail_donate_page
    self.assertEqual(response.status_code, 302)
AssertionError: 200 != 302

----------------------------------------------------------------------
Ran 1 test in 0.033s

FAILED (failures=1)
Destroying test database for alias 'default'...
```

- Add Render Donate Page

  python manage.py test donate/

```
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.F
======================================================================
FAIL: test_fail_donate_page (donate.test_views.TestViews)
Test donate page renders when user click on donate button
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\user\Downloads\MS4PomodoroBlogChat\django-blogchat-tech\donate\test_views.py", line 8, in test_fail_donate_page
    self.assertEqual(response.status_code, 302)
AssertionError: 200 != 302

----------------------------------------------------------------------
Ran 2 tests in 0.038s

FAILED (failures=1)
Destroying test database for alias 'default'...
```

- Modify test_donate_page(self):
  render donate/donate.html

- Add def test_successMsg(self):
 render donate/success.html', {'amount':amount}

- __TO BE ADDED__ Add def charge
redirect donate/success/5/

- python manage.py test donate.test_views

```
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.F.
======================================================================
FAIL: test_fail_donate_page (donate.test_views.TestViews)
TDD Fail Render Donate Page
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\user\Downloads\MS4PomodoroBlogChat\django-blogchat-tech\donate\test_views.py", line 8, in test_fail_donate_page
    self.assertEqual(response.status_code, 302)
AssertionError: 200 != 302

----------------------------------------------------------------------
Ran 3 tests in 0.067s

FAILED (failures=1)
Destroying test database for alias 'default'...
```
## Email

- Create new account using Temp Email


## Donation

### Stripe Payment

- Validate Form input values and Stripe Payment Token

  - Form Input values matches values terminal output
  - Add Customer
  - Payment Transacted

  ![](docs\testing\stripePyamentUnitTest.png)

  ![](docs\testing\stripePyamentUnitTestOutput.png)

- STRIPE Customer Created

- STRIPE Payment Created


- Navbar Donate Button renders Donate Page
- Redirect to Success Page
- Redirect to Error Page
- Cancel redirect to Donate Page

### Donation Captured

- Donation transaction captured for display in the database
- Displays in Admin
- Displays on Donation List Page accessible only to Admin
- Display message when no donations
- Execute donation model and views tests


## Bugs

### Deployment to Heroku with Whitenoise to serve static files does not recognize css files

- Error: Console error during deployment to Heroku unable to access css static files

```
Refused to apply style from 'https://django-blogchat-tech.herokuapp.com/static/css/base.css' because its MIME type ('text/html') is not a supported stylesheet MIME type, and strict MIME checking is enabled.
```
- Root Cause: Static file not copied during deployment to Heroku
- Resolution: Install, configure Whitenoise and deploy to heroku

  Solution: After 3 days of AGONY
Resolution:
  - DISABLE_COLLECTSTATIC = 1 needs to be removed from heroku dashboard for static files to be copied and then replaced it after (probably need to do this when deploying to heroku each time)
  ![](docs\testing\staticfilesNotFound.png)
  - Updated settings following instructions found on https://devcenter.heroku.com/articles/django-assets.
Created statisfiles folder with an empty staticfiles.txt

  ```
  STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
  # Extra places for collectstatic to find static files.    STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
  ```

  - Included mimetypes in settings and type="test/css" in html
added to urls.py

  ```
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  ```

- References: 

  - [Django staticfiles not found on Heroku (with whitenoise)](https://stackoverflow.com/questions/35507140/django-staticfiles-not-found-on-heroku-with-whitenoise)

  - [Django and Static Assets](https://devcenter.heroku.com/articles/django-assets)
  [Using WhiteNoise with Django](http://whitenoise.evans.io/en/stable/django.html)

  - [Understanding static files in Django + Heroku](https://vonkunesnewton.medium.com/understanding-static-files-in-django-heroku-1b8d2f003977)

  - [Static vs. Media files in Django](https://browniebroke.com/blog/static-vs-media-in-django/)

  - [Heroku static files not loading, Django](https://stackoverflow.com/questions/28961177/heroku-static-files-not-loading-django)

  - [CSS not loading wrong MIME type Django](https://stackoverflow.com/questions/35557129/css-not-loading-wrong-mime-type-django)

  - [Static Files on Heroku with Django and Whitenoise | Hiit Startup | Django Tutorial](https://www.youtube.com/watch?v=TgmeAN32Uvw)

  - [Serve Static Files with Whitenoise](https://www.youtube.com/watch?v=qSrJt3UD9xk)
  - [Managing static files (e.g. images, JavaScript, CSS)](https://docs.djangoproject.com/en/3.2/howto/static-files/)
  - [Django Static Files Settings](https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-STATICFILES_FINDERS)

  ### STRIPE Form input field values not displaying in terminal output

- Error: Only Stripe variables values are displaying in output

  ```
  [05/Jul/2021 06:07:43] "POST /donate/charge/ HTTP/1.1" 302 0
  [05/Jul/2021 06:07:43] "GET /donate/success/5/ HTTP/1.1" 200 3954
  C:\Users\user\Downloads\MS4PomodoroBlogChat\django-blogchat-tech\donate\views.py changed, reloading.
  Watching for file changes with StatReloader
  Performing system checks...

  System check identified no issues (0 silenced).
  July 05, 2021 - 06:08:02
  Django version 3.2.4, using settings 'django_blogchat_tech.settings'
  Starting development server at http://127.0.0.1:8000/
  Quit the server with CTRL-BREAK.
  [05/Jul/2021 06:08:05] "GET / HTTP/1.1" 200 5514
  [05/Jul/2021 06:08:11] "GET /donate/ HTTP/1.1" 200 5089
  Data: <QueryDict: {'csrfmiddlewaretoken': ['Hf0aFlNvrhtAmOdttDv0IRlgZ1P6RME5HBSXIDx4bHLPR4zDdasd6vIzrX5EIYtN'], 'stripeToken': ['tok_1J9oj3IpOT7SMB9HH9kY1rwS']}>
  Email: None
  [05/Jul/2021 06:08:29] "POST /donate/charge/ HTTP/1.1" 302 0
  [05/Jul/2021 06:08:29] "GET /donate/success/5/ HTTP/1.1" 200 3954
  ```

- Root Cause: Input did not include name attribute
  ```
  <input required type="text" id = "nickname"  placeholder="Your Name">
  ```
  

- Fix include input element name attribute
  ```
  <input required type="text" id = "nickname" name = "nickname" placeholder="Your Name">
  ```
  
  ```
  Starting development server at http://127.0.0.1:8000/
  Quit the server with CTRL-BREAK.
  [05/Jul/2021 06:11:45] "GET / HTTP/1.1" 200 5514
  [05/Jul/2021 06:11:50] "GET /donate/ HTTP/1.1" 200 5138
  [05/Jul/2021 06:11:50] "GET /static/donate/js/stripe.js HTTP/1.1" 304 0
  Data: <QueryDict: {'csrfmiddlewaretoken': ['EjaOUESHr7yL1gmIfA8S5obPtlZ8OF89EF2BXWCgbxQ0wwISZ755t2y8VhfGFRXR'], 'nickname': ['Test Name'], 'email': ['test@email.com'], 'amount': ['50'], 'stripeToken': ['tok_1J9omcIpOT7SMB9HPoBXjSHo']}>
  [05/Jul/2021 06:12:10] "POST /donate/charge/ HTTP/1.1" 302 0
  [05/Jul/2021 06:12:10] "GET /donate/success/5/ HTTP/1.1" 200 3954
  ```


References:
- [django MultiValueDictKeyError error, how do I deal with it](https://stackoverflow.com/questions/5895588/django-multivaluedictkeyerror-error-how-do-i-deal-with-it)

### Stripe Forbidden (CSRF cookie not set.)

- Error: Forbidden (CSRF cookie not set.): /donate/charge/

  ```
  System check identified no issues (0 silenced).
  July 12, 2021 - 14:11:20
  Django version 3.2.4, using settings 'django_blogchat_tech.settings'
  Starting development server at http://127.0.0.1:8000/
  Quit the server with CTRL-BREAK.
  [12/Jul/2021 14:11:23] "GET / HTTP/1.1" 200 5520
  [12/Jul/2021 14:11:41] "GET /donate/ HTTP/1.1" 200 5086
  [12/Jul/2021 14:11:41] "GET /static/css/headers.css HTTP/1.1" 200 466
  [12/Jul/2021 14:11:41] "GET /static/css/base.css HTTP/1.1" 200 264
  [12/Jul/2021 14:11:41] "GET /static/donate/css/donate.css HTTP/1.1" 200 100
  [12/Jul/2021 14:11:41] "GET /static/donate/js/stripe.js HTTP/1.1" 200 2083
  Forbidden (CSRF cookie not set.): /donate/charge/
  [12/Jul/2021 14:12:57] "POST /donate/charge/ HTTP/1.1" 403 2870
  Forbidden (CSRF cookie not set.): /donate/charge/
  [12/Jul/2021 14:15:40] "POST /donate/charge/ HTTP/1.1" 403 2870
  C:\Users\user\Downloads\MS4PomodoroBlogChat\django-blogchat-tech\donate\views.py changed, reloading.
  Watching for file changes with StatReloader
  Performing system checks...
  ```

- Root Cause: CSRF decorator required for Stripe view

- Fix include input element name attribute

  ```
  @csrf_protect
  def charge(request):
      """ A view to process donation """
  ```

### Django Model - TypeError: __str__ returned non-string

- Error: TypeError: __str__ returned non-string (type NoneType)

- Root Cause: return self.name is a CharField 

```
class UserProfile(models.Model):
    """
    A user profile model for maintaining user profiles
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80,
                            null=True, blank=True)
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)

    def __str__(self):
        return self.name
```
- Fix - str type needs to be explicit for self.name

```
    def __str__(self):
        return str(self.name)
```
Reference:
[Django __str__ returned non-string (type NoneType)](https://stackoverflow.com/questions/47121046/django-str-returned-non-string-type-nonetype/47263135)

### Django Model Test Foreign Key

- Error:
```
(venv) C:\Users\user\Downloads\MS4PomodoroBlogChat\django-blogchat-tech>python manage.py test profile.test_models  
System check identified no issues (0 silenced).
E
======================================================================
ERROR: test_models (unittest.loader._FailedTest)
----------------------------------------------------------------------
AttributeError: module 'profile' has no attribute 'test_models'
```

- Root Cause:  Did not create user object to be referenced
```
    @classmethod
    def setup(cls):
        UserProfile.objects.create( user= user, name='testuser',email='testemail@example.com' )
```

- Fix 
```
    @classmethod
    def setup(cls):
        user = get_user_model().objects.create_user(
                username='testuser', email='testemail@example.com',
                password='secret')
        UserProfile.objects.create( user= user, name='testuser',email='testemail@example.com' )
```

Reference:
- [how to test a model that has a foreign key in django?](https://stackoverflow.com/questions/44604686/how-to-test-a-model-that-has-a-foreign-key-in-django)

- [How to pass data for OneToOneField when testing?](https://stackoverflow.com/questions/56721076/how-to-pass-data-for-onetoonefield-when-testing)

### Django 'str' object has no attribute 'get' - Stack Overflow

- Error:  
```
Reverse for 'user_profile' with no arguments not found. 1 pattern(s) tried: ['profiles/(?P<user>[^/]+)/$']
```

- Root Cause: Url pattern requires argument <str:user>
```
path('<str:user>/', views.user_profile, name='user_profile'),
```

- Fix

```
response = self.client.get(reverse('edit_profile', kwargs = {'user': self.user}))
```

Reference:
- [Django Testing Tutorial - Testing Views #3](https://www.youtube.com/watch?v=hA_VxnxCHbo)
- [Views that are restricted to logged in users](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing)
- [Try DJANGO Tutorial - 34 - Django URLs Reverse](https://www.youtube.com/watch?v=JqbBGxDLQeU)
- [Django Testing Tutorial - How To Test Your Django Applications (Using The Unittest Module)](https://www.youtube.com/playlist?list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM)

### Stripe Public Key Issue

- Error: Integration Error: Missing value for Stript(): apikey should be a string.

![Stripe Integration Error](docs\testing\stripeIntegrationError.png)


- Root Cause: 

The name of the public key was not the same in the stripe.js and view.py

- Fix:

```
// Get Stripe publishable key
fetch("/donate/config/")
.then((result) => {
  console.log("then result");
  return result.json(); })
.then((data) => {
  // Initialize Stripe.js
  const stripe = Stripe(data.publicKey);
  console.log("then data");
```

```
@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': os.environ.get('STRIPE_PUBLIC_KEY') }
        return JsonResponse(stripe_config, safe=False)
```

### admin.py Post model AttributeError

- Error: 
python manage.py runserver
```
AttributeError: 'Post' object has no attribute 'publish'
```

- Root Cause: 

The field name publish_date is not the same as referenced by slug unique_for_date='publish'

- Fix

Change the field name publish_date to publish in model.y and admin.py

### Donate model test warning timezone

- Error:

```
(venv) C:\Users\user\Downloads\MS4PomodoroBlogChat\django-blogchat-tech>python manage.py test donate.test_models
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
C:\Users\user\Downloads\MS4PomodoroBlogChat\django-blogchat-tech\venv\lib\site-packages\django\db\models\fields\__init__.py:1358: RuntimeWarning: DateTimeField Donation.donate_date received a naive datetime (2021-08-02 00:00:00) while time zone support is active.
  warnings.warn("DateTimeField %s.%s received a naive datetime "
.
----------------------------------------------------------------------
Ran 1 test in 0.006s

OK
Destroying test database for alias 'default'...
```

- Root Cause:
Introduced timezone for the blog app model need to update for donate test 

- Fix 
Modify test import timezone and replace datetime.date.today() with timezone.now()

## Reverse resolution of URLs template tag syntax error

- Error: TemplateSyntaxError at /blog/topic/javascript/ Could not parse the remainder: '=' from '='

- Root Cause: Syntax error passing url paramet
- Fix: 

```
              <div class="dropdown-menu dropdown-menu-dark" aria-labelledby="navbarDarkDropdownMenuLink">
                {% for topic in topic_list %}
                  <a href="{% url 'topic' topic.name %}" class="dropdown-item">
                  {{ topic.name|title }}
                  </a>
                {% endfor %}
              </div> 
```

Reference:
[Reverse resolution of URLs](https://docs.djangoproject.com/en/3.2/topics/http/urls/)

### error

- Error:

- Root Cause: 

- Fix 

Reference:
[]()

## Final Check

- Debug Off
- credentials and passwwords not pushed to github
- Ensure that users not logged in are redirected to the login page. 
- Check that authentication cannot be bypassed by typing the URL into the browser bar -  consider creating custom 403/404 pages to deal with this. 
- Make sure you have checked that no links result in an internal server error. 
- If you have included a user type with higher access privileges, then you can include example login credentials at submission. 
- Do not display links the user does not have the privileges to access.
