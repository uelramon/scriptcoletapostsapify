🧠 Coleta de Dados do Instagram via Apify
Este repositório contém um script Python para automatizar a coleta de dados de perfis públicos do Instagram utilizando a plataforma Apify. O script lê uma lista de contas a partir de uma planilha, coleta os posts mais recentes de cada conta e salva os dados em arquivos .xlsx.

📌 Funcionalidades
Coleta posts recentes de contas do Instagram.

Usa a API da Apify com autenticação via token.

Suporte para configuração de:

Número máximo de posts por conta

Limite de dias para os posts coletados

Geração de três arquivos de saída:

dados_instagram.xlsx: Dados completos dos posts coletados

resumo_coleta.xlsx: Quantidade de posts por conta

erros_coleta.xlsx: Contas que falharam durante a coleta

⚙️ Pré-requisitos
Python 3.8+

Conta na Apify

Token de acesso à Apify

sessionId de uma conta logada no Instagram

📦 Instalação
Clone o repositório:

bash
Copiar
Editar
git clone https://github.com/seu-usuario/coleta-apify.git
cd coleta-apify
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Crie a planilha contas_instagram.xlsx com uma coluna chamada Contas, contendo os @users a serem coletados.

🛠️ Como usar
Configure os parâmetros dentro do script Coleta_Apify.py:

Insira seu token da Apify em apify_token

Insira seu sessionId do Instagram

Ajuste os limites de posts (LIMITE_POSTS) e dias (LIMITE_DIAS), se necessário

Execute o script:

bash
Copiar
Editar
python Coleta_Apify.py
Os arquivos de saída serão gerados no mesmo diretório.

📁 Estrutura dos Arquivos
Coleta_Apify.py — script principal

contas_instagram.xlsx — entrada com os perfis do Instagram

dados_instagram.xlsx — dados brutos coletados

resumo_coleta.xlsx — quantidade de posts coletados por conta

erros_coleta.xlsx — contas que apresentaram erros

🚨 Observações
O uso do Apify para coletar dados do Instagram pode depender de autenticação válida e está sujeito a limitações da plataforma e da rede social.

Este script é para fins educacionais. Utilize com responsabilidade conforme os Termos de Uso da Apify e do Instagram.

📄 Licença
Este projeto está licenciado sob a MIT License.
