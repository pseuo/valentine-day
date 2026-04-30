import os

import pyperclip
from PIL import Image, ImageOps


source_dir = 'origin_images'
target_dir = 'images'
threshold = 1.5 * 1024 * 1024
quality = 80
supported_exts = ('.jpg', '.jpeg', '.png', '.webp')


def get_image_files(directory):
  image_files = []
  for root, _, filenames in os.walk(directory):
    for filename in filenames:
      if filename.lower().endswith(supported_exts):
        image_files.append(os.path.join(root, filename))
  return image_files


def get_save_options(ext, filesize):
  if filesize < threshold:
    return {}

  if ext in ('.jpg', '.jpeg', '.webp'):
    return {'quality': quality, 'optimize': True}
  if ext == '.png':
    return {'optimize': True}
  return {}


if not os.path.isdir(source_dir):
  raise SystemExit(f'Source directory does not exist: {source_dir}')

os.makedirs(target_dir, exist_ok=True)

output_paths = []
filenames = get_image_files(source_dir)

for filename in filenames:
  relative_path = os.path.relpath(filename, source_dir)
  output_filename = os.path.join(target_dir, relative_path)
  output_dir = os.path.dirname(output_filename)
  if output_dir:
    os.makedirs(output_dir, exist_ok=True)

  filesize = os.path.getsize(filename)
  ext = os.path.splitext(output_filename)[1].lower()
  save_options = get_save_options(ext, filesize)

  print('output_filename:', output_filename)
  if save_options:
    print('compressed:', filename)

  with Image.open(filename) as im:
    im = ImageOps.exif_transpose(im)
    if ext in ('.jpg', '.jpeg') and im.mode in ('RGBA', 'LA', 'P'):
      im = im.convert('RGB')
    im.save(output_filename, **save_options)

  output_paths.append('"' + output_filename.replace('\\', '/') + '"')

clipboard_text = ','.join(output_paths)
print(clipboard_text)

try:
  pyperclip.copy(clipboard_text)
except pyperclip.PyperclipException as error:
  print('copy failed:', error)
