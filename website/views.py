from django.shortcuts import render
from website.models import Pessoa

# Create your views here.

def index(request):


    if request.method == 'POST':
        pessoa = Pessoa()
        pessoa.nome = request.POST.get('nome')
        pessoa.sobrenome = request.POST.get('sobrenome')
        pessoa.data_nascimento = request.POST.get('data_nascimento')
        pessoa.email = request.POST.get('email')
        pessoa.str_cep = request.POST.get('str_cep')
        pessoa.str_numero = request.POST.get('str_numero')
        pessoa.complemento = request.POST.get('complemento')
        pessoa.genero = request.POST.get('genero')
        pessoa.telefone = request.POST.get('telefone')
        pessoa.celular = request.POST.get('celular')
        pessoa.motivo = request.POST.get('motivo')
        pessoa.save()

        contexto = {
            'nome': pessoa.nome
        }
        return render(request, 'index.html', contexto)

    return render(request, 'index.html')



def ong(request):

    if request.method == 'POST':
        Ong = Ong()
        Ong.Responsavel = request.POST.get('Responsavel')
        Ong.Nome = request.POST.get('Nome')
        Ong.Endereço = request.POST.get('Endereço')
        Ong.Telefone = request.POST.get('Telefone')
        Ong.Horario = request.POST.get('Horario de Atendimento')
        Ong.Data = request.POST.get('Data de Funcionamento')

        contexto = {
            'nome': Ong.Responsavel
        }
        return render(request, 'cadastrar.html', contexto)


    return render(request, 'cadastrar.html')

