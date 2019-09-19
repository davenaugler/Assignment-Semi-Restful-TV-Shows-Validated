from django.db import models



# Create your models here.

class ShowsManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Title should be at least 2 characters"
        if len(postData['network']) < 3: 
            errors['network'] = "Network should be at least 3 characters"
        if len(postData['release_date']) < 8:
            errors['release_date'] = "Release date should have at least 8 characters"
        if len(postData['description']) < 10:
            errors['description'] = "Description should be at least 10 characters"
        return errors
        



class Shows(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    description = models.CharField(max_length=255)
    release_date = models.DateField('%m-%d-%Y')
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)
    objects = ShowsManager()

    def __repr__(self):
        return f"Shows: ({self.id})| Title: {self.title}| Network: {self.network}| Description: {self.description}| Release-Date: {self.release_date}"
