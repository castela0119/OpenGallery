# Generated by Django 4.0.4 on 2022-05-28 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': '선택사항',
                'db_table': 'choice',
            },
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': '설문조사',
                'db_table': 'survey',
            },
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participant_email', models.EmailField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('answer', models.ManyToManyField(to='surveys.choice')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='surveys.survey')),
            ],
            options={
                'verbose_name_plural': '제출',
                'db_table': 'submission',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='surveys.survey')),
            ],
            options={
                'verbose_name_plural': '질문',
                'db_table': 'question',
            },
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='surveys.question'),
        ),
    ]
