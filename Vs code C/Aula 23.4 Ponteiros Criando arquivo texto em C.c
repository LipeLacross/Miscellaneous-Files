#include <stdio.h>
#include <stdlib.h>

/*----------------------------------------------------------------
Sintaxe:
FILE *<nome_ponteiro> 
*/
int main()
{
    // criando a variável ponteiro para o arquivo
    FILE *ponteiroarquivo;
    //FILE é escrito com letras maiúsculas

    //Sintaxe para abrir o arquivo:
    //*<ponteiro> = fopen("<nome do arquivo>", "<tipo de abertura>");
    ponteiroarquivo = fopen("Arquivo.txt", "a");
    //Depois de aberto, realizamos as operações necessárias e fechamos o arquivo.

    /*Tipos de abertura de arquivos
    r: Permissão de abertura somente para leitura. 
    É necessário que o arquivo já esteja presente no disco.

    w: Permissão de abertura para escrita (gravação). 
    Este código cria o arquivo caso ele não exista, 
    e caso o mesmo exista ele recria o arquivo novamente 
    fazendo com que o conteúdo seja perdido. 
    Portanto devemos tomar muito cuidado ao usar esse tipo de abertura.
    //sobrepõe todo o conteúdo

    a: Permissão para abrir um arquivo texto para escrita(gravação), 
    permite acrescentar novos dados ao final do arquivo. 
    Caso não exista, ele será criado.
    //serve para adicionar mais conteúdo para os dados já existentes
    */

    //Sintaxe para fechar o arquivo:
    //fclose(<nome_ponteiro>);
    fclose(ponteiroarquivo);
    

    printf("O arquivo foi criado com sucesso!\n");

    return 0;
}