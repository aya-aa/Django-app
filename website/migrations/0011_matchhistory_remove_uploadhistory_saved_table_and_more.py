# Generated by Django 4.2.4 on 2023-08-29 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_modelsave'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_date', models.DateTimeField(auto_now_add=True)),
                ('cv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.mymodel')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.post')),
            ],
        ),
        migrations.RemoveField(
            model_name='uploadhistory',
            name='saved_table',
        ),
        migrations.RemoveField(
            model_name='uploadhistory',
            name='user',
        ),
        migrations.DeleteModel(
            name='ModelSave',
        ),
        migrations.DeleteModel(
            name='UploadHistory',
        ),
    ]
