# Generated by Django 3.2 on 2021-07-25 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.TextField(max_length=100)),
                ('nome_assinante', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='fotoprincipal',
            name='data_add',
        ),
        migrations.AlterField(
            model_name='fotoprincipal',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
