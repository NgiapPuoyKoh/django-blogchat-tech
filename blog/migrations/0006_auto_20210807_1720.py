# Generated by Django 3.2.4 on 2021-08-07 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210805_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10),
        ),
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(choices=[('whitenoise', 'Whitenoise'), ('bootstrap5', 'Bootstrap5'), ('stripe', 'Stripe'), ('sql', 'SQL'), ('javascript', 'JavaScript'), ('django', 'Django')], default='No Topic', max_length=254),
        ),
    ]
