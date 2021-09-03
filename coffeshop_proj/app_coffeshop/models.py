from django.db import models
from django.contrib.auth.models import User

STATUS_TYPE = (
    (1, 'waiting'),
    (2, 'preparation'),
    (3, 'ready'),
    (4, 'delivered.'),
)


class Product(models.Model):
    title = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.title


class Option(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    ingredients = models.CharField(max_length=15, null=True)

    def __str__(self):
        return "{}: {}".format(self.product, self.ingredients)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    _status = models.PositiveSmallIntegerField(null=True, choices=STATUS_TYPE)

    # getter
    @property
    def status(self):
        return dict(STATUS_TYPE).get(self._status)

    @status.setter
    def status(self, value):
        self._status = {v: k for k, v in STATUS_TYPE}.get(value)

    def __str__(self):
        return "{}: {} - {}".format(self.user, self.product, self.status)
