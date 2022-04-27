from common.models import CommonCategory


class Category(CommonCategory):

    class Meta:
        app_label = "event"
        verbose_name = "Categorie de l'expérience"




class AccessibilityCategory(CommonCategory):

    class Meta:
        app_label = "event"
        verbose_name = "Categorie accésibilité de l'expérience"
