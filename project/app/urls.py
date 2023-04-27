from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("",views.main,name="home"),
    path("taj",views.taj,name="taj"),
    path("aja",views.aja,name="aja"),
    path("elo",views.elo,name="elo"),
    path("jan",views.jan,name="jan"),
    path("khaj",views.khaj,name="khaj"),
    path("qua",views.qua,name="qua"),
    path("red",views.red,name="red"),
    path("sar",views.sar,name="sar"),
    path("sun",views.sun,name="sun"),
    path("tajbook",views.tajbook,name="tajbook"),
    path("ajabook",views.ajabook,name="ajabook"),
    path("elobook",views.elobook,name="elobook"),
    path("janbook",views.janbook,name="janbook"),
    path("khajbook",views.khajbook,name="khajbook"),
    path("quabook",views.quabook,name="quabook"),
    path("redbook",views.redbook,name="redbook"),
    path("sarbook",views.sarbook,name="sarbook"),
    path("sunbook",views.sunbook,name="sunbook"),

    path("gogo",views.gogo,name="gogo"),

    path("database",views.dbms,name="dbms"),
    path('admin/', admin.site.urls),
]
