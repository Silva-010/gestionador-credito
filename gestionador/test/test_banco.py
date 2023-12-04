import pytest
from apps.banco.models import Banco

@pytest.mark.django_db
def test_banco_creation():
    banco = Banco.objects.create(
        nombre='sadasd',
        direccion='asdasd 123',
        telefono='+56228159862'
    )
    assert banco.nombre == 'sadasd'

@pytest.mark.django_db
def test_banco_str_method():
    banco = Banco.objects.create(
        nombre='Banco de Prueba',
        direccion='Dirección de prueba',
        telefono='+56228159862'
    )
    assert str(banco) == 'Banco de Prueba'

@pytest.mark.django_db
def test_banco_natural_key():
    banco = Banco.objects.create(
        nombre='Banco de Prueba',
        direccion='Dirección de prueba',
        telefono='+56228159862'
    )
    assert banco.natural_key() == ('Banco de Prueba',)

@pytest.mark.django_db
def test_banco_verbose_name():
    assert Banco._meta.verbose_name == 'Banco'

@pytest.mark.django_db
def test_banco_verbose_name_plural():
    assert Banco._meta.verbose_name_plural == 'Bancos'

@pytest.mark.django_db
def test_banco_ordering():
    # Agrega varios bancos con nombres específicos para probar el ordenamiento
    Banco.objects.create(nombre='Banco C')
    Banco.objects.create(nombre='Banco A')
    Banco.objects.create(nombre='Banco B')
    
    bancos = Banco.objects.all()
    assert [banco.nombre for banco in bancos] == ['Banco A', 'Banco B', 'Banco C']
