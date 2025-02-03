from interactions import Extension, slash_command, slash_option, OptionType, SlashContext, Embed

class Quotes(Extension):

    convertedID = None

    # command to set up the quotes channel
    @slash_command(name="setquotechannel", description="Please input the channel ID of the designated channel for quotes.")
    @slash_option(
        name="channel_id",
        description="Input the channel ID",
        required=True,
        opt_type=OptionType.STRING
    )
    async def setquotechannel(self, ctx: SlashContext, channel_id: str):
        try:
            self.convertedID = int(channel_id)  # store the channel id as an instanct
            channel = await self.client.fetch_channel(self.convertedID)

            await ctx.send(f"Channel for quotes was set to {self.convertedID}, sending a message to test!")
            await channel.send("This is a test message!")
        except ValueError:
            await ctx.send("Input was not a valid integer! Try again.")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

    # command to quote a message using a message id
    @slash_command(name="quote", description="quote a message :D")
    @slash_option(
        name="message_id",
        description="the ID of the message to quote",
        opt_type=OptionType.STRING,
        required=True
    )
    async def quote_message(self, ctx: SlashContext, message_id: str):
        if self.convertedID is None:
            await ctx.send("please set the quotes channel first using /setquotechannel!")
            return

        try:
            # Convert message_id to int
            message_id = int(message_id)

            # Fetch the message and the quote channel
            channel = await self.client.fetch_channel(ctx.channel_id)
            message = await channel.fetch_message(message_id)
            quote_channel = await self.client.fetch_channel(self.convertedID)

            # Create an embed for the quoted message
            embed = Embed(title="quote", description=message.content, color=0x00FF00)
            embed.set_author(name=message.author.name, icon_url=message.author.avatar.url)

            # Send the embed to the quote channel
            await quote_channel.send(embed=embed)
            await ctx.send("message added to quotes channel!")

        except ValueError:
            await ctx.send("the message ID must be a valid integer!")
        except Exception as e:
            await print(f"error quoting message: {e}")
            await ctx.send("there was an error! tell mevia to look at the console.")