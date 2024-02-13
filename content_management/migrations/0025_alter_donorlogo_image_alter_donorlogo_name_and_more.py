# Generated by Django 5.0.1 on 2024-02-13 12:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "content_management",
            "0024_alter_tender_title_alter_tender_title_en_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="donorlogo",
            name="image",
            field=models.FileField(
                help_text="Зображення має бути у форматі .jpg, .jpeg, .webp, .png або .svg та не перевищувати 2 МБ. Після завантаження зображення буде автоматично компресоване та змінено на формат .webp.",
                upload_to="donors-logos/",
                verbose_name="Зображення",
            ),
        ),
        migrations.AlterField(
            model_name="donorlogo",
            name="name",
            field=models.CharField(
                blank=True,
                help_text="Максимальна довжина тексту: 100 символів.",
                max_length=100,
                null=True,
                verbose_name="Імʼя донора",
            ),
        ),
        migrations.AlterField(
            model_name="donorlogo",
            name="name_en",
            field=models.CharField(
                blank=True,
                help_text="Максимальна довжина тексту: 100 символів.",
                max_length=100,
                null=True,
                verbose_name="Імʼя донора",
            ),
        ),
        migrations.AlterField(
            model_name="donorlogo",
            name="name_uk",
            field=models.CharField(
                blank=True,
                help_text="Максимальна довжина тексту: 100 символів.",
                max_length=100,
                null=True,
                verbose_name="Імʼя донора",
            ),
        ),
        migrations.AlterField(
            model_name="news",
            name="image",
            field=models.FileField(
                help_text="Зображення має бути у форматі .jpg, .jpeg, .webp, .png або .svg та не перевищувати 2 МБ. Після завантаження зображення буде автоматично компресоване та змінено на формат .webp.",
                upload_to="news/",
                verbose_name="Зображення",
            ),
        ),
        migrations.AlterField(
            model_name="partnerlogo",
            name="company_name",
            field=models.CharField(
                blank=True,
                help_text="Максимальна довжина тексту: 100 символів.",
                max_length=100,
                null=True,
                verbose_name="Назва компанії",
            ),
        ),
        migrations.AlterField(
            model_name="partnerlogo",
            name="company_name_en",
            field=models.CharField(
                blank=True,
                help_text="Максимальна довжина тексту: 100 символів.",
                max_length=100,
                null=True,
                verbose_name="Назва компанії",
            ),
        ),
        migrations.AlterField(
            model_name="partnerlogo",
            name="company_name_uk",
            field=models.CharField(
                blank=True,
                help_text="Максимальна довжина тексту: 100 символів.",
                max_length=100,
                null=True,
                verbose_name="Назва компанії",
            ),
        ),
        migrations.AlterField(
            model_name="partnerlogo",
            name="image",
            field=models.FileField(
                help_text="Зображення має бути у форматі .jpg, .jpeg, .webp, .png або .svg та не перевищувати 2 МБ. Після завантаження зображення буде автоматично компресоване та змінено на формат .webp.",
                upload_to="partner-logos/",
                verbose_name="Зображення",
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.FileField(
                help_text="Зображення має бути у форматі .jpg, .jpeg, .webp, .png або .svg та не перевищувати 2 МБ. Після завантаження зображення буде автоматично компресоване та змінено на формат .webp.",
                upload_to="projects/",
                verbose_name="Зображення",
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="title",
            field=models.CharField(
                help_text="Максимальна довжина тексту: 100 символів.",
                max_length=100,
                verbose_name="Назва",
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="title_en",
            field=models.CharField(
                help_text="Максимальна довжина тексту: 100 символів.",
                max_length=100,
                null=True,
                verbose_name="Назва",
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="title_uk",
            field=models.CharField(
                help_text="Максимальна довжина тексту: 100 символів.",
                max_length=100,
                null=True,
                verbose_name="Назва",
            ),
        ),
        migrations.AlterField(
            model_name="teammember",
            name="full_name",
            field=models.CharField(
                help_text="Максимальна довжина тексту: 200 символів.",
                max_length=200,
                verbose_name="Повне ім'я",
            ),
        ),
        migrations.AlterField(
            model_name="teammember",
            name="full_name_en",
            field=models.CharField(
                help_text="Максимальна довжина тексту: 200 символів.",
                max_length=200,
                null=True,
                verbose_name="Повне ім'я",
            ),
        ),
        migrations.AlterField(
            model_name="teammember",
            name="full_name_uk",
            field=models.CharField(
                help_text="Максимальна довжина тексту: 200 символів.",
                max_length=200,
                null=True,
                verbose_name="Повне ім'я",
            ),
        ),
        migrations.AlterField(
            model_name="teammember",
            name="image",
            field=models.FileField(
                help_text="Зображення має бути у форматі .jpg, .jpeg, .webp, .png або .svg та не перевищувати 2 МБ. Після завантаження зображення буде автоматично компресоване та змінено на формат .webp.",
                upload_to="team-members/",
                verbose_name="Зображення",
            ),
        ),
        migrations.AlterField(
            model_name="teammember",
            name="position",
            field=models.CharField(
                help_text="Максимальна довжина тексту: 200 символів.",
                max_length=200,
                verbose_name="Посада",
            ),
        ),
        migrations.AlterField(
            model_name="teammember",
            name="position_en",
            field=models.CharField(
                help_text="Максимальна довжина тексту: 200 символів.",
                max_length=200,
                null=True,
                verbose_name="Посада",
            ),
        ),
        migrations.AlterField(
            model_name="teammember",
            name="position_uk",
            field=models.CharField(
                help_text="Максимальна довжина тексту: 200 символів.",
                max_length=200,
                null=True,
                verbose_name="Посада",
            ),
        ),
        migrations.AlterField(
            model_name="tender",
            name="title",
            field=models.CharField(
                help_text="Максимальна довжина тексту: 200 символів.",
                max_length=200,
                verbose_name="Назва",
            ),
        ),
        migrations.AlterField(
            model_name="tender",
            name="title_en",
            field=models.CharField(
                help_text="Максимальна довжина тексту: 200 символів.",
                max_length=200,
                null=True,
                verbose_name="Назва",
            ),
        ),
        migrations.AlterField(
            model_name="tender",
            name="title_uk",
            field=models.CharField(
                help_text="Максимальна довжина тексту: 200 символів.",
                max_length=200,
                null=True,
                verbose_name="Назва",
            ),
        ),
    ]
