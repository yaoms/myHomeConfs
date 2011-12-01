# Fake feather effect
convert -size 80x60 xc:black \
        -fill white -draw 'rectangle 1,1 78,58' \
        -gaussian 7x15 +matte lomo_mask.png
mogrify -resize 800x600 -gaussian 0x5 lomo_mask.png
# Change contrast and saturation
convert -contrast 120 -modulate 100,120 original.jpg lomo.png
# Compose
composite -compose Multiply lomo_mask.png lomo.png output.png
# Output before/after sample
montage original.jpg output.png -geometry 480x320 -quality 100 montage.jpg
