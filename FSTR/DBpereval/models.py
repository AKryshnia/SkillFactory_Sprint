from django.db import models


class Tourist(models.Model):
    email = models.CharField(max_length=100, unique=True)
    fam = models.CharField(max_length=255) # фамилия
    name = models.CharField(max_length=255) # имя
    otc = models.CharField(max_length=255) # отчество
    phone = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.email


class Pereval(models.Model):
    NEW = 'NW'
    PENDING = 'PN'
    ACCEPTED = 'AC'
    REJECTED = 'RJ'
    STATUS_CHOICES = (
        ('NW', 'new'),
        ('PN', 'pending'),
        ('AC', 'accepted'),
        ('RJ', 'rejected'),
    )

    winter = models.ForeignKey('Level', on_delete=models.CASCADE, related_name='winter_level')
    spring = models.ForeignKey('Level', on_delete=models.CASCADE, related_name='spring_level')
    summer = models.ForeignKey('Level', on_delete=models.CASCADE, related_name='summer_level')
    autumn = models.ForeignKey('Level', on_delete=models.CASCADE, related_name='autumn_level')

    beauty_title = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    other_titles = models.CharField(max_length=128)
    connect = models.CharField(max_length=128)
    add_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Tourist, on_delete=models.CASCADE)
    coords = models.OneToOneField('Coordinates', on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=NEW)


class Coordinates(models.Model):
    latitude = models.DecimalField(decimal_places=8, max_digits=10)
    longitude = models.DecimalField(decimal_places=8, max_digits=10)
    elevation = models.IntegerField(default=0)

class Level(models.Model):
    LVLA_1 = '1A'
    LVLA_2 = '2A'
    LVLA_3 = '3A'
    LVLB_1 = '1Б'
    LVLB_2 = '2Б'
    LVLB_3 = '3Б'
    LEVEL_CHOICES = (
        ('1A', '1A'),
        ('2A', '2A'),
        ('3A', '3A'),
        ('1Б', '1Б'),
        ('2Б', '2Б'),
        ('3Б', '3Б'),
    )
    level = models.CharField(max_length=2, choices=LEVEL_CHOICES, default=LVLA_1)


class PerevalImage(models.Model):
    # само изображение
    data = models.ImageField(upload_to='pereval_image', default='default.jpg')
    title = models.CharField(max_length=255) # название
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE, related_name='images') # id перевала

