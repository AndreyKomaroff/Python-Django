import instaloader 

il = instaloader.Instaloader()
profile = instaloader.Profile.from_username(il.context, "trainer.kamarooff")

print(f'Profile info:\n{profile.biography}\nPosts count: {profile.mediacount}\nHashtags: {profile.has_highlight_reels}')