author = Author(name="Chirag", email="chirag@example.com")
print(author)

Without **str**, this would look like:

<Author: Author object (1)>

But because you defined:

def **str**(self):
return self.name

Chirag
