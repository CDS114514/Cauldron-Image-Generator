### Cauldron Image Generator

This Python tool converts a 64x64 PNG image into a Minecraft Bedrock structure (`cauldron_colored.mcstructure`) that uses the liquid color of cauldrons to display the image.

#### Requirements

- Python 3.x
- Pillow (PIL) library
- PyNBT library

Install the dependencies using pip:

```bash
pip install Pillow pynbt
```

#### Usage

1. Place a **64×64 PNG image** named `image.png` in the same directory as the script.
2. Ensure that the template structure file `cauldron.mcstructure` is present in the same directory. This file contains the base cauldron arrangement and must exist.
3. Run the script:

```bash
python cauldron.py
```

4. Upon successful completion, the script generates a file named `cauldron_colored.mcstructure` (64×64×1). You can import this structure into Minecraft Bedrock Edition using a structure block.

#### How it works

The script reads the input image, flips it horizontally (because the structure layout corresponds to a mirrored view), and assigns each pixel’s color to the corresponding cauldron’s `CustomColor` NBT tag. The resulting structure retains the cauldron blocks but with their liquid color set to the image pixel color.

#### Notes

- The input image must be exactly 64×64 pixels.
- The original `cauldron.mcstructure` file is required as a template.
- The generated structure is a single layer (Y=0) with dimensions 64×64.

