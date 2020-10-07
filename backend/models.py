from django.db import models

# Todo Model
# Fields: 
# 		- text <CharField>: User created text specifying a "todo" 
# 		- created_at <DateTimeField>: Timestamp of creation
class Todo(models.Model): 
	text       = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self): 
		return self.text