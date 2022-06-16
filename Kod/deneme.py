from PIL import Image, ImageDraw, ImageFont
import os
samplePath = os.path.abspath(os.getcwd()) + '/sample'

sampleFont = ImageFont.truetype('ariblk.ttf', 200)

sonEtiketPath = os.path.abspath(os.getcwd()) + '/son'
sonEtiketFolderContents = os.listdir(sonEtiketPath)
i = 0


for sonEtiketHam in sonEtiketFolderContents:

    with Image.open('son/{}'.format(sonEtiketHam)).convert("RGBA") as base:

        txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
        # get a drawing context
        d = ImageDraw.Draw(txt)

        # draw text, half opacity
        d.text((70, 450), "SAMPLE", font=sampleFont, fill=(255, 0, 0, 150))
        # draw text, full opacity


        out = Image.alpha_composite(base, txt)

        out.save("deneme/hamidiye{}.png".format(i))
        i = i+1