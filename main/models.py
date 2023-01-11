from django.db import models

class User(models.Model):
    
    username = models.TextField(max_length=20)
    
class UserInput(models.Model):
    
    api_type = (
        ('BP', 'Write Blog Post'),
        ('TC', 'Text to Code'),
        ('EC', 'Explain Code'),
    )
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    input = models.TextField(max_length=500)
    created_time = models.DateTimeField(auto_now=True)
        
class UserHistory(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    input = models.ForeignKey(UserInput, on_delete=models.CASCADE)
    output = models.TextField(max_length=1000)
    created_time = models.DateTimeField(auto_now=True)
