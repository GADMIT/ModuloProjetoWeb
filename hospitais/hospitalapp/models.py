from django.db import models
from PIL import Image

# Create your models here
class Hospital(models.Model):
    """Representa a entidade hospital"""
    nome_hospital = models.CharField(max_length=200)
    foto = models.ImageField(null=True, blank=True)
    desc_hospital = models.TextField
    tipo_hospital = models.CharField(max_length=200)
    conceito_hospital = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
    	super().save(*args, **kwargs)
    	im = Image.open(self.foto.path)
    	novo_tamanho = (100, 100)
    	im.thumbnail(novo_tamanho)
    	im.save(self.foto.path)
    	



    def foto_url(self):
    	if self.foto and hasattr(self.foto, 'url'):
    		print("a url da foto é: ", self.foto.url)
    		return self.foto.url
    	else:
    		return "/static/img/img/hosp04.jpg"
    	

    def __str__(self):
        """retorna uma representação de uma string do modelo"""

        return self.nome_hospital