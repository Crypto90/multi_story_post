from instagrapi import Client
import os

# --- Config ---
USERNAME = "USERNAME"
PASSWORD = "PASSWORD"
IMAGE_FILENAME = "story.png"  # image in the same folder
HIGHLIGHT_NAME = "Streamplan"  # highlight name to update

def login():
    cl = Client()
    cl.login(USERNAME, PASSWORD)
    return cl

def upload_story(cl, image_path):
    print("Uploading story...")
    media = cl.photo_upload_to_story(image_path)
    return media

def update_highlight(cl, highlight_name, media):
    print("Updating story highlight...")
    highlights = cl.highlight_user_feed(cl.user_id)
    target_highlight = None
    for h in highlights:
        if h.title == highlight_name:
            target_highlight = h
            break

    if target_highlight:
        # Replace with new story (you can also append instead of replace)
        cl.highlight_edit(
            highlight_id=target_highlight.pk,
            cover=media.pk,
            title=highlight_name,
            media=[media.pk]
        )
    else:
        # Create a new highlight
        cl.highlight_create(title=highlight_name, media=[media.pk])

def main():
    image_path = os.path.join(os.path.dirname(__file__), IMAGE_FILENAME)
    cl = login()
    media = upload_story(cl, image_path)
    update_highlight(cl, HIGHLIGHT_NAME, media)

if __name__ == "__main__":
    main()
