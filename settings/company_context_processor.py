from .models import Company


def get_company(request):
    company=Company.objects.last()
    return{'company':company}