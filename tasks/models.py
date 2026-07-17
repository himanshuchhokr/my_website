from django.db import models


class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('progress', 'In Progress'),
        ('done', 'Done'),
    ]

    TAG_CHOICES = [
        ('DSA', 'DSA'),
        ('Python', 'Python'),
        ('Web Dev', 'Web Dev'),
        ('Maths', 'Maths'),
        ('Project', 'Project'),
        ('Hackathon', 'Hackathon'),
        ('Other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    tag = models.CharField(max_length=20, choices=TAG_CHOICES, default='Other')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='todo')
    commit_hash = models.CharField(max_length=8, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.commit_hash:
            import uuid
            self.commit_hash = uuid.uuid4().hex[:7]
        super().save(*args, **kwargs)

    def __str__(self):
        return f"[{self.status}] {self.title}"
