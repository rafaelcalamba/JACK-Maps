#!/usr/bin/env python
 
from gimpfu import *
 
def convert_gs_texture(imagecount, w, h):
  while imagecount > 0:
    imagecount -= 1
    image = gimp.image_list()[imagecount]
    pdb.gimp_image_scale(image, w, h)
    pdb.gimp_image_resize_to_layers(image)
    if pdb.gimp_image_get_precision(image) != 150:
      pdb.gimp_image_convert_precision(image, 150)
    pdb.gimp_image_convert_indexed(image, 0, 0, 256, 0, 1, "")
 
register(
  "python-fu-convert-gs-texture",
  "Converts image to a GoldSrc texture",
  "Converts image to indexed color 8-bit gamma integer",
  "Rafael Calamba",
  "Rafael Calamba",
  "2020",
  "Convert to GoldSrc texture",
  "",
  [
  (PF_INT, "imagecount", "Image Count", "1"),
  (PF_INT, "w", "Width", "256"),
  (PF_INT, "h", "Height", "256")
  ],
  [],
  convert_gs_texture, menu="<Image>/Image")
 
main()