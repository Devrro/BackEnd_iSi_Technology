Hello there. I am going to show you simple django project with rest_framework connection. 

First of all, I want to thank your company for this test. It was fun to do
and I remembered many of things I had learned before

Secondly, I have to admit that tasks were done with not 100% accuracy of the provided plan.
Let`s go down and see what I did.


1. App "simple_chat" was created. Every model in it has mentioned in task fields. There was some
little desire to change the models and add more fields, but I decided to act according to task items.
It was not possible (at least for now) to quickly disable the ability to create a "Thread" instance.\
But I found a few ways to do that. \
    - I. Create model contraints -> Since "participant field" is models.ManyToMany field it was not possible
    without using "through". I decided to avoid that :skull:
    - II. Rewrite add() method for ManyToMany manager. -> I think it's the most interesting way to do that, but a bit too complex 
    for a such task.\
    - III. Just validate data and check field in API View. -> I guess it was the easiest way and fastest way to do that.:skull:
In my sea of overthinking I found that the option (III) was the best for me and id didn`t require too much work to do. 
End-points are added.\
The need in URL validation with RegEx is a bit exaggerated for now because i am using rest_framework serializers and
views.\
2. Simple django admin panel is provided. Never used and I would rewrite it in. 
3. LimitOfsetPagination is set as default pagination class for all views.
4. Look the 2 paragraph
5. Django is installed and working.
6. Custom UserModel is created and provided in settings.py

**How to run**\
- Install pipenv
- create \ run virtualenv using pipenv from .backend directory with dependecies in Pipfile
  - > pipenv install  
- Use console command in .backend directory (Windows)
  - > python manage.py runserver

After it`s better to use **[Postman agent](https://www.postman.com/devrro/workspace/testing/overview)**  for all requests, except those in "/admin" URL path.
Don't forget to set environment in upper right corner menu!
All views are created with AllowAny permission class.
