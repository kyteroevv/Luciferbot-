# This plugin is part of the Cipher Elite Telegram UserBot
# Author: Rishabh (https://github.com/rishabhops)
# License: MIT License — See LICENSE file for full text

from telethon import events, errors
from telethon.tl.functions.channels import EditBannedRequest, EditAdminRequest, LeaveChannelRequest
from telethon.tl.functions.messages import UpdatePinnedMessageRequest
from telethon.tl.functions.phone import CreateGroupCallRequest
from telethon.tl.types import ChatBannedRights, ChatAdminRights
from plugins.bot import add_handler
from utils.utils import CipherElite
from utils.decorators import rishabh

def init(client_instance):
    commands = [
        ".ban - Ban a user from the group",
        ".unban - Unban a user from the group",
        ".kick - Kick a user from the group",
        ".mute - Mute a user in the group",
        ".unmute - Unmute a user in the group",
        ".promote - Promote a user to admin",
        ".demote - Remove admin rights from a user",
        ".pin - Pin a message in the group",
        ".unpin - Unpin a message in the group",
        ".purge - Delete messages in bulk by replying",
        ".vc - Start a group voice chat (Owner Only)",
        ".leave - Leave the current group (Owner Only)",
        ".tagall - Tag all members in the group (Owner Only)",
        ".zombies - Remove deleted accounts from the group (Owner Only)",
        ".allban - Ban all non-admin members from the group (Mass Ban)"
    ]
    description = "Admin commands for group management 👮‍♂️"
    add_handler("admin", commands, description)

