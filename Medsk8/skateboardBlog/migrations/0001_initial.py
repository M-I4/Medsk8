# Generated by Django 4.1.3 on 2022-11-16 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0003_alter_profile_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024)),
                ('content', models.TextField()),
                ('publish_date', models.DateTimeField()),
                ('image', models.ImageField(upload_to='images/')),
                ('post_type', models.CharField(choices=[('Article', 'Article'), ('Opinion', 'Opinion'), ('Review', 'Review')], default='Article', max_length=64)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skateboardBlog.post')),
            ],
        ),
    ]