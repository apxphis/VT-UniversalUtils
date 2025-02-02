# quote.py

# this extension lets users react to messages and send them to a quote channel!
# note: important that the mods set this up to send to their specified quotes channel
from interactions import Extension, listen, slash_command, slash_option, OptionType, SlashContext, Embed

class Quotes(Extension):
    # command to set up the quotes channel
    @slash_command(name="setquotechannel", description="please input the channel id of the designated channel for quotes", group_name="quotes", group_description="commands for quotes!")
    @slash_option(
        name="channelID",
        description="input the channel ID",
        required=True,
        opt_type=OptionType.INTEGER
    )
    async def setquotechannel(self, ctx: SlashContext, channelID):
        channel = await self.client.fetch_channel(channelID)

        if type(channelID) is not int:
            await ctx.send("input was not a correct integer! try again")
        else:
            await ctx.send(f"channel for quotes was set to {str(channelID)}, sending a message to test!") # if you input the wrong ID, don't worry! copy the channel ID for the right channel and run it again
            channel.send("this is a test message!")
    @slash_command(name="quote", description="Quote a message.", group_name="quotes")
    @slash_option(
        name="message_id",
        description="The ID of the message to quote",
        opt_type=OptionType.STRING,
        required=True
    )
    async def quote_message(self, ctx: SlashContext, message_id: str):
        if self.quote_channel_id is None:
            await ctx.send("please set the quotes channel first using /setquotechannel!")
            return

        try:
            # Convert message_id to int if it's a number, otherwise leave as string
            try:
                message_id = int(message_id)
            except ValueError:
                pass

            channel = await self.client.fetch_channel(ctx.channel_id) # Get the channel the command was used in
            message = await channel.fetch_message(message_id) # Get the message

            quote_channel = await self.client.fetch_channel(self.quote_channel_id)
            embed = Embed(title="Quote", description=message.content, color=0x00ff00) # Example Embed
            embed.set_author(name=message.author.name, icon_url=message.author.avatar.url)
            await quote_channel.send(embed=embed)
            await ctx.send("Message quoted!")

        except Exception as e:
            await ctx.send(f"Error quoting message: {e}")