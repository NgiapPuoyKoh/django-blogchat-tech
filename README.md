# Pomodoro Blog

[Click here access Pomodoro Blog](https://django-blogchat-tech.herokuapp.com/)

"Reading maketh a full man; conference a ready man; and writing an exact man." Francis Bacon

Pomodoro BlogChat is a site for users to read, converse and write about topics. Each blog entry focuses on a single concept.

The brain operates in two fundamental modes focus diffuse mode. Work with focus attention for 24 minutes and relax for 5 minutes. Practice slow thinking and exercise to increase the ability to learn and recall. Understanding combined with practice and repetition in a variety of circumstances to truly gain mastery.

The inspiration for this application came from Francis Bacon's quote and  [Barbara Oakley: Learning How to Learn](https://tedsummaries.com/2015/03/04/barbara-oakley-learning-how-to-learn/).

## User Experience Design (UX)

## Strategy Plane

### Purpose

This site provides a community platform where learners can apply the approach by reading(focus-mode) a blog to learn, have a conversation(diffuse-mode) to understand, and posting a blog(practice to master) to share their understanding. Users will help each other learn.

A blog post will typically be an explanation of a concept or a how-to tip or trick. The idea is to apply the Pomodoro approach to focus the blog post on a small chunk of information that takes no longer than 25 minutes to digest.

A blog series in turn will consist of a playlist of blog posts. As coders, one of the most important skills is to break down a problem into components and write code in chunks to solve the problem.

Readers can ask the blog post author questions and participate in a discussion via comments.

### Site Goals

#### Business Goals

- Free blog platform that can be simply implemented and deployed. It can be easily extended using the Django framework
- The site follows the minimum viable product (MVP) approach to identify and implement basic features that users to improve their learning outcome
- The site owner can accept voluntary donations
- The application can be implemented and configured for their own use
- The administrator of the blog will have full administrative privileges to control user access and privileges and to audit and remove content that is inappropriate or offensive

#### User Goals

- Authenticated users will be able to reinforce learning by publishing post blogs and make comments
- Non authenticated users will be able to access blog post content and make comments

#### Content

- The blog content will be categorized by topic
- The administrator will configure and maintain the list of topics for any subject
- Authors will use the title associate it with a blog series to build a collection of blogs

### User Stories

| Use Case # | As Persona | Want to |
| --- | --- | --- |
| 1.1 | As a user | I want to know the purpose and how to use the blog |
| 1.2 | As a user | I want to view a list of features |
| 1.3 | As a user | I want to know how to use each feature |
| 1.4 | As a user | I want to navigate to each feature from the feature page |
| | |
| 2.1 | As a non-authenticated user | I want to be able to view a list of blog posts |
| 2.2 | As a non-authenticated user | I want to be able to view blog details |
| 2.3 | As a non-authenticated user | I can make submit a comment on a post |
| 2.4 | As an authenticated user | I want to be able to search for blogs|
| 2.5 | As a non-authenticated user | I want to be able to register an account |
| | |
| 3.1 | As an authenticated user | I want to be able to create a blog post |
| 3.2 | As an authenticated user | I want to be able to update my blog post |
| 3.3 | As an authenticated user | I want to be able to delete my blog post |
| 3.4 | As an authenticated user | I want to be able to set the status of my blog post |
| | |
| 4.1 | As a authenticated user | I can make submit a comment on a post |
| 4.2 | As an authenticated user | I want to be able to comment on a blog post |
| 4.3 | As an authenticated user | I want to be able to view a blog list
| 4.4  | As an authenticated user | I want to be view blog list by topic|
| 4.5 | As a non-authenticated user | I want to be able able to view blog details|
| 4.6 | As an authenticated user | I want to be able to search for blogs|
| 4.7 | As a non-authenticated user | I can comment on a post |
| | |
| 5.1 | As an authenticated user | I want to be able to login |
| 5.2 | As an authenticated user | I Want to be able to create my profile information |
| 5.3 | As an authenticated user | I want to be able to edit my profile information |
| | |
| 6.1 | As a user | I want to be able to make voluntary donations of any amount using a credit card |
| 6.2 | As a user, I want to be able to make secure payments
| | |
| 7.1 | As an administrator | I want to be able to create a user account |
| 7.2 | As an administrator | I want to be able to update a user |
| 7.3 | As an administrator | I want to be able to delete a user |
| 7.4 | As an administrator | I want to be able to manage the topic list |
| 7.5 | As an administrator | I want to be able to have CRUD privileges to curate blog posts |
| 7.5 | As an administrator | I want to be able to have CRUD privileges to curate comments |
| | |
| 8.1 | As a site owner | I want to accept donations to maintain the site |
| 8.2 | As a site owner | I want to be able to track donors information and donation amounts

### Wireframes

<details>
    <summary> Click to expand!</summary>

**Note:**

```
The respective Mobile wireframes version of each web page listed will be similar to the Home Page Mobile Wireframe. The content stacked in a single column.
```

- Home Page

![Home Page](docs/wireframes/homePage.png)

- Home Page Mobile

![Home Page Mobile](docs/wireframes/homePageMobile.png)

- Sign In 

![Sign In](docs/wireframes/signInPage.png)

- Register Page

![Register Page](docs/wireframes/registerPage.png)

- Profile Create

![Profile Create](docs/wireframes/profileCreate.png)

- Profile Update Delete

![Profile Update Delete](docs/wireframes/profileUpdateDelete.png)

- Blog View Posts

 ![Blog View Posts](docs/wireframes/blogViewPosts.png)


- Blog Post Detail

![Blog Post Detail](docs/wireframes/blogViewPostDetail.png)

- Blog Post Create

![Blog Post Create](docs/wireframes/blogPostCreatePublish.png)

- Blog Post Edit Delete

![Blog Post Edit Delete](docs/wireframes/blogPostCreatePublish.png)

- Blog Posts Search

![Blog Posts Search](docs/wireframes/blogViewPostsSearch.png)

- Blog Posts Comment

![Blog Posts Comment](docs/wireframes/blogPostComments.png)

- Donate Page

![Donate Page](docs/wireframes/donatePage.png)

- Donate Success

![Donate Success](docs/wireframes/donateSuccessConfirmation.png)

</details>

## Scope Plane

### Planned Features

#### Mobile First responsive on all device sizes

The goal is to design the application to work on small screen sizes. The approach is to focus on what is necessary for rending and navigation.

#### Overview Feature Page

The feature page provides the user with information about the site. The page will render the description and a link to access each feature.

- Overview of the purpose of the application
- Feature Description
- Provide User with Instructions
- Navigation Links to Features

#### Blog Posts Display

The blog post page will render all posts by default. There will be an option to display posts by topic.
Each post will display the title and a link to navigate to view the details of the post.

All users will be able to view the blog.
Only authenticated users will be rendered buttons to update and delete posts owned by them.

- Blog List by Date
- Blog List by Topic
- Blog Detail

#### Blog Post Management CRUD

Only Authenticated users will be able to create, modify and publish posts that they share.

- Create a post
- Edit a post
- Delete a post
- Publish a post
- Unpublish a post

#### Blog Posts Search

Users can use the search navigation form on the navigation bar to search for blogs using keywords.
Posts that contain one or more of the keywords entered will render a search results page.

At the bottom of the results page, there will be an option to perform a new search.

- Search posts using keywords in title, excerpt, and content fields.
- Users to not need to be authenticated to perform a search.

#### Blog Post Comments

Users will be able to add comments to each post on the post detail page.
The comments will be rendered below each post on the detail post page.

- A comment form will be rendered below each post for any user to submit a comment
- Users do not need to be authenticated to post comments

#### User Authentication

Users who wish to create and share posts need to sign up for an account for authenticated access.
Authenticated users will have the privileges to manage the post that they create.

- Account Sign Up
- Account Sign In
- Access to create post link on the navigation bar

#### User Profile

Authenticated users will have the option to enter an alternated name and email.
This information can be utilized in future enhancements as the user's preferred contact information.

- Create a profile
- Update a profiles

### Blog Application Administration

The application administrator with superuser privileges have full access to all the data using the Django Administrator panel.

- Manage user access
- Curate blog post
- Curate comments
- Access details of donations received
  
### Donation

- Accept donation using stripe payment
- Simple Accept payment of any amount available only in the US and Canada
- Record donor name, email, and amount of donations received

## Future Features

### Live Chat Conversations

- As a blogger, I want to be able to have a conversation with readers via live chat

### Contact Form

- Users can submit questions to the site owner
- Administrator can respond to questions

### Donation Enhancements

- Automated email generation Thank You for Donations
- Dashboard to track and report donations received
- Donor information Management

### Blog Post Enhancements

- Blog Topic Category Management
- Rating and reviews
- Blog post status management to include draft, publish and unpublish
- Blog series playlist generation

### Blog Application Configuration, Administration and Data Management

- Application configuration dashboard
- Blog Topic Management
- Donation Management
- Data management dashboard

## Structure Plane

### Database Schema

![Pomodoro Blog Database Schema](docs/readme/pomodoroBlogDBSchema.png)

## Donate Apps

- Donation

```
class Donation(models.Model):
    """
    A model to record donations
    """
    donor_name = models.CharField(max_length=50)
    donor_email = models.EmailField(max_length=254)
    donate_date =  models.DateTimeField(max_length=80,
                                      null=False, blank=False)
    amount = models.IntegerField(default=0) 
    donated =  models.BooleanField(default=True)

    def __str__(self):
        return self.donor_name

```

## Blog App

- Topic

```
class Topic(models.Model):

    options = {
        ('django', 'Django'),
        ('bootstrap5', 'Bootstrap5'),
        ('javascript', 'JavaScript'),
        ('sql', 'SQL'),
        ('whitenoise', 'Whitenoise'),
        ('stripe', 'Stripe')
    }

    class Meta:
        verbose_name_plural = 'Topics'

    name = models.CharField(max_length=254, choices=options, default='No Topic')
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
```

- Post

```
class Post(models.Model):

    class Meta:
        verbose_name_plural = 'Posts'

    options = {
        ('draft', 'Draft'),
        ('published', 'Published'),
    }

    title = models.CharField(max_length=254)
    excerpt = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    status = models.CharField(max_length=10, choices=options, default='draft')
    topic = models.ForeignKey('Topic', null=True, blank=True, on_delete=models.SET_NULL)


    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})


    def __str__(self):
        return self.title

# Code Source: Try Django 1.9 - 29 of 38 - SlugField
def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Post)
```

- Comment

```

class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name ="comments")
    name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
    publish = models.DateTimeField(auto_now_add = True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ("publish",)

    def __str__(self):
        return f"Comment by {self.name}"
    
```

## Profile App

- UserProfile

```
class UserProfile(models.Model):
    """
    A user profile model for maintaining user profiles
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80,
                            null=True, blank=True)
    email = models.EmailField(max_length=70, blank=True, null=True, unique= True)

    def __str__(self):
        return str(self.name)
    
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()

```

## Django Contrib and Alluth

- allauth socialaccount
- auth
- admin
- sites
- contenttype
- sessions
- Abstract BaseUser
- Abstract PermmissionsMixin


The structure plane: How is the information structured and how is it logically grouped?