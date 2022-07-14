#include <stdio.h>
#include <stdlib.h>

struct tp_endereco
{
    char nome;
    int num;
    char email;
    char rua[40];
    char bairro[40];
    char cidade[40];
    char estado[3];
    int cep;
};

struct tp_data_nascimento
{
    int dia;
    int mes;
    int ano;
    struct tp_endereco ender;
};

int main(){
    struct tp_data_nascimento pessoa1;
    pessoa1.dia = 24;
    pessoa1.mes = 8;
    pessoa1.ano = 2001;
    pessoa1.ender.nome;
    pessoa1.ender.bairro;
    pessoa1.ender.cidade;
    pessoa1.ender.estado;
    pessoa1.ender.rua;

    fgets(pessoa1.ender.nome, 40, stdin);
    //strtok(pessoa1.ender.nome, "\n");

    printf("Nome: %s", pessoa1.ender.nome);

    return 0;
}
/*
struct tp_endereco
{
    char nome;
    int num;
    char email;
    char rua[40];
    char bairro[40];
    char cidade[40];
    char estado[3];
    int cep;
};

struct tp_data_nascimento
{
    int dia;
    int mes;
    int ano;
};

struct cad_cliente
{
    char nome_cliente[60];
    int tele;

    struct tp_endereco endereco;

    struct tp_data_nascimento data_nascimento;

} cad_cliente[1];

int main()
{
    //system("clear");
    int i;

    printf("\n\n------- Cadastro dos clientes -------\n\n");

    for (i = 0; i < cad_cliente; i++)
    {
        printf("\n\nNome do cliente................:");
        //fflush(stdin);
        gets(cad_cliente[i].nome_cliente);

        printf("\n\nDigite o telefone do cliente...:");
        scanf("%d", &cad_cliente[i].tele);

        printf("\n\nDigite a rua...................:");
        //fflush(stdin);
        gets(cad_cliente[i].endereco.rua);

        printf("\n\nDigite o numero................:");
        scanf("%d", &cad_cliente[i].endereco.num);

        printf("\n\nBairro.........................:");
        //fflush(stdin);
        gets(cad_cliente[i].endereco.bairro);

        printf("\n\nCidade.........................:");
        //fflush(stdin);
        gets(cad_cliente[i].endereco.cidade);

        printf("\n\nEstado.........................:");
        //fflush(stdin);
        gets(cad_cliente[i].endereco.estado);

        printf("\n\nDigite o CEP...................:");
        scanf("%d", &cad_cliente[i].endereco.cep);

        printf("\n\nDia de nascimento..............:");
        scanf("%d", &cad_cliente[i].data_nascimento.dia);

        printf("\n\nMes de nascimento..............:");
        scanf("%d", &cad_cliente[i].data_nascimento.mes);

        printf("\n\nAno de nascimento..............:");
        scanf("%d", &cad_cliente[i].data_nascimento.ano);
    }
    printf("\n\n--------Dadosdosclientes --------\n\n");

    for (i = 0; i < 2; i++)
    {
        printf("\n Nome............: %s", cad_cliente[i].nome_cliente);
        printf("\n Rua.............: %s", cad_cliente[i].endereco.rua);
        printf("\n Numero..........: %s", cad_cliente[i].endereco.num);
        printf("\n Bairro..........: %s", cad_cliente[i].endereco.bairro);
        printf("\n Cidade..........: %s", cad_cliente[i].endereco.cidade);
        printf("\n Estado..........: %s", cad_cliente[i].endereco.estado);
        printf("\n Cep.............: %s", cad_cliente[i].endereco.cep);

        printf("\n Dia de nasc:%d", cad_cliente[i].data_nascimento.dia);
        printf("\n Mes de nasc:%d", cad_cliente[i].data_nascimento.mes);
        printf("\n Ano de nasc:%d", cad_cliente[i].data_nascimento.ano);
    }

    return 0;
}
*/