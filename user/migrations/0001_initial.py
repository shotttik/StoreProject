# Generated by Django 3.2 on 2021-04-14 17:32

from django.db import migrations, models
import django.utils.timezone
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-Mail')),
                ('personal_number', models.CharField(max_length=11, unique=True, verbose_name='პირადი ნომერი')),
                ('mobile_phone', models.CharField(max_length=9, verbose_name='ტელეფონის ნომერი')),
                ('member_status', models.PositiveSmallIntegerField(choices=[(1, 'ბუღალტერი'), (2, 'დიზაინერი'), (3, 'მენეჯერი'), (4, 'ქოლ ცენტრი')])),
                ('location', models.PositiveSmallIntegerField(choices=[(1, 'თბილისი'), (2, 'რეგიონი')])),
                ('address', models.CharField(max_length=255, verbose_name='მისამართი')),
                ('balance', models.DecimalField(decimal_places=2, default=0, help_text='$', max_digits=8, verbose_name='ბალანსი')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', user.models.UserManager()),
            ],
        ),
    ]