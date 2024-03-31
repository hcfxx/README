import discord
from discord.ext import commands

# Botun prefix'i
prefix = "!"

# Botun niyetleri (intents)
intents = discord.Intents.default()

# Botun tanımlanması
bot = commands.Bot(command_prefix=prefix, intents=intents)

# Hesaplama komutu
@bot.command()
async def hesapla(ctx, arac_fiyati: float, motor_yuzde_kaybi: float):
    sabit_deger = 0.00497
    sonuc = arac_fiyati * sabit_deger * motor_yuzde_kaybi
    sonuc = max(sonuc, 10000)
    sonuc = round(sonuc / 1000) * 1000
    await ctx.send(f"Sonuc: ${sonuc:,.2f}")

# Botun hazır olduğunda gönderilecek mesaj
@bot.event
async def on_ready():
    print(f'{bot.user.name} is ready.')

# Botun çalıştırılması
bot.run('MTIyNDA1ODY1MTkzODEyNzk0NA.GCGpFF.MPACY4iqRHSfq3Xw-7jrJUIOVjSgFNyErzlF7M')
