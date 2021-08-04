from django.contrib import admin
from django.db.models import base
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from api.views import ImagemViewSet, ImagePrincipalUrl, FotosAcoesView, TimeVoluntariosView, DepoimentosView, NewsLetterView, NossosDadosView, LocaisTrabalhadosView
from index.views import index

router = routers.DefaultRouter()

router.register('foto-principal', ImagePrincipalUrl, basename='pega-foto-perfil')
router.register('atualiza-foto-principal', ImagemViewSet, basename='atualiza-foto-perfil')

router.register(r'acoes', FotosAcoesView, basename='fotos-acoes')
router.register(r'voluntarios', TimeVoluntariosView, basename='voluntarios')

router.register(r'depoimentos', DepoimentosView, basename='depoimentos')
router.register(r'newsletter', NewsLetterView, basename='newsletter')

router.register(r'nossos-dados', NossosDadosView, basename='nossos-dados')
router.register(r'locais-trabalhados', LocaisTrabalhadosView, basename='locais-trabalhados')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('index.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)