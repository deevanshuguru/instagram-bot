from instagrapi.types import StoryMention, StoryMedia
from instagrapi.story import StoryBuilder

media_pk = cl.media_pk_from_url('https://www.instagram.com/p/CTA31aPj3IH/')
media_path = cl.video_download(media_pk)
adw0rd = cl.user_info_by_username('deevanshu_guru')

buildout = StoryBuilder(
    media_path,
    'Credits @deevanshu_guru',
    [StoryMention(user=deevanshu_guru)],
    Path('/path/to/background_720x1280.jpg')
).video(15)  # seconds

cl.video_upload_to_story(
    buildout.path,
    "Credits @deevanshu_guru",
    mentions=buildout.mentions,
    links=[StoryLink(webUri='https://github.com/MagmaCray/instagram-bot')],
    medias=[StoryMedia(media_pk=media_pk)]
)
