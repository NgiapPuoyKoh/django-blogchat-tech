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

| User Case # | As Persona | Want to |
| --- | --- | --- |
| 1.1 | As a user | I want to know the purpose and how to use the blog |
| 1.2 | As a user | I want to view a list of features |
| 1.3 | As a user | I want to know how to use each feature |
| 1.4 | As a user | I want to navigate to each feature from the feature page |

| 2.1 | As a non-authenticated user | I want to be able to view a list of blog posts |
| 2.2 | As a non-authenticated user | I want to be able to view blog details |
| 2.3 | As a non-authenticated user | I can make submit a comment on a post |
| 2.4 | As an authenticated user | I want to be able to search for blogs|
| 2.5 | As a non-authenticated user | I want to be able to register an account |

| 3.1 | As an authenticated user | I want to be able to create a blog post |
| 3.2 | As an authenticated user | I want to be | 
able to update my blog post |
| 3.3 | As an authenticated user | I want to be able to delete my blog post |
| 3.4 | As an authenticated user | I want to be able to set the status of my blog post |

| 4.1 | As a authenticated user | I can make submit a comment on a post |
| 4.2 | As an authenticated user | I want to be able to comment on a blog post |
| 4.3 | As an authenticated user | I want to be able to view a blog list
| 4.4  | As an authenticated user | I want to be view blog list by topic|
| 4.5 | As a non-authenticated user | I want to be able able to view blog details|
| 4.6 | As an authenticated user | I want to be able to search for blogs|
| 4.7 | As a non-authenticated user | I can comment on a post |

| 5.1 | As an authenticated user | I want to be able to login |
| 5.2 | As an authenticated user | I Want to be able to create my profile information |
| 5.3 | As an authenticated user | I want to be able to edit my profile information |

| 6.1 | As a user | I want to be able to make voluntary donations of any amount using a credit card |
| 6.2 | As a user, I want to be able to make secure payments

| 7.1 | As an administrator | I want to be able to create a user account |
| 7.2 | As an administrator | I want to be able to update a user |
| 7.3 | As an administrator | I want to be able to delete a user |
| 7.4 | As an administrator | I want to be able to manage the topic list |
| 7.5 | As an administrator | I want to be able to have CRUD privileges to curate blog posts |
| 7.5 | As an administrator | I want to be able to have CRUD privileges to curate comments |

| 8.1 | As a site owner | I want to accept donations to maintain the site |
| 8.2 | As a site owner | I want to be able to track donors information and donation amounts

Future Features

- As a user, I want to be able to rate a blog post
- As a blogger, I want to be able to have a conversation with readers via live chat
- As a blogger, I want to be able to set a blog to a status draft, publish and unpublish
- As a blogger, I want to be able to create a blog series playlist
