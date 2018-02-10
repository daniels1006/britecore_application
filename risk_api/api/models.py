from django.db import models


class RiskType(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Risk(models.Model):
    risk_type = models.ForeignKey('api.RiskType', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class DataType(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Field(models.Model):
    risk_type = models.ForeignKey('api.RiskType', on_delete=models.DO_NOTHING)
    data_type = models.ForeignKey('api.DataType', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=64)

    def __str__(self):
        return '(' + self.risk_type.name + ')' + ' ' + self.name


class MetaField(models.Model):
    field = models.ForeignKey('api.Field', on_delete=models.CASCADE)
    key = models.CharField(max_length=64)
    value = models.CharField(max_length=1024)

    def __str__(self):
        return '(' + self.field.name + ')' + ' ' + self.key


class RiskData(models.Model):
    risk = models.ForeignKey('api.Risk', on_delete=models.CASCADE)
    field = models.ForeignKey('api.Field', on_delete=models.DO_NOTHING)
    value = models.CharField(max_length=1024)

    def __str__(self):
        return self.value
