from django.db import models
from django.urls import reverse

# Create your models here.
# st_id, fname, lname

PREFIX_NAME = (
    ("นาย", "นาย"),
    ("นางสาว", "นางสาว"),
    ("นาง", "นาง"),
)


class Student(models.Model):
    prefix_name = models.CharField(max_length=10, choices=PREFIX_NAME, default="นาย")
    st_id = models.CharField(max_length=12, unique=True)
    fname = models.CharField(max_length=100, blank=False)
    lname = models.CharField(max_length=100, blank=False)
    major = models.ForeignKey('Major', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.fname + " " + self.lname

    def get_absolute_url(self):
        return reverse("student_detail", kwargs={"pk": self.pk})


class Major(models.Model):
    mj_name = models.CharField(max_length=100, blank=False)

    class Meta:
        verbose_name = "Major   "
        verbose_name_plural = "Majors"

    def __str__(self):
        return self.mj_name

    def get_absolute_url(self):
        return reverse("Major_detail", kwargs={"pk": self.pk})
