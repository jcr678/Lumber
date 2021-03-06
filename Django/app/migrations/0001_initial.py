# Generated by Django 3.0.5 on 2020-04-07 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('isemployee', models.BooleanField(default=False)),
                ('startemploymentweeks', models.IntegerField()),
                ('endemploymentweeks', models.IntegerField()),
                ('messages', models.TextField()),
                ('Jobtype', models.TextField()),
                ('availabilemonday', models.BooleanField(default=False)),
                ('availabiletuesday', models.BooleanField(default=False)),
                ('availabilewednesay', models.BooleanField(default=False)),
                ('availabilethursday', models.BooleanField(default=False)),
                ('availabilefriday', models.BooleanField(default=False)),
                ('availabilesaturday', models.BooleanField(default=False)),
                ('availabilesunday', models.BooleanField(default=False)),
                ('introduction', models.TextField()),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('matches', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matched', to='app.Person')),
                ('swipesiminterestedin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='them', to='app.Person')),
                ('swipesinterestedinme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='me', to='app.Person')),
            ],
        ),
    ]
