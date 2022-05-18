from django.db import models

<<<<<<< Updated upstream
# Create your models here.
=======
gol = [('blue', 'BLUE'), ('green', 'GREEN'), ('black', 'BLACK')]


class Clientes(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)



Estados = (('Pa', 'Pará'), ('MG', 'Minas Gerais'), ('SP', 'São Paulo'))


class Frete(models.Model):
    nome_empresa = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    estado = models.CharField(max_length=2, choices=Estados)
    data_entrega = models.DateField()
    # clientes = models.ForeignKey(Clientes, on_delete=models.CASCADE)


class Produto(models.Model):
    frete = models.ForeignKey(Frete, on_delete=models.CASCADE)
    nome_produto = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField()


class Order(models.Model):
    client = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)


class ItemOrder(models.Model):
    order = models.ForeignKey('Order', on_delete=models.PROTECT)
    product = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
>>>>>>> Stashed changes
