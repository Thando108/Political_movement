from django.db import models
from django.utils import timezone

class Issue(models.Model):
    """
    Model representing an issue in the application.

    Attributes:
        title (CharField): The title of the issue.
        description (TextField): The description of the issue.
        pub_date (DateTimeField): The publication date of the issue.
    """

    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """
        Returns the string representation of the Issue model.

        Returns:
            str: The title of the issue.
        """
        return self.title

    def was_published_recently(self):
        """
        Checks if the issue was published recently (within the last day).

        Returns:
            bool: True if the issue was published within the last day, False otherwise.
        """
        now = timezone.now()
        return now - timezone.timedelta(days=1) <= self.pub_date <= now

class Member(models.Model):
    """
    Model representing a member in the application.

    Attributes:
        name (CharField): The name of the member.
        email (EmailField): The email of the member (must be unique).
        joined_date (DateTimeField): The date when the member joined (automatically set when the record is created).
    """

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    joined_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns the string representation of the Member model.

        Returns:
            str: The name of the member.
        """
        return self.name

class Contribution(models.Model):
    """
    Model representing a contribution made by a member.

    Attributes:
        member (ForeignKey): A foreign key linking the contribution to a member.
        amount (DecimalField): The amount of the contribution.
        date (DateTimeField): The date when the contribution was made (automatically set when the record is created).
    """

    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns the string representation of the Contribution model.

        Returns:
            str: A string combining the member's name and the contribution amount.
        """
        return f'{self.member.name} - {self.amount}'

