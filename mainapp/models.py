from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255,null=True, blank=True)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:     # change in admin view and sql commands
        ordering = ['-created_date']
    
    def __str__(self):
        return '{} ({})'.format(self.name, self.id)
    

class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return '{} ({})'.format(self.email, self.id)