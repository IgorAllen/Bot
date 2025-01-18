import random
import discord
from discord.ext import commands

# Configuração do bot
TOKEN = 'Datum'  # Substitua pelo token do seu bot
PREFIX = '!'  # Prefixo para os comandos do bot

bot = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.default())

# Evento para indicar que o bot está online
@bot.event
async def on_ready():
    print(f"{bot.user.name} está online e pronto para rolar dados!")

# Comando para rolar dados
@bot.command(name='rolar')
async def rolar_dado(ctx, tipo_dado: str):
    try:
        # Verifica se o formato está correto (ex: 1d20, 2d6)
        quantidade, faces = map(int, tipo_dado.lower().split('d'))
        
        if quantidade <= 0 or faces <= 0:
            await ctx.send("Por favor, insira valores positivos para a quantidade e as faces do dado.")
            return

        # Rola os dados e calcula o total
        resultados = [random.randint(1, faces) for _ in range(quantidade)]
        total = sum(resultados)

        # Envia o resultado no chat
        await ctx.send(f"🎲 Rolando {quantidade}d{faces}: {resultados} \nTotal: {total}")

    except ValueError:
        await ctx.send("Formato inválido! Use o formato 'XdY', onde X é a quantidade de dados e Y o número de faces (ex: 1d20, 2d6).")

# Inicia o bot
bot.run(TOKEN)
