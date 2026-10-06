"""Finite ambiguous November catalog date checks, no attachment queue."""
from collect import fetch

for name, url in [
    ('google-gemini3-developers.html', 'https://blog.google/technology/developers/gemini-3-developers/'),
    ('google-image-verification.html', 'https://blog.google/technology/ai/ai-image-verification-gemini-app/'),
    ('google-nanobanana-developers.html', 'https://blog.google/technology/developers/gemini-3-pro-image-developers/'),
    ('google-nanobanana.html', 'https://blog.google/technology/ai/nano-banana-pro/'),
    ('google-antigravity.html', 'https://antigravity.google/blog/introducing-google-antigravity'),
]:
    fetch(name, url)
