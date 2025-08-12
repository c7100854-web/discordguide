import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load the bot's token from a file named '.env' for security.
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Define the channel ID where the rules message will be sent.
RULES_CHANNEL_ID = 1394330328612470794  # <<< REPLACE THIS WITH YOUR CHANNEL ID

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

class RulesView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="All Games", style=discord.ButtonStyle.primary, custom_id="all_games")
    async def all_games_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        terms_content = (
            "**All Games Guide**\n"
            "\n\n"
            "**1) DM people that have valuable items in the game that you want to hit\n"
            "2) Offer them a crosstrade or some type of trade that will require a middleman\n"
            "3) Once you get your crosstrade, convince them to use middleman for the trade\n"
            "4) Invite them to this server and create a ticket in ⁠https://discord.com/channels/1384957255878709328/1394330241257963590\n"
            "5) A Middleman will claim your ticket (they'll know you're a hitter from your role) and then scam the victim for their items.\n"
            "6) You and the Middleman will split the hit 50/50 or the MM can choose to give you 100% **"
        )
        await interaction.response.send_message(terms_content, ephemeral=True)

    @discord.ui.button(label="Mm2", style=discord.ButtonStyle.primary, custom_id="mm2")
    async def mm2_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        terms_content = (
            "**There are 2 methods to hit mm2:**\n\n"

            "**1) Multi Trade Scam**\n"
            "This scam happens when a trader offers multiple items in exchange for several of your items in one big trade. "
            "For example, they might offer their Harvester for your 20 Turkeys all at once. "
            "Because the trade involves many items, you will need to use a middleman.\n\n"

            "**2) Crosstrading Scam**\n"
            "In this scam, you offer them real money, or items from other games in exchange for their mm2 items."
        )
        await interaction.response.send_message(terms_content, ephemeral=True)

    @discord.ui.button(label="Adopt Me", style=discord.ButtonStyle.primary, custom_id="adopt_me")
    async def adopt_me_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        terms_content = (
            "**How to hit using Crosstrade in Adopt Me**\n\n"

            "You offer Robux, cash, or items from another game (MM2, PSX, Grow A Garden, etc.) for someone’s Adopt Me pets, "
            "then flip the situation once they trust you.\n\n"

            "**Here’s how you hit:**\n"
            "• Start by saying something like:\n"
            " – “I’ll give you 1k Robux for your Neon Frost”\n\n"
            "• To gain trust, tell them we’ll use a middleman\n\n"
            "• Make the deal seem urgent:\n"
            " – “Only doing one more trade today”\n"
            " – “This Robux offer is limited, gotta move quick”\n\n"
            "• Because it’s off-platform and cross-game, they can’t do anything. No proof, no support.\n\n"
            "🔒 They trusted the “middleman” plan, and you flipped it. Clean hit.\n\n"
            "✅ Best targets: new players, kids who want Robux, or people greedy for cross-game value\n\n"
            "🎭 Bonus tip: If they start doubting, act offended or say “I’ve been scammed before too, that’s why we’re using a mm” — it lowers their guard."
        )
        await interaction.response.send_message(terms_content, ephemeral=True)

    @discord.ui.button(label="Bladeball", style=discord.ButtonStyle.primary, custom_id="bladeball")
    async def bladeball_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        terms_content = (
            "**How to hit Blade Ball players using crosstrade**\n\n"

            "Target players with clean inventories — rare slashes, kill FX, or limited items. "
            "You act like you're trading robux/money, Adopt Me, MM2, PSX, or other game items for their Blade Ball stuff.\n\n"

            "**Here’s the method step-by-step:**\n"
            "• Find a victim with value (good slash skins, rare kill FX, limiteds like Lightning Slash, Duality, etc.)\n"
            "• Slide in and say:\n"
            " – “Wanna trade for your Lightning? I got Adopt Me pets”\n"
            " – “I’ll give MM2 godlies for your FX/Slash skin”\n"
            "• To build trust, say:\n"
            " – “We’ll use a middleman if you want”\n"
            " – Or “I’ve done crosstrades before, check my vouches” (use fake ones)\n"
            "• Push them to use our middleman — since Blade Ball has no real crosstrade system, you need them to trust your word\n"
            "• There’s no system in-game to track or reverse the hit — it’s done\n\n"
            "🧠 Bonus: You don’t need to offer Robux or money. Just use fake Adopt Me pets, MM2 trash, or PSX basics — they don’t know the value.\n\n"
            "🎭 Pressure tactics:\n"
            " – “I’ve been scammed before too, that’s why I use a mm”\n"
            " – “You’re getting overpaid, this is fair”\n"
            " – “Don’t waste my time if you’re scared, I’m legit”\n\n"
            "✅ Cleanest hits: kids with stacked BB inventories and no clue about other game values\n\n"
            "❌ They think cross-trading items = safe, but there’s no trade window between games. All trust-based = all hittable."
        )
        await interaction.response.send_message(terms_content, ephemeral=True)

    @discord.ui.button(label="Account Steal", style=discord.ButtonStyle.primary, custom_id="account_steal")
    async def account_steal_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        terms_content = (
            "**Middlemanning Accounts**\n"
            "A guide!\n\n"

            "**First step: Securing the account**\n"
            "Make sure 2fa is disabled beforehand. Remove number, add your new email, change password. "
            "The user will receive an email stating to revert. There are 2 methods to counter this:\n\n"

            "**Adding Authenticator**\n"
            "Authenticator blocks it so when you try to revert it asks for Auth code, which YOU have. It is pretty good method.\n\n"

            "**What if I don't have authenticator? Email method**\n"
            "This method is way more easy. First, add an alt mail. While you are doing that, tell the user to wait or make up an excuse. "
            "Add a second mail; this second mail will cancel his revert and you can transfer it back to your main.\n\n"
            "**Note:** DO NOT CLICK THE REVERT OPTION SENT TO YOUR ALT MAIL. IF YOU CLICK, THE USER WILL BE ELIGIBLE TO REVERT! ALWAYS MANUALLY RE-ADD.\n\n"

            "**Underage Account**\n"
            "This method is 100% working. The only downside is the account must not be VC Verified.\n\n"
            "Disable 2FA and all that. What you wanna do is put a birthdate that's under 13 but turning 13 in a few days. "
            "For example, in 2024 people who were born in 2011 — you put their date. Example: If the date is October 1st, you make it Oct 3rd 2011 "
            "and within 2 days the account will be 13+. Making acc underage removes email completely ensuring there's no revert. "
            "This is the best method so far, however only works with unverified VC accounts.\n\n"

            "**After account has been secured**, add 2fa, email, and phone # (if needed).\n\n"
            "If it’s an acc with a valuable item on it, immediately trade the item to your ALT (or an acc you don’t care about) and find a buyer for $$$ "
            "before the item gets rolled back. This is called a *Poisoned Limited*. To avoid getting scammed, sell it or trade it as fast as you can.\n\n"
            "**Check if the item is poisoned or clean:** https://trades.roblox.com/docs/index.html (w/ trade id)"
        )
        await interaction.response.send_message(terms_content, ephemeral=True)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    rules_channel = client.get_channel(RULES_CHANNEL_ID)
    if rules_channel:
        rules_embed = discord.Embed(
            title="**Guide on how to hit !**",
            description="",
            color=discord.Color.green()  # This sets the left line color to green
        )
        rules_embed.set_footer(text="Made by sully")
        await rules_channel.send(embed=rules_embed, view=RulesView())
        print("Rules message sent successfully!")
    else:
        print(f"Error: Could not find channel with ID {RULES_CHANNEL_ID}.")

client.run(DISCORD_TOKEN)
