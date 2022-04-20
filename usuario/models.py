from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from tinymce import models as tinymce_models
from .managers import UserManager
from django.urls import reverse

class User(AbstractBaseUser,PermissionsMixin):
    #ID annadida por django por defecto
    nombre = models.CharField(max_length=100,blank=False)
    apellido = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=255, unique= True)
    password = models.CharField(max_length=200)
    imagenPerfil = models.ImageField(upload_to='pfp',default="planky.png",null=True,blank=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre'] #email & password estan por default
    
    objects = UserManager()
    
    @property
    def nombreCompleto(self):
        return '%s %s' % (self.nombre, self.apellido) 


ELECCION_TEMAS = (
    ('Matemáticas',(
        ('Álgebra','Álgebra'),
        ('Geometría','Geometría'),
        ('Cálculo','Cálculo'),
        )
    ),
    ('Español',(
        ('Lectura y Redacción','Lectura y Redacción'),
        ('Literatura','Literatura'),
        )
    ),
    ('Ciencias Naturales',(
        ('Biología','Biología'),
        ('Química','Química'),
        ('Medicina','Medicina'),
        )
    ),
    ('Humanidades',(
        ('Historia','Historia'),
        ('Filosofía','Filosofía'),
        ('Psicología','Psicología'),
        ),
    )
)

#Para no repetir los atributos comunes entre Flashcard y Práctica
class Herramienta(models.Model):
    user = models.ForeignKey(User,null = True, on_delete=models.SET_NULL)
    filtro = models.CharField(choices = ELECCION_TEMAS, max_length=50, default=('Matemáticas',('Álgebra','Álgebra')))
    titulo = models.CharField(max_length=100, blank=False,default='')
    descripcion = models.CharField(max_length=100, blank= False)
    visible = models.BooleanField(default=True)
    voto = models.IntegerField(default=0)
    
    class Meta:
        abstract = True
    
    def __str__(self):
        return self.titulo
    


#Comparte los atributos de herramienta, solo se añade el editor de texto
class Flashcard(Herramienta):
    contenido = tinymce_models.HTMLField()  #Para el editor de texto

    def get_absolute_url(self):
       return reverse("core:documento", kwargs={"id" : self.id})

    
#Comparte los atributos de Herramienta, también sirve para tener la llave primaria 
#para relacionar las preguntas
class Practica(Herramienta):
    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("core:practica", kwargs={"id" : self.id})

    def get_preguntas_abiertas(self):
        preguntas_abiertas = Abierta.objects.filter(practica = self)
        return preguntas_abiertas
    
    def get_preguntas_cerradas(self):
        preguntas_cerradas = Cerrada.objects.filter(practica = self)
        return preguntas_cerradas
    
    def calificar(self):
        pass

#Clase abstracta para los diferentes tipos de preguntas
class Pregunta(models.Model):
    practica = models.ForeignKey(Practica,null=True,on_delete=models.SET_NULL)
    planteamiento = models.CharField(blank=False, max_length=100) 
    respuesta = models.CharField(max_length=100,blank=False)

    def __str__(self) -> str:
        return self.planteamiento

    def classname(obj):
        return obj.__class__.__name__   

    def calificar_pregunta(self, respuesta_usuario):
        if respuesta_usuario == self.respuesta:
            return 1
        else:
            return 0

    class Meta:
        abstract = True

#Clase para definir las preguntas abiertas
class Abierta(Pregunta):
    pass

#Clase solo para tener una primarykey para asociar las respuestas cerradas
class Cerrada(Pregunta):
    def get_respuestas(self):
        respuestas = RespuestaCerrada.objects.filter(id_pregunta = self)
        return respuestas
        
#Clase para definir las respuestas cerradas de una pregunta de tipo Cerrada
#Se hace de esta forma para que el usuario pueda definir "n" respuestas
#Cuenta con la llave foránea de la clase Cerrada para identificar a la clase que pertenecen
class RespuestaCerrada(models.Model):
    es_correcta = models.BooleanField(default=False)
    id_pregunta = models.ForeignKey(Cerrada,null=True,on_delete=models.SET_NULL)
    respuesta = models.CharField(blank=False, max_length=100)