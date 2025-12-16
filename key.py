def get(key):
    """
    Função para obter o token do bot Discord.
    
    INSTRUÇÕES:
    1. Substitua 'SEU_TOKEN_AQUI' pelo token real do seu bot
    2. Para obter o token:
       - Acesse https://discord.com/developers/applications
       - Selecione seu aplicativo
       - Vá em "Bot"
       - Clique em "Reset Token" e copie o token
    
    ⚠️ IMPORTANTE: Nunca compartilhe este arquivo ou seu token publicamente!
    """
    tokens = {
        'TOKEN': 'SEU_TOKEN_AQUI'
    }
    return tokens.get(key)
