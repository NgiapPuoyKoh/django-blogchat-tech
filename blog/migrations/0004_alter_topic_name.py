# Generated by Django 3.2.4 on 2021-08-05 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210801_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(choices=[('sql', 'SQL'), ('bootstrap5', 'Bootstrap5'), ('javascript', 'JavaScript'), ('whitenoise', 'Whitenoise'), ('django', 'Django'), ('stripe', 'Stripe')], default='No Topic', max_length=254),
        ),
    ]
