from django.db import models
from django.utils import timezone

# Model representing an issue in the application
class Issue(models.Model):
    # Title of the issue
    title = models.CharField(max_length=200)
    # Description of the issue
    description = models.TextField()
    # Publication date of the issue
    pub_date = models.DateTimeField('date published')

    # String representation of the Issue model
    def __str__(self):
        return self.title

    # Method to check if the issue was published recently (within the last day)
    def was_published_recently(self):
        now = timezone.now()
        return now - timezone.timedelta(days=1) <= self.pub_date <= now

# Model representing a member in the application
class Member(models.Model):
    # Name of the member
    name = models.CharField(max_length=100)
    # Email of the member (must be unique)
    email = models.EmailField(unique=True)
    # Date when the member joined (automatically set when the record is created)
    joined_date = models.DateTimeField(auto_now_add=True)

    # String representation of the Member model
    def __str__(self):
        return self.name

# Model representing a contribution made by a member
class Contribution(models.Model):
    # Foreign key linking the contribution to a member
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    # Amount of the contribution
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Date when the contribution was made (automatically set when the record is created)
    date = models.DateTimeField(auto_now_add=True)

    # String representation of the Contribution model
    def __str__(self):
        return f'{self.member.name} - {self.amount}'
