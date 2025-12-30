import os
import discord
from key import get
from datetime import datetime, timedelta

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)
TOKEN = get('TOKEN')

@client.event
async def on_ready():
    print(f'{client.user} está online!')

@client.event
async def on_message(message):
    conteudo = message.content
    l_conteudo = conteudo.lower()

    if message.author == client.user:
        return

    if l_conteudo.startswith('!invite'):
        await message.channel.send(f'LINK DE CONVITE')
    
    if l_conteudo.startswith('!telegram'):
        await message.channel.send(f'https://t.me/+2Oo4v98hHyZiNDYx')

    if l_conteudo.startswith('!pendrive'):
        await message.channel.send(f'https://t.me/+WJBJONu-t0oyM2Mx')

    if l_conteudo.startswith('!engenharia'):
        await message.channel.send(f'https://drive.google.com/drive/folders/1dTydzQcB3eezRkf2LdaKt37fxLLH2Ds2')

    if l_conteudo.startswith('!python'):
        await message.channel.send(f'https://t.me/+0oqdXpK1cl0yNjEx')

    if l_conteudo.startswith('!java'):
        await message.channel.send(f'https://t.me/+ibUWnieEWsszNmI5')

    if l_conteudo.startswith('!iniciante'):
        await message.channel.send(f'https://t.me/+BXiALlbmnlo5ZTkx')

    if l_conteudo.startswith('!linux'):
        await message.channel.send(f'https://t.me/+d4P_9InAfyMzYjcx')

    if l_conteudo.startswith('!mentoria'):
        await message.channel.send(f'https://t.me/+RoEkVjqIahY2NjJh')

    if l_conteudo.startswith('!intermediario'):
        await message.channel.send(f'https://t.me/+1w2XdCG8w38wNThh')

    if l_conteudo.startswith('!avancado'):
        await message.channel.send(f'https://t.me/+RaVQGYLVXjxlYTIx')

    if l_conteudo.startswith('!mentoria'):
        await message.channel.send(f'https://t.me/+DWOudRhMumg0OGIx')

    if l_conteudo.startswith('!vps'):
        await message.channel.send(f'https://t.me/+iTGHYTFUEzQ5ODhi')

    if l_conteudo.startswith('!ethical'):
        await message.channel.send(f'https://t.me/+4wesoXdCBfo3OTMx')
    
    if l_conteudo.startswith('!email'):
        await message.channel.send(f"""
Email Anonim- http://anonimjjzzccjgmxgowzgbp3eocjljdxz2lban7ozwmdrudopezvugqd.onion/
                                   
NULL Message - http://74b3as5fsvxirkrzxbzukugry5la56ilhsqa4yzwhw7bevcydc22tlid.onion/
                                   
Panz Mail- http://panzvbljmqb5j2tznnal2aavx2zz7pob3wamueloi6uukrh4v4u6jfad.onion/
                                   
Tormail- http://tormailpout6wplxlrkkhjj2ra7bmqaij5iptdmhhnnep3r6f27m2yid.onion/
""")   
    
    if l_conteudo.startswith('!foruns5'):
        await message.channel.send(f"""
DarkZone Forum- http://darkobds5j7xpsncsexzwhzaotyc4sshuiby3wtxslq5jy2mhrulnzad.onion/darkzone-forum/

RuDark- http://rudarkznow3mhg6kdbwvvpkzsupjfgrt6id5hae53fdm5iikf77t4pid.onion/cgi-bin/rudark/YaBB.pl

Def Con Forums- https://ezdhgsy2aw7zg54z6dqsutrduhl22moami5zv2zt6urr6vub7gs6wfad.onion/

Cebulka- http://cebulka7uxchnbpvmqapg5pfos4ngaxglsktzvha7a5rigndghvadeyd.onion/index.php

Def Con- http://g7ejphhubv5idbbu3hb3wawrs5adw7tkx7yjabnf65xtzztgg4hcsqqd.onion/

Libre Forum- http://libreeunomyly6ot7kspglmbd5cvlkogib6rozy43r2glatc6rmwauqd.onion

Bunker- http://bunkerapkk334hqopst6ur63mrjs4ls25z22x4telrvo5yn3c3llk3ad.onion/

The Stock Insiders- http://thestock6nonb74owd6utzh4vld3xsf2n2fwxpwywjgq7maj47mvwmid.onion/

Poast- http://6x7g7rr6fhdoszolkqkaittdr6qzgejjxoc42q4ceaph2xttmo5vgryd.onion/

Suprbay- http://suprbaydvdcaynfo4dgdzgxb4zuso7rftlil5yg5kqjefnw4wq4ulcad.onion

XSS.is- http://xssforumv3isucukbxhdhwz67hoa5e2voakcfkuieq4ch257vsburuid.onion/

Breaking Bad- http://6tn2ejdphoveywwt6pc2sbaez62bytq4vr4xd2f2b6mrffhzakrcvbid.onion/

Le Monde Parallèle- http://lmpv2xoglvgh6ty6ymh2vww3gamfq5x3myk3gu7qzck7klcftf4s4lyd.onion/

Diaspora social- http://diasporg5tj4xz5mxkd5qnrppo7tbb6ynk2gtmjw5lmz6mtbesj3k6id.onion/
""")

    if l_conteudo.startswith('!foruns4'):
        await message.channel.send(f"""
Медицинская марихуана в Украине- http://weedmedpolea3sn7yrrg6f624rlracg4iqzft7trkro262gqzvnj7bqd.onion/

Форум независимой Республики Сибирь- https://axxa63ucb43pyn2f7wvd3qg5cijz62dunsno5ukqaigfv6xucuqnctyd.onion/

Sanctioned Suicide- http://suicidabvrputryeg3mxdwwtwnv3eqj2koztuaiko5zn5rzodtencnad.onion/

Raddle- http://c32zjeghcp5tj3kb72pltz56piei66drc63vkhn5yixiyk4cmerrjtid.onion/

Runion- http://runionv3do7jdylpx7ufc6qkmygehsiuichjcstpj4hb2ycqrnmp67ad.onion/

Ramble- http://rambleeeqrhty6s5jgefdfdtc6tfgg4jj6svr4jpgk4wjtg3qshwbaad.onion/

0Day- http://zerodayhukmtc56zualcmtvtto5xfz7gytgt7poxgkmgegnq34p3xcyd.onion/

RedFace- http://wzxwaen2zhuouiirspgpaw7hjvlzini5bfmopb6e45mkj5exbzzossad.onion/

OnniForums- http://onnii6niq53gv3rvjpi7z5axkasurk2x5w5lwliep4qyeb2azagxn4qd.onion/

Abyss Forum- http://qyvjopwdgjq52ehsx6paonv2ophy3p4ivfkul4svcaw6qxlzsaboyjid.onion/
""")

    if l_conteudo.startswith('!foruns3'):
        await message.channel.send(f"""
Mazafaka- http://uwovoq3luqdzqkuy5ynjl3lxh2gqbib2ceb77kcbr47ww4oyqyiahuid.onion/index.php

Exploit.IN- https://exploitivzcm5dawzhe6c32bbylyggbjvh5dyvsvb5lkuz5ptmunkmqd.onion/

Consulado- http://vwstizqo6omfamnlmzrb7ypj5yda6cqqy4kmtvhmp3z5ewl5ellqcvad.onion/

Germania- http://germania7zs27fu3gi76wlr5rd64cc2yjexyzvrbm4jufk7pibrpizad.onion/

Dread- http://g66ol3eb5ujdckzqqfmjsbpdjufmjd5nsgdipvxmsh7rckzlhywlzlqd.onion/

Cosa Nostra- http://conosqsj6lyh52toau47tjpxcsccan6l3kakrpm2ox73vcf674d7a6id.onion/

Russian DarkNet Hub- http://4n6enyz6oenoaqtmchbvippilm5zilps4apudlhw3ei7mcstzmj56fyd.onion/

The Green Machine- http://vw5vzi62xqhihghvonatid7imut2rkgiudl3xomj4jftlmanuwh4r2qd.onion/

Форум Дубликат- http://dublikateyrxbx2wzsoi6bkfp3pso5npxgqqklkjt22rbbmo5vmpxzad.onion/

Криминальный форум- http://b45aqyhwqsnnr7ljygvdwhlsmzhxsevaab2au6hvroasyhxbxw6q4ayd.onion/
""")

    if l_conteudo.startswith('!foruns2'):
        await message.channel.send(f"""
Dark Web Forums- http://dwforumuugiyderhybcpfxmlmoawgq6z3w6hk45nrnem3p7kwszhybad.onion/

Dark Net Army Forum- http://darknet77vonbqeatfsnawm5jtnoci5z22mxay6cizmoucgmz52mwyad.onion/

Onion Gun Forum- http://oniongunutp6jfdhkgvsaucuunp4b7kqmbeeo5nxbxtnfxptlaxotmid.onion/

BreachForums- http://breachedu76kdyavc6szj6ppbplfqoz3pgrk3zw57my4vybgblpfeayd.onion/

Crime Network- http://cnw4acab23przeum6ios6pw63ivxxbrvpclz5yssflkos6ano6oq4fqd.onion/

CryptBB- http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/

Verified- http://verified3vr2kdbnza6c3e5ak4z5xmtti4hx36dfg3kbi6pwekztvsqd.onion/

Jungsforum- http://jungsmj4w5z7jpoy4e5q5lj4csn3gmektmaflbvfv47syygfdxpbblad.onion/

Balkanchan- http://26yukmkrhmhfg6alc56oexe7bcrokv4rilwpfwgh2u6bsbkddu55h4ad.onion/

Russian Community- http://commudazrdyhbullltfdy222krfjhoqzizks5ejmocpft3ijtxq5khqd.onion/
""")

    if l_conteudo.startswith('!foruns1'):
        await message.channel.send(f"""
French Pool- http://jkie5viyrmymttownlksylz5vipyxxvs6qgy2yybgbssoiuf7a7klpqd.onion/

Refuge Forum- http://refuge3noitqegmmjericvur54ihyj7tsfyfwdblitaeaqu2koi7iuqd.onion/

AnonGTS- http://eux4gt4qcaiesps5w5rppxcenoe5shapwycums5yuiikmc4mpc74gpyd.onion/

BHF.EE- http://bhf2b5nb3lb2kxpaoyqz7cuk2dkgej5n2refuffxzyhldwt4d7de4zqd.onion/

TorForum- http://torbuyxpe6auueywlctu4wz6ur3o5n2meybt6tyi4rmeudtjsysayqyd.onion/forum/

HackTown- http://hacktowns3sba2xavxecm23aoocvzciaxirh3vekg2ovzdjgjxedfvqd.onion/home.php

Klos Forum- http://forums.kaizushih5iec2mxohpvbt5uaapqdnbluaasa2cmsrrjtwrbx46cnaid.onion/

DarkTalk- http://324jrpzofcssslvsurr4nemwsfikxezmryeeiuoykyzr2j3tu6a4fpad.onion/

CryptOlympe- http://olympeeeuqr2oxanzkntviwyivyxzo7w2xbeyqy2o2mv6usxanmpy7id.onion/

Cryptostorm's Community Forum- http://coqhgexmcthsuirhll6guwtvtdsu46wbygd6go6g74u5grekwrt6jtyd.onion/
""")

    if l_conteudo.startswith('!info'):
        await message.channel.send(f"""
Este Bot foi criado na intenção de ser apenas mais um bot qualquer para divertir o servidor, aqui está alguns comando que ele é capaz de fazer.

!invite - Manda o link de convite
!info - Informações sobre o bot e comandos disponíveis
!email - Lista de E-mails temporários
!telegram - Telegram para conhecimento
!pendrive - Curso sobre Pendrive Hacker
!ethical - Curso Ethical Hacking e Penetration Testing
!engenharia - Curso sobre Engenharia social
!vps - Curso sobre Administração de Servidor VPS
!linux - Curso Formação Linux Completa
!web - Curso Web Hacking na Pratica 2.0
!python - Curso Python
!java - Curso Java
!iniciante - Curso Iniciante Black Rat Pro
!intermediario - Curso Intermediário Black Rat Pro
!avancado - Curso Avançado Black Rat Pro
!mentoria - Mentoria curso Black Rat Pro
!foruns1 - Lista de fóruns 1
!foruns2 - Lista de fóruns 2
!foruns3 - Lista de fóruns 3
!foruns4 - Lista de fóruns 4
!foruns5 - Lista de fóruns 5
!userinfo - Exibe informações sobre o usuário
!clear - Limpa mensagens (Admin apenas)
!ban - Bane um usuário (Admin apenas)
!deletar - Deleta todos os canais do server (Admin apenas)
!raid - Raid no servidor (Admin apenas)
!kick - Expulsa um usuário (Admin apenas)
!mute - Silencia um usuário (Admin apenas)
!unmute - Remove o silêncio de um usuário (Admin apenas)
!removercargos - Remove todos os cargos (Admin apenas)
""")

    if l_conteudo.startswith('!deletar'):
        if message.author.guild_permissions.administrator:
            try:
                for channel in message.guild.channels:
                    await channel.delete()
                
                await message.guild.create_text_channel('Chat-Geral')
                await message.guild.create_voice_channel('Call 1')
                
                # Envia mensagem no novo canal criado
                general = discord.utils.get(message.guild.channels, name='Chat-Geral')
                if general:
                    await general.send("Todos os canais foram deletados e novos canais foram criados!")
            except Exception as e:
                print(f"Erro ao deletar canais: {e}")
        else:
            await message.channel.send(f"{message.author.mention}, você não tem permissão para executar esse comando.")
    
    if l_conteudo.startswith('!raid'):
        if message.author.guild_permissions.administrator:
            try:
                for channel in message.guild.channels:
                    if isinstance(channel, discord.TextChannel):
                        await channel.delete()
                    if isinstance(channel, discord.VoiceChannel):
                        await channel.delete()
                for _ in range(50):
                    new_channel = await message.guild.create_voice_channel('всемогущий esteve aqui !!!')
                    new_channel = await message.guild.create_text_channel('всемогущий esteve aqui !!!')
                    for _ in range(1):
                        await new_channel.send("""
Server deletado com sucesso!

Nunca mexa com quem não deve !!!


@everyone @here
""")
            except Exception as e:
                print(f"Erro no raid: {e}")
        else:
            await message.channel.send(f"{message.author.mention}, você não tem permissão para executar esse comando.")

    if l_conteudo.startswith('!userinfo'):
        try:
            user = message.mentions[0] if message.mentions else message.author
            await message.channel.send(f'Nome: {user.name}\nID: {user.id}\nStatus: {user.status}\nEntrou em: {user.joined_at}')
        except Exception as e:
            await message.channel.send('Erro ao buscar informações do usuário.')

    if l_conteudo.startswith('!clear'):
        if message.author.guild_permissions.manage_messages:
            args = l_conteudo.split()
            if len(args) == 2 and args[1].isdigit():
                count = int(args[1])
                await message.channel.purge(limit=count + 1)
                await message.channel.send(f'{count} mensagens apagadas!', delete_after=5)
            else:
                await message.channel.send('Uso: !clear <número de mensagens>', delete_after=5)
        else:
            await message.channel.send(f'{message.author.mention}, você não tem permissão para executar esse comando.')

    if l_conteudo.startswith('!ban'):
        if message.author.guild_permissions.ban_members:
            try:
                if not message.mentions:
                    await message.channel.send('Você precisa mencionar um usuário para banir.')
                    return
                user = message.mentions[0]
                await message.guild.ban(user)
                await message.channel.send(f'{user.name} foi banido.')
            except Exception as e:
                await message.channel.send('Erro ao banir usuário.')
        else:
            await message.channel.send(f'{message.author.mention}, você não tem permissão para executar esse comando.')

    if l_conteudo.startswith('!kick'):
        if message.author.guild_permissions.kick_members:
            try:
                if not message.mentions:
                    await message.channel.send('Você precisa mencionar um usuário para expulsar.')
                    return
                user = message.mentions[0]
                await message.guild.kick(user)
                await message.channel.send(f'{user.name} foi expulso.')
            except Exception as e:
                await message.channel.send('Erro ao expulsar usuário.')
        else:
            await message.channel.send(f'{message.author.mention}, você não tem permissão para executar esse comando.')

    if l_conteudo.startswith('!mute'):
        if message.author.guild_permissions.manage_roles:
            try:
                if not message.mentions:
                    await message.channel.send('Você precisa mencionar um usuário para silenciar.')
                    return
                user = message.mentions[0]
                role = discord.utils.get(message.guild.roles, name='Muted')
                if not role:
                    role = await message.guild.create_role(name='Muted')
                    for channel in message.guild.channels:
                        await channel.set_permissions(role, speak=False, send_messages=False)
                await user.add_roles(role)
                await message.channel.send(f'{user.name} foi silenciado.')
            except Exception as e:
                await message.channel.send('Erro ao silenciar usuário.')
        else:
            await message.channel.send(f'{message.author.mention}, você não tem permissão para executar esse comando.')

    if l_conteudo.startswith('!unmute'):
        if message.author.guild_permissions.manage_roles:
            try:
                if not message.mentions:
                    await message.channel.send('Você precisa mencionar um usuário para remover o silêncio.')
                    return
                user = message.mentions[0]
                role = discord.utils.get(message.guild.roles, name='Muted')
                if role:
                    await user.remove_roles(role)
                    await message.channel.send(f'{user.name} teve o silêncio removido.')
                else:
                    await message.channel.send('O cargo "Muted" não existe.')
            except Exception as e:
                await message.channel.send('Erro ao remover silêncio do usuário.')
        else:
            await message.channel.send(f'{message.author.mention}, você não tem permissão para executar esse comando.')

    if l_conteudo.startswith('tomalerda'):
        try:
            now = datetime.utcnow()
            start_of_day = datetime(now.year, now.month, now.day)

            def is_user_message(msg):
                msg_time = msg.created_at.replace(tzinfo=None)
                return msg.author == message.author and msg_time >= start_of_day

            deleted = await message.channel.purge(limit=None, check=is_user_message)
        except Exception as e:
            print(f"Erro ao deletar mensagens: {e}")
    
    if l_conteudo.startswith('!removercargos'):
        if message.author.guild_permissions.administrator:
            try:
                for role in message.guild.roles:
                    if role.name != "@everyone":
                        await role.delete()
                await message.channel.send("Todos os cargos foram removidos!")
            except Exception as e:
                await message.channel.send('Erro ao remover cargos.')
        else:
            await message.channel.send(f"{message.author.mention}, você não tem permissão para executar esse comando.")

client.run(TOKEN)
