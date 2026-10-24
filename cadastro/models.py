from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    matricula = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nome


class Diretor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    cpf = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=30,
        default="Pendente"
    )

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name="projetos"
    )

    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="projetos"
    )

    def __str__(self):
        return self.titulo