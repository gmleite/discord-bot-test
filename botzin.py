import discord
from discord.ext import commands
import random
import json
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)
try:
    client = commands.Bot(command_prefix='?')
    chvs = ['HOA', 'MOTS', 'PF', 'TOP', 'DOS', 'SOA', 'NW', 'SD']


    ####################SALVAR AS CHAVES QDO EU DESLIGO O PC XD?####################
    def json_chvs(chaves_disponiveis, caminho='savechaves.json'):
        with open(caminho, 'w') as arquivo:
            json.dump(chaves_disponiveis, arquivo, default=_chvs_para_json)
            
    def _chvs_para_json(chaves_disponiveis):
        return chaves_disponiveis.__dict__

    #####puxa as chaves do arquivo json
    def chvs_json(caminho='savechaves.json'):
        chaves_disponiveis = {}
        with open(caminho) as arquivo:
            chaves_disponiveis = json.load(arquivo)
            
        return chaves_disponiveis

    ####retornar as chaves qdo ligar o bot de novo
    chaves_disponiveis = {}
    chaves_disponiveis = chvs_json()


    @client.event
    async def on_ready():
        print('Bot online')


    @client.command()
    async def ping(ctx):
        await ctx.send(f'{round(client.latency * 1000)}ms', delete_after=5)


    @client.command()
    async def addplayer(ctx, player, chave):
        player = player.lower()
        chaves_disponiveis.update({player: chave})
        json_chvs(chaves_disponiveis)
        await ctx.send(f'{player.capitalize()} adicionado com chave {chave.capitalize()}', delete_after=5)
        
    ###capitalize é só visual pra mensagem###
    ###json_chvs atualiza o arquivo pra qql mudança nas chaves


    @client.command()
    async def attplayer(ctx, player, chave):
        player = player.lower()
        chaves_disponiveis.update({player: chave})
        json_chvs(chaves_disponiveis)
        await ctx.send(f'Chave atualizada para {player.capitalize()}, {chave.capitalize()}.', delete_after=5)
    ###json_chvs atualiza o arquivo pra qql mudança nas chaves


    @client.command()
    async def chave(ctx, player):
        player = player.lower()
        await ctx.send(f'Player: {player.capitalize()}, Chave: {chaves_disponiveis[player]}', delete_after=5)

    @client.command()
    async def chaves(ctx):
        await ctx.channel.purge(limit=50)

        for i, z in chaves_disponiveis.items():
            await ctx.send(f'`{i.capitalize()}, {z.capitalize()}`')


    @client.command()
    async def clear(ctx, amount=1):
        if amount <= 10:
            await ctx.channel.purge(limit=amount)
        else:
            await ctx.send(f'Vai com calma', delete_after=5)

    @client.command()
    async def removerplayer(ctx, player):
        json_chvs(chaves_disponiveis, 'savekeysbackup.json')
        if player == 'all':
            chaves_disponiveis.clear
            json_chvs(chaves_disponiveis)
            await ctx.send(f'Todos os players removidos.', delete_after=5)
        else:
            chaves_disponiveis.pop(player)
            json_chvs(chaves_disponiveis)
            await ctx.send(f'{player.capitalize()} removido.', delete_after=5)
    ### remove player do bot atual e do arquivo de save

    @client.command()
    async def comandos(ctx):
        await ctx.author.send("""Comandos disponiveis:
    ?addplayer Nome Chave-nivel
    ?attplayer Nome Chave-nivel
    ?chave Nome (Retorna a Chave do Player)
    ?chaves (Retorna todas as chaves)
    ?removerplayer Nome (Remove da lista, se usar "all" limpa a lista inteira)
    ?clear numero (Limpa um numero de mensagens, máximo 10 por vez)."""  )
    ###responde no privado

    @client.event
    async def on_message(message):
        if message.content.startswith('?'):
            await message.delete(delay=5)
            await client.process_commands(message)
        ### deleta a mensagem de comando dps de executar ele 


    client.run('ODEzNTE4NDUyMDQ4Mzk2MzE4.YDQeGQ.nTooRVj_Tjq8MONrYBVUqdK7Yqg')
except Exception as e:
    logging.exception('Erro inesperado: %s', e)










