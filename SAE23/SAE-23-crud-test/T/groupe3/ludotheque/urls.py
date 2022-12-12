from django.urls import path
from . import views



urlpatterns = [
    path('main/', views.index),
    path('mainjeu/', views.indexjeu),

    path("jeu/ajoutjeu/", views.ajoutjeux),
    path("jeu/traitementjeu", views.traitementjeu),
    path('jeu/affichejeu/<int:id>/', views.affichejeu),
    path('jeu/updatejeu/<int:id>/', views.updatejeu),
    path('jeu/traitementupdatejeu/<int:id>', views.traitementupdatejeu),
    path('jeu/deletejeu/<int:id>/', views.deletejeu),

    path("categorie/ajoutcatego/", views.ajoutcategorie),
    path("categorie/traitementcatego", views.traitementcategorie),
    path('categorie/affichecatego/<int:id>/', views.affichecategorie),
    path('categorie/updatecatego/<int:id>/', views.updatecategorie),
    path('categorie/traitementupdatecatego/<int:id>', views.traitementupdatecategorie),
    path('categorie/deletecatego/<int:id>/', views.deletecategorie),

    path("joueur/ajoutjoueur/", views.ajoutjoueur),
    path("joueur/traitementjoueur", views.traitementjoueur),
    path('joueur/affichejoueur/<int:id>/', views.affichejoueur),
    path('joueur/updatejoueur/<int:id>/', views.updatejoueur),
    path('joueur/traitementupdatejoueur/<int:id>', views.traitementupdatejoueur),
    path('joueur/deletejoueur/<int:id>/', views.deletejoueur),

    path("editeur/ajoutediteur/", views.ajoutediteur),
    path("editeur/traitementediteur", views.traitementediteur),
    path('editeur/afficheediteur/<int:id>/', views.afficheediteur),
    path('editeur/updateediteur/<int:id>/', views.updateediteur),
    path('editeur/traitementupdateediteur/<int:id>', views.traitementupdateediteur),
    path('editeur/deleteediteur/<int:id>/', views.deleteediteur),

    path("commentaire/ajoutcommentaire/", views.ajoutcom),
    path("commentaire/traitementcommentaire", views.traitementcom),
    path('commentaire/affichecommentaire/<int:id>/', views.affichecommentaire),
    path('commentaire/updatecommentaire/<int:id>/', views.updatecommentaire),
    path('commentaire/traitementupdatecommentaire/<int:id>', views.traitementupdatecommentaire),
    path('commentaire/deletecommentaire/<int:id>/', views.deletecommentaire),
]
