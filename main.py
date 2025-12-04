import asyncio
import os

from dotenv import load_dotenv

from bot.bot import Bot


async def main():
    load_dotenv()
    bot = Bot()
    await bot.load_cogs()
    token = os.environ.get("DISCORD_TOKEN")
    if token is None:
        print("Error: DISCORD_TOKEN not found in environment variables.")
        return

    token = token.strip()
    if not token:
        print("Error: DISCORD_TOKEN is empty.")
        return

    print(f"Token loaded: {len(token)} characters")
    print(f"Token prefix: {token[:10]}...")

    # Check if it's likely a bot token (should start with specific pattern)
    if not any(token.startswith(prefix) for prefix in ["Bot ", "MTk", "Nz", "OD"]):
        print("Warning: Token doesn't appear to be a valid bot token format.")
        print("Make sure you're using a BOT token from Discord Developer Portal,")
        print("not a user token. Bot tokens typically start with 'MTk', 'Nz', or 'OD'.")

    try:
        print("Attempting to connect to Discord...")
        await bot.start(token)
    except Exception as e:
        print("\nFailed to connect to Discord:")
        print(f"  Error Type: {type(e).__name__}")
        print(f"  Error Message: {e}")
        print("\nPossible causes:")
        print("  1. Invalid bot token")
        print("  2. Network/firewall blocking Discord")
        print("  3. Bot token revoked or disabled")
        print("  4. Proxy or VPN interfering with connection")
        await bot.close()


if __name__ == "__main__":
    asyncio.run(main())
