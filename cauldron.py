import pynbt
from pynbt import TAG_Int
from PIL import Image
import os

INPUT_STRUCTURE = "cauldron.mcstructure"
OUTPUT_STRUCTURE = "cauldron_colored.mcstructure"
INPUT_IMAGE = "image.png"

WIDTH = 64
HEIGHT = 64


def bgra_to_signed_int(b, g, r, a):
    """Convert BGRA color components to a signed 32-bit integer as used by Minecraft."""
    value = (b & 0xFF) | ((g & 0xFF) << 8) | ((r & 0xFF) << 16) | ((a & 0xFF) << 24)
    if value >= 0x80000000:
        value -= 0x100000000
    return value


def main():

    if not os.path.exists(INPUT_STRUCTURE):
        print("Error: cauldron.mcstructure not found.")
        return

    if not os.path.exists(INPUT_IMAGE):
        print("Error: image.png not found.")
        return

    img = Image.open(INPUT_IMAGE).convert("RGB")

    if img.size != (WIDTH, HEIGHT):
        print("Error: Image must be 64x64 pixels.")
        return

    pixels = list(img.getdata())

    # Read the template structure
    structure = pynbt.NBTFile(open(INPUT_STRUCTURE, "rb"), little_endian=True)

    block_data = structure["structure"]["palette"]["default"]["block_position_data"]

    for i in range(WIDTH * HEIGHT):

        key = str(i)

        if key not in block_data:
            continue

        entity = block_data[key]["block_entity_data"]
        x = i % WIDTH
        y = i // WIDTH

        # Mirror horizontally because the structure coordinates are reversed
        mirror_x = WIDTH - 1 - x

        r, g, b = pixels[y * WIDTH + mirror_x]

        color = bgra_to_signed_int(b, g, r, 255)

        entity["CustomColor"] = TAG_Int(color)

    structure.save(open(OUTPUT_STRUCTURE, "wb"), little_endian=True)

    print("Done:", OUTPUT_STRUCTURE)


if __name__ == "__main__":
    main()
