from django.db import models

class Photo(models.Model):
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание", blank=True)
    image_caption = models.CharField("Подпись", max_length=100, blank=True)
    image = models.ImageField("Изображение", upload_to="photos/%Y/%m")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title