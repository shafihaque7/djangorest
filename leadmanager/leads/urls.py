from rest_framework import routers
from .api import LeadViewSet,SalaryViewSet, ParadigmViewset, LanguageViewset, ProgrammerViewset

router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'leads')
router.register('api/salary', SalaryViewSet, 'salary')
router.register('api/paradigm', ParadigmViewset, 'paradigm')
router.register('api/language', LanguageViewset, 'language')
router.register('api/programmer', ProgrammerViewset, 'programmer')

urlpatterns = router.urls