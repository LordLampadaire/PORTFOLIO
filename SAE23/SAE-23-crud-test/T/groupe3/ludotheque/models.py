# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

# -*- coding: utf-8 -*-
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_even(value):
    if not (0<=value<=10):
        raise ValidationError(
            _('%(value)s n\'est pas compris entre 0 et 10 (bornes incluses)'),
            params={'value': value},
        )


TYPE_PROFIL = (
        ('Professionnel','Professionnel'),
        ('Particulier','Particulier'),
    )

class Editeur(models.Model):
    # idediteur = models.AutoField(db_column='idEditeur', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(max_length=45)
    date = models.DateField(blank=True, null=True)
    logo = models.URLField(blank=True)

    def __str__(self):
        return f"{self.nom}"

    def dico(self):
        return {"nom": self.nom, "date": self.date, "logo": self.logo}


class Categorie(models.Model):
    # idcategorie = models.AutoField(db_column='idCategorie', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(max_length=45)
    description = models.TextField()

    def __str__(self):
        return f"{self.nom}"

    def dico(self):
        return {"nom": self.nom, "description": self.description}



class Jeux(models.Model):
    # idjeux = models.AutoField(db_column='idJeux', primary_key=True)  # Field name made lowercase.
    editeur = models.ForeignKey(Editeur, on_delete=models.CASCADE, db_column='Jeux_idEditeur', default=None)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, db_column='Categorie_idCategorie',
                                  default=1)  # Field name made lowercase.
    titre = models.CharField(max_length=45)
    date_sortie = models.CharField(max_length=45)
    photo = models.URLField(blank=True)

    def __str__(self):
        return f"{self.titre}"

    def dico(self):
        return {"titre": self.titre, "date_sortie": self.date_sortie, "photo": self.photo, "categorie": self.categorie, "editeur": self.editeur}


class Joueur(models.Model):
    # idjoueur = models.AutoField(db_column='idJoueur', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(max_length=45)
    prenom = models.CharField(max_length=45)
    mail = models.EmailField(help_text='A valid email address, please.')
    mdp = models.CharField(max_length=45)
    type = models.CharField(max_length=15, verbose_name="Type", choices=TYPE_PROFIL, default='PARTICULIER')


    def __str__(self):
        return f"{self.nom} {self.prenom}"

    def dico(self):
        return {"nom": self.nom, "prenom": self.prenom, "mail": self.mail, "mdp": self.mdp, "type": self.type}

    @classmethod
    def recup_option(cls):
        return dict(cls.TYPE_PROFIL).get(cls.type)

class Commentaire(models.Model):
    # idcommentaire = models.AutoField(db_column='idCommentaire', primary_key=True)  # Field name made lowercase.
    jeu = models.ForeignKey(Jeux, on_delete=models.CASCADE)
    joueur = models.ForeignKey(Joueur, on_delete=models.CASCADE)
    note = models.PositiveIntegerField(default=0, validators=[validate_even])
    commentaire = models.TextField()
    date = models.DateField()
    #jeux_idjeux = models.ForeignKey('Jeux', models.DO_NOTHING, db_column='Jeux_idJeux')  # Field name made lowercase.

    def __str__(self):
        return f"{self.commentaire}"

    def dico(self):
        return {"note": self.note, "commentaire": self.commentaire, "date": self.date}



class JeuxhasEditeur(models.Model):
    jeu = models.ForeignKey(Jeux, on_delete=models.CASCADE)
    editeur = models.ForeignKey(Editeur, on_delete=models.CASCADE)

