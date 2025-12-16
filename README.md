# Bot Discord - Black Rat Pro

Bot Discord criado para compartilhar recursos educacionais, cursos e links úteis relacionados a segurança da informação, programação e comunidades técnicas.

## 📋 Requisitos

- Python 3.8 ou superior
- Biblioteca discord.py
- Conta Discord
- Bot Discord criado no [Discord Developer Portal](https://discord.com/developers/applications)

## 🚀 Instalação

### 1. Clone ou baixe este repositório

```bash
git clone <seu-repositorio>
cd <pasta-do-bot>
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Configure o Token do Bot

Você precisa criar um arquivo `key.py` na mesma pasta do bot com o seguinte conteúdo:

```python
def get(key):
    tokens = {
        'TOKEN': 'SEU_TOKEN_AQUI'
    }
    return tokens.get(key)
```

**⚠️ IMPORTANTE:** Substitua `SEU_TOKEN_AQUI` pelo token do seu bot Discord.

#### Como obter o token do bot:

1. Acesse o [Discord Developer Portal](https://discord.com/developers/applications)
2. Clique no seu aplicativo (ou crie um novo)
3. Vá em "Bot" no menu lateral
4. Clique em "Reset Token" e copie o token gerado
5. Cole o token no arquivo `key.py`

### 4. Configure o Link de Convite

No arquivo `bot.py`, encontre a linha:

```python
if l_conteudo.startswith('!invite'):
    await message.channel.send(f'LINK DE CONVITE')
```

Substitua `LINK DE CONVITE` pelo link de convite do seu bot. Para gerar o link:

1. No Discord Developer Portal, vá em "OAuth2" > "URL Generator"
2. Selecione o escopo `bot`
3. Selecione as permissões necessárias (recomendado: Administrator ou as permissões específicas que você precisa)
4. Copie o link gerado e cole no código

### 5. Execute o Bot

```bash
python bot.py
```

Se tudo estiver correto, você verá a mensagem:
```
<nome-do-bot> está online!
```

## 📝 Comandos Disponíveis

### Comandos de Informação
- `!invite` - Manda o link de convite do bot
- `!info` - Informações sobre o bot e comandos disponíveis
- `!email` - Lista de E-mails temporários
- `!userinfo` - Exibe informações sobre o usuário (ou mencione alguém)

### Comandos de Recursos/Cursos
- `!telegram` - Telegram para conhecimento
- `!pendrive` - Curso sobre Pendrive Hacker
- `!ethical` - Curso Ethical Hacking e Penetration Testing
- `!engenharia` - Curso sobre Engenharia social
- `!vps` - Curso sobre Administração de Servidor VPS
- `!linux` - Curso Formação Linux Completa
- `!web` - Curso Web Hacking na Pratica 2.0
- `!python` - Curso Python
- `!java` - Curso Java
- `!iniciante` - Curso Iniciante Black Rat Pro
- `!intermediario` - Curso Intermediário Black Rat Pro
- `!avancado` - Curso Avançado Black Rat Pro
- `!mentoria` - Mentoria curso Black Rat Pro

### Comandos de Fóruns
- `!foruns1` - Lista de fóruns 1
- `!foruns2` - Lista de fóruns 2
- `!foruns3` - Lista de fóruns 3
- `!foruns4` - Lista de fóruns 4
- `!foruns5` - Lista de fóruns 5

### Comandos de Moderação (Admin apenas)
- `!clear <número>` - Limpa um número específico de mensagens
- `!ban @usuário` - Bane um usuário do servidor
- `!kick @usuário` - Expulsa um usuário do servidor
- `!mute @usuário` - Silencia um usuário
- `!unmute @usuário` - Remove o silêncio de um usuário
- `!deletar` - Deleta todos os canais do servidor e cria novos
- `!raid` - Executa raid no servidor (uso extremo)
- `!removercargos` - Remove todos os cargos do servidor

## ⚙️ Configuração de Intents

O bot utiliza as seguintes intents do Discord:
- `message_content` - Para ler o conteúdo das mensagens
- `members` - Para acessar informações dos membros

Certifique-se de habilitar estas intents no Discord Developer Portal:
1. Vá em "Bot" no menu lateral
2. Role até "Privileged Gateway Intents"
3. Ative "MESSAGE CONTENT INTENT" e "SERVER MEMBERS INTENT"

## ⚠️ Avisos Importantes

1. **Segurança do Token**: Nunca compartilhe seu token do bot publicamente. Mantenha o arquivo `key.py` em `.gitignore` se for usar controle de versão.

2. **Comandos Destrutivos**: Os comandos `!deletar`, `!raid` e `!removercargos` são extremamente destrutivos e devem ser usados com muito cuidado. Eles podem causar danos irreversíveis ao servidor.

3. **Permissões**: Para que os comandos administrativos funcionem, o bot precisa ter as permissões adequadas no servidor.

4. **Uso Responsável**: Este bot foi criado para fins educacionais. Use-o de forma responsável e ética.

## 🔧 Estrutura de Arquivos

```
.
├── bot.py              # Código principal do bot
├── key.py              # Arquivo com o token (criar manualmente)
├── requirements.txt    # Dependências do projeto
└── README.md          # Este arquivo
```

## 🐛 Solução de Problemas

### Bot não inicia
- Verifique se o token está correto no arquivo `key.py`
- Certifique-se de que todas as dependências estão instaladas
- Verifique se as intents estão habilitadas no Developer Portal

### Comandos não funcionam
- Verifique se o bot tem as permissões necessárias no servidor
- Confirme que as intents estão habilitadas
- Verifique os logs de erro no terminal

### Erros de permissão
- Certifique-se de que o bot tem as permissões adequadas para executar os comandos
- Verifique a hierarquia de cargos no servidor (o cargo do bot deve estar acima dos cargos que ele gerencia)

## 📄 Licença

Este projeto é fornecido "como está", sem garantias de qualquer tipo.

## 🤝 Contribuições

Sinta-se livre para melhorar este bot e compartilhar suas modificações!

---

**Desenvolvido para fins educacionais e de estudo em segurança da informação.**
