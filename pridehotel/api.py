from rest_framework import routers
from app.views import *

router=routers.DefaultRouter()
router.register(r"category", CategoryView, basename="category")
router.register(r"rooms", RoomsView, basename="rooms")
router.register(r"bookroom", BookRoomView, basename="bookroom")
router.register(r"contact", ContactView, basename="contact")
