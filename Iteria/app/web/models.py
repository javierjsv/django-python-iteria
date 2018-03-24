# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class usuario (models.Model):
    idUsuario = models.IntegerField(primary_key=True)
    correo = models.CharField(max_length=45)
    documento = models.CharField(max_length=45)
    fech_creacion = models.DateField(auto_now_add=True)
    fech_actualizacion = models.DateField(auto_now_add=True)

    def nombre (self):
        cadena = "{0},{1}"
        return cadena.format(self.idUsuario, self.documento)

    def __str__(self):
        return self.nombre()
    


class estado (models.Model):
    idEstado = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)
    fech_creacion = models.DateField(auto_now_add=True)
    fech_actualizacion = models.DateField(auto_now_add=True)


    def estado (self):
        cadena = "{0},{1}"
        return cadena.format(self.idEstado, self.nombre)

    def __str__(self):
        return self.estado()



class sesion (models.Model):
    idSesion = models.IntegerField(primary_key=True)
    dispocitivo = models.CharField(max_length=45)
    usuario_idUsuario = models.ForeignKey(usuario, null=False, blank=False, on_delete=models.CASCADE)
    fech_creacion = models.DateField(auto_now_add=True)
    fech_actualizacion = models.DateField(auto_now_add=True)
    estado_idEstado = models.ForeignKey(estado, null=False, blank=False, on_delete=models.CASCADE)



    def sesion (self):
        cadena = "{0},{1},{2}"
        return cadena.format(self.idSesion, self.usuario_idUsuario, self.estado_idEstado)

    def __str__(self):
        return self.sesion()



class rol (models.Model):
    idRol = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    fech_creacion = models.DateField(auto_now_add=True)
    fech_actualizacion = models.DateField(auto_now_add=True)

    def rol (self):
        cadena = "{0},{1}"
        return cadena.format(self.idRol, self.nombre)

    def __str__(self):
        return self.rol()



class rol_user (models.Model):
    idRol_User = models.IntegerField(primary_key=True)
    rol_idRol = models.ForeignKey(rol, null=False, blank=False, on_delete=models.CASCADE)
    usuario_idUsuario = models.ForeignKey(usuario, null=False, blank=False, on_delete=models.CASCADE)
    fech_creacion = models.DateField(auto_now_add=True)
    fech_actualizacion = models.DateField(auto_now_add=True)


    def UserRol (self):
        cadena = "{0},{1}"
        return cadena.format(self.rol_idRol, self.usuario_idUsuario)

    def __str__(self):
        return self.UserRol()



class permisos (models.Model):
    idPermisos = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    fech_creacion = models.DateField(auto_now_add=True)
    fech_actualizacion = models.DateField(auto_now_add=True)

    def permisos (self):
        cadena = "{0},{1}"
        return cadena.format(self.idPermisos, self.nombre)

    def __str__(self):
        return self.permisos()

class rol_permiso (models.Model):
    idRol_permiso = models.IntegerField(primary_key=True)
    permisos_idPermiso = models.ForeignKey(permisos, null=False, blank=False, on_delete=models.CASCADE)
    idRol_idRol = models.ForeignKey(rol, null=False, blank=False, on_delete=models.CASCADE)
    fech_creacion = models.DateField(auto_now_add=True)
    fech_actualizacion = models.DateField(auto_now_add=True)

    def permisoRol (self):
        cadena = "{0},{1}{2}"
        return cadena.format(self.idRol_permiso, self.permisos_idPermiso, self.idRol_idRol)

    def __str__(self):
        return self.permisoRol()