async def register_commands():
    @CipherElite.on(events.NewMessage(pattern=r"\.ban"))
    @rishabh()
    async def ban(event):
        if event.is_reply:
            reply = await event.get_reply_message()
            try:
                await event.client(EditBannedRequest(
                    channel=event.chat_id,
                    user_id=reply.sender_id,
                    banned_rights=ChatBannedRights(until_date=None, view_messages=True)
                ))
                await event.reply("🚫 User has been banned!")
            except errors.RPCError as e:
                await event.reply(f"❌ Failed to ban user: {e.message}")
            except Exception as e:
                await event.reply(f"❌ An error occurred: {str(e)}")

    @CipherElite.on(events.NewMessage(pattern=r"\.unban"))
    @rishabh()
    async def unban(event):
        if event.is_reply:
            reply = await event.get_reply_message()
            try:
                await event.client(EditBannedRequest(
                    channel=event.chat_id,
                    user_id=reply.sender_id,
                    banned_rights=ChatBannedRights(until_date=None, view_messages=False)
                ))
                await event.reply("✅ User has been unbanned!")
            except errors.RPCError as e:
                await event.reply(f"❌ Failed to unban user: {e.message}")
            except Exception as e:
                await event.reply(f"❌ An error occurred: {str(e)}")

    @CipherElite.on(events.NewMessage(pattern=r"\.kick"))
    @rishabh()
    async def kick(event):
        if event.is_reply:
            reply = await event.get_reply_message()
            try:
                await event.client(EditBannedRequest(
                    channel=event.chat_id,
                    user_id=reply.sender_id,
                    banned_rights=ChatBannedRights(until_date=None, view_messages=True)
                ))
                await event.client(EditBannedRequest(
                    channel=event.chat_id,
                    user_id=reply.sender_id,
                    banned_rights=ChatBannedRights(until_date=None, view_messages=False)
                ))
                await event.reply("👢 User has been kicked from the group!")
            except errors.RPCError as e:
                await event.reply(f"❌ Failed to kick user: {e.message}")
            except Exception as e:
                await event.reply(f"❌ An error occurred: {str(e)}")

    @CipherElite.on(events.NewMessage(pattern=r"\.mute"))
    @rishabh()
    async def mute(event):
        if event.is_reply:
            reply = await event.get_reply_message()
            try:
                await event.client(EditBannedRequest(
                    channel=event.chat_id,
                    user_id=reply.sender_id,
                    banned_rights=ChatBannedRights(until_date=None, send_messages=True)
                ))
                await event.reply("🤐 User has been muted!")
            except errors.RPCError as e:
                await event.reply(f"❌ Failed to mute user: {e.message}")
            except Exception as e:
                await event.reply(f"❌ An error occurred: {str(e)}")

    @CipherElite.on(events.NewMessage(pattern=r"\.unmute"))
    @rishabh()
    async def unmute(event):
        if event.is_reply:
            reply = await event.get_reply_message()
            try:
                await event.client(EditBannedRequest(
                    channel=event.chat_id,
                    user_id=reply.sender_id,
                    banned_rights=ChatBannedRights(until_date=None, send_messages=False)
                ))
                await event.reply("🔊 User has been unmuted!")
            except errors.RPCError as e:
                await event.reply(f"❌ Failed to unmute user: {e.message}")
            except Exception as e:
                await event.reply(f"❌ An error occurred: {str(e)}")

    @CipherElite.on(events.NewMessage(pattern=r"\.promote"))
    @rishabh()
    async def promote(event):
        if event.is_reply:
            reply = await event.get_reply_message()
            try:
                admin_rights = ChatAdminRights(
                    change_info=True,
                    post_messages=True,
                    edit_messages=True,
                    delete_messages=True,
                    ban_users=True,
                    invite_users=True,
                    pin_messages=True,
                    add_admins=False
                )
                await event.client(EditAdminRequest(
                    channel=event.chat_id,
                    user_id=reply.sender_id,
                    admin_rights=admin_rights,
                    rank="Admin"
                ))
                await event.reply("👑 User has been promoted to admin!")
            except errors.RPCError as e:
                await event.reply(f"❌ Failed to promote user: {e.message}")
            except Exception as e:
                await event.reply(f"❌ An error occurred: {str(e)}")

    @CipherElite.on(events.NewMessage(pattern=r"\.demote"))
    @rishabh()
    async def demote(event):
        if event.is_reply:
            reply = await event.get_reply_message()
            try:
                empty_rights = ChatAdminRights(
                    change_info=False, post_messages=False, edit_messages=False,
                    delete_messages=False, ban_users=False, invite_users=False,
                    pin_messages=False, add_admins=False
                )
                await event.client(EditAdminRequest(
                    channel=event.chat_id,
                    user_id=reply.sender_id,
                    admin_rights=empty_rights,
                    rank=""
                ))
                await event.reply("⬇️ User has been demoted!")
            except errors.RPCError as e:
                await event.reply(f"❌ Failed to demote user: {e.message}")
            except Exception as e:
                await event.reply(f"❌ An error occurred: {str(e)}")

    @CipherElite.on(events.NewMessage(pattern=r"\.pin"))
    @rishabh()
    async def pin_message(event):
        if event.is_reply:
            try:
                reply = await event.get_reply_message()
                await event.client(UpdatePinnedMessageRequest(
                    peer=event.chat_id,
                    id=reply.id,
                    silent=False
                ))
                await event.reply("📌 Message pinned successfully!")
            except errors.RPCError as e:
                await event.reply(f"❌ Failed to pin message: {e.message}")
            except Exception as e:
                await event.reply(f"❌ An error occurred: {str(e)}")

    @CipherElite.on(events.NewMessage(pattern=r"\.unpin"))
    @rishabh()
    async def unpin_message(event):
        if event.is_reply:
            try:
                reply = await event.get_reply_message()
                await event.client(UpdatePinnedMessageRequest(
                    peer=event.chat_id,
                    id=reply.id,
                    unpin=True
                ))
                await event.reply("📍 Message unpinned successfully!")
            except errors.RPCError as e:
                await event.reply(f"❌ Failed to unpin message: {e.message}")
            except Exception as e:
                await event.reply(f"❌ An error occurred: {str(e)}")

    @CipherElite.on(events.NewMessage(pattern=r"\.purge"))
    @rishabh()
    async def purge(event):
        if not event.is_reply:
            await event.reply("❌ Kisi message par reply karke `.purge` use karein!")
            return
        
        try:
            reply = await event.get_reply_message()
            message_ids = []
            async for msg in event.client.iter_messages(event.chat_id, min_id=reply.id - 1):
                message_ids.append(msg.id)
                if len(message_ids) >= 100:
                    break
            
            if message_ids:
                await event.client.delete_messages(event.chat_id, message_ids)
                await event.delete()
        except errors.RPCError as e:
            await event.reply(f"❌ Failed to purge messages: {e.message}")
        except Exception as e:
            await event.reply(f"❌ An error occurred: {str(e)}")

    @CipherElite.on(events.NewMessage(pattern=r"\.vc"))
    @rishabh()
    async def start_voice_chat(event):
        me = await event.client.get_me()
        if event.sender_id != me.id:
            return

        if not event.is_group:
            await event.reply("❌ Yeh command sirf groups ke andar use ki ja sakti hai!")
            return

        try:
            await event.client(CreateGroupCallRequest(peer=event.chat_id))
            await event.reply("🎙️ Group Voice Chat successfully start ho gayi hai!")
        except errors.RPCError as e:
            await event.reply(f"❌ Voice chat start nahi ho saki: {e.message}")
        except Exception as e:
            await event.reply(f"❌ An error occurred: {str(e)}")

    @CipherElite.on(events.NewMessage(pattern=r"\.leave"))
    @rishabh()
    async def leave_group(event):
        me = await event.client.get_me()
        if event.sender_id != me.id:
            return

        if not event.is_group:
            await event.reply("❌ Yeh command sirf groups ke andar use ki ja sakti hai!")
            return

        try:
            await event.reply("👋 Group choda ja raha hai...")
            await event.client(LeaveChannelRequest(event.chat_id))
        except errors.RPCError as e:
            await event.reply(f"❌ Group leave karne me error aaya: {e.message}")
        except Exception as e:
            await event.reply(f"❌ An error occurred: {str(e)}")

    @CipherElite.on(events.NewMessage(pattern=r"\.tagall"))
    @rishabh()
    async def tagall(event):
        me = await event.client.get_me()
        if event.sender_id != me.id:
            return
        
        if not event.is_group:
            await event.reply("❌ Yeh command sirf groups ke andar use ki ja sakti hai!")
            return

        args = event.text.split(maxsplit=1)
        custom_text = args[1] if len(args) > 1 else "Attention everyone! 🔔"

        await event.delete()
        
        mentions = []
        async for user in event.client.iter_participants(event.chat_id):
            if user.bot or user.deleted:
                continue
            mentions.append(f"[{user.first_name}](tg://user?id={user.id})")
            
            if len(mentions) >= 40:
                text_to_send = f"{custom_text}\n\n" + " ".join(mentions)
                await event.client.send_message(event.chat_id, text_to_send)
                mentions = []

        if mentions:
            text_to_send = f"{custom_text}\n\n" + " ".join(mentions)
            await event.client.send_message(event.chat_id, text_to_send)

    @CipherElite.on(events.NewMessage(pattern=r"\.zombies"))
    @rishabh()
    async def zombies(event):
        me = await event.client.get_me()
        if event.sender_id != me.id:
            return

        if not event.is_group:
            await event.reply("❌ Yeh command sirf groups ke andar use ki ja sakti hai!")
            return

        msg = await event.reply("🔍 Group me deleted accounts (Zombies) dhoonde ja rahe hain...")
        
        zombie_count = 0
        try:
            async for user in event.client.iter_participants(event.chat_id):
                if user.deleted:
                    try:
                        await event.client(EditBannedRequest(
                            channel=event.chat_id,
                            user_id=user.id,
                            banned_rights=ChatBannedRights(until_date=None, view_messages=True)
                        ))
                        await event.client(EditBannedRequest(
                            channel=event.chat_id,
                            user_id=user.id,
                            banned_rights=ChatBannedRights(until_date=None, view_messages=False)
                        ))
                        zombie_count += 1
                    except Exception:
                        pass
            
            await msg.edit(f"✅ Zombie cleanup complete!\nTotal Deleted Accounts Removed: {zombie_count}")
        except Exception as e:
            await msg.edit(f"❌ Zombie cleanup fail ho gaya: {str(e)}")

    @CipherElite.on(events.NewMessage(pattern=r"\.allban"))
    @rishabh()
    async def allban(event):
        me = await event.client.get_me()
        if event.sender_id != me.id:
            return

        if not event.is_group:
            await event.reply("❌ Yeh command sirf groups ke andar use ki ja sakti hai!")
            return

        msg = await event.reply("⚠️ Mass ban process shuru ho raha hai. Non-admin members ban kiye ja rahe hain...")
        
        banned_count = 0
        failed_count = 0
        
        try:
            async for user in event.client.iter_participants(event.chat_id):
                if user.id == me.id:
                    continue
                
                participant = await event.client.get_permissions(event.chat_id, user.id)
                if participant.is_admin or participant.is_creator:
                    continue
                
                try:
                    await event.client(EditBannedRequest(
                        channel=event.chat_id,
                        user_id=user.id,
                        banned_rights=ChatBannedRights(until_date=None, view_messages=True)
                    ))
                    banned_count += 1
                except Exception:
                    failed_count += 1
            
            await msg.edit(f"✅ Mass ban complete!\nSuccessfully Banned: {banned_count}\nFailed: {failed_count}")
        except Exception as e:
            await msg.edit(f"❌ Mass ban process fail ho gaya: {str(e)}")
