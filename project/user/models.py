from django.core.validators import FileExtensionValidator, validate_image_file_extension, MinLengthValidator
from rest_framework.exceptions import ValidationError
from project.settings import GENDERS
from django.utils.timezone import now
from django.db import models


def DateValidator(date, year_difference=3):
    today = now()
    if today.year - date.year < year_difference:
        raise ValidationError(detail=f'Year difference must be high {year_difference}')


def CharValidator(value):
    if not value.isalpha():
        raise ValidationError(detail='All the characters must be alphabet letters')


# create User model with all fields
class User(models.Model):

    dob = models.DateField('Date of birth', blank=False,
                           validators=[DateValidator])

    name = models.CharField('Name', max_length=20, blank=False,
                            validators=[MinLengthValidator(limit_value=2, message=None),
                                        CharValidator])

    last_name = models.CharField('Last name', max_length=20, blank=False,
                                 validators=[MinLengthValidator(limit_value=2, message=None),
                                             CharValidator])

    gender = models.CharField('Gender', max_length=1, choices=GENDERS)

    cv = models.FileField('CV / Resume', upload_to='',
                          validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    image = models.ImageField('Picture', upload_to='',
                              validators=[validate_image_file_extension,
                                          FileExtensionValidator(allowed_extensions=['jpeg', 'png'])])

    def __str__(self):
        return f"Date of birth: {self.dob}\nName: {self.name}\n" \
               f"Surname: {self.last_name}\nGender: {self.gender}"
