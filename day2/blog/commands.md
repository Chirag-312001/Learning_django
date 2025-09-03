author = Author(name="Chirag", email="chirag@example.com")
print(author)

Without **str**, this would look like:

<Author: Author object (1)>

But because you defined:

def **str**(self):
return self.name

Chirag

=====================================

created the 3 models

- tired creating the foreign key

=====================================

while adding the multiple models in admin panel we should add one by one

like this

from django.contrib import admin
from .models import Posts, Author, Comments

admin.site.register(Author)
admin.site.register(Posts)
admin.site.register(Comments)

=====================================

Django Shell (Play with ORM)

---

python manage.py shell

---

from blog.models import Author, Post, Comment

# Create Author

a1 = Author.objects.create(name="Chirag", email="chirag@example.com")

# Create Post

p1 = Post.objects.create(title="My First Post", content="Hello Django!", author=a1)

# Create Comment

c1 = Comment.objects.create(post=p1, text="Nice post!")

# Query all posts

Post.objects.all()

# Filter

Post.objects.filter(author\_\_name="Chirag")

# Reverse relation (Author → Posts)

a1.posts.all()

# Reverse relation (Post → Comments)

p1.comments.all()

=====================================

Common ORM Queries

Get first post:

Post.objects.first()

Filter with conditions:

Post.objects.filter(title\_\_icontains="django")

Exclude:

Post.objects.exclude(title\_\_icontains="django")

Order by:

Post.objects.order_by('-created_at')

Count:

Post.objects.count()

=====================================

Optimize with select_related & prefetch_related

These reduce extra database hits.

Example:

# Without optimization → extra queries for author

posts = Post.objects.all()
for p in posts:
print(p.author.name) # Triggers extra queries

# Optimized

posts = Post.objects.select_related('author')
for p in posts:
print(p.author.name)

For Many-to-Many or reverse lookups:

posts = Post.objects.prefetch_related('comments')

=========================================

📝 Django ORM Cheat Sheet (Quick Reference)

1. Create Objects
   Author.objects.create(name="Chirag", email="chirag@example.com")
   Post.objects.create(title="Hello", content="First post!", author=a1)

2. Read (Basic Queries)
   Post.objects.all() # All records
   Post.objects.first() # First record
   Post.objects.last() # Last record
   Post.objects.get(id=1) # Get one (raises error if not found)

3. Filter
   Post.objects.filter(title="Hello")
   Post.objects.filter(title**icontains="django") # Case-insensitive match
   Post.objects.filter(created_at**year=2025) # Year filter

4. Exclude
   Post.objects.exclude(title\_\_icontains="draft")

5. Ordering
   Post.objects.order_by('created_at') # Asc
   Post.objects.order_by('-created_at') # Desc

6. Count & Exists
   Post.objects.count()
   Post.objects.filter(author=a1).exists()

7. Update
   p1 = Post.objects.get(id=1)
   p1.title = "Updated Title"
   p1.save()

Or bulk update:

Post.objects.filter(author=a1).update(title="New Title")

8. Delete
   p1 = Post.objects.get(id=1)
   p1.delete()

Or bulk delete:

Post.objects.filter(author=a1).delete()

9. Relationships

# Forward

p1.author # Get post’s author
c1.post # Get comment’s post

# Reverse (thanks to related_name)

a1.posts.all() # All posts by author
p1.comments.all() # All comments on post

10. Query Optimization
    Post.objects.select_related('author') # For FK/OneToOne
    Post.objects.prefetch_related('comments') # For reverse/M2M

11. Aggregation & Annotation
    from django.db.models import Count, Avg

Post.objects.aggregate(total=Count('id')) # Total posts
Post.objects.annotate(num_comments=Count('comments'))

12. Q Objects (OR conditions)
    from django.db.models import Q

Post.objects.filter(Q(title**icontains="django") | Q(content**icontains="api"))
