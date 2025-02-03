import discord
import json
import asyncio

TOKEN = "DEIN_BOT_TOKEN_HIER"
BACKUP_FILE = "discord_backup.json"

intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.messages = True
intents.guild_messages = True

client = discord.Client(intents=intents)

async def backup_guild(guild):
    """Erstellt ein Backup des Servers als JSON-Datei."""
    backup_data = {
        "server_name": guild.name,
        "server_id": guild.id,
        "channels": [],
        "roles": [],
        "emojis": []
    }
    
    for channel in guild.channels:
        channel_type = "Text" if isinstance(channel, discord.TextChannel) else "Voice" if isinstance(channel, discord.VoiceChannel) else "Category"
        permissions_data = {role.name: {perm[0]: perm[1] for perm in channel.overwrites_for(role) if perm[1] is not None} for role in guild.roles}
        
        backup_data["channels"].append({
            "id": channel.id,
            "name": channel.name,
            "type": channel_type,
            "category": channel.category.name if channel.category else None,
            "position": channel.position,
            "permissions": permissions_data
        })
    
    for role in guild.roles:
        permissions = [perm[0] for perm in role.permissions if perm[1]]
        backup_data["roles"].append({
            "id": role.id,
            "name": role.name,
            "color": str(role.color),
            "position": role.position,
            "permissions": permissions
        })
    
    for emoji in guild.emojis:
        backup_data["emojis"].append({
            "id": emoji.id,
            "name": emoji.name,
            "url": str(emoji.url)
        })
    
    with open(BACKUP_FILE, "w", encoding="utf-8") as f:
        json.dump(backup_data, f, indent=4, ensure_ascii=False)
    print(f"✅ Backup gespeichert: {BACKUP_FILE}")

async def restore_guild(guild):
    """Stellt ein Backup aus der JSON-Datei wieder her."""
    try:
        with open(BACKUP_FILE, "r", encoding="utf-8") as f:
            backup_data = json.load(f)
    except FileNotFoundError:
        print("❌ Keine Backup-Datei gefunden!")
        return
    
    existing_roles = {role.name: role for role in guild.roles}
    
    for role_data in sorted(backup_data["roles"], key=lambda r: r["position"]):
        if role_data["name"] not in existing_roles:
            await guild.create_role(name=role_data["name"], color=discord.Color(int(role_data["color"].replace("#", "0x"), 16)), permissions=discord.Permissions.none())
    
    existing_channels = {channel.name: channel for channel in guild.channels}
    
    for channel_data in backup_data["channels"]:
        if channel_data["name"] not in existing_channels:
            if channel_data["type"] == "Text":
                await guild.create_text_channel(name=channel_data["name"])
            elif channel_data["type"] == "Voice":
                await guild.create_voice_channel(name=channel_data["name"])
            elif channel_data["type"] == "Category":
                await guild.create_category(name=channel_data["name"])
    
    print("✅ Wiederherstellung abgeschlossen!")

@client.event
async def on_ready():
    print(f"Bot {client.user} ist online!")
    for guild in client.guilds:
        print(f"Starte Backup für {guild.name} ({guild.id})")
        await backup_guild(guild)
        # await restore_guild(guild)
    await client.close()

client.run(TOKEN)
