![Taco Banner](./assets/taco-banner.png)

**Taco** is a simple command-line tool designed to **mass-convert** images to the WebP format. It supports multiple image formats and allows you to specify file patterns for **batch processing**. The tool is written in **Python** and uses the **Pillow** library for image processing.

I created **Taco** to solve a problem I faced: the lack of a simple, user-friendly tool for **batch image conversion**. While there are many image conversion tools available, I couldn’t find one that was straightforward, lightweight, and met my specific needs. Frustrated with the options, I decided to build **Taco**—a command-line tool that makes batch converting images to WebP format quick and hassle-free. Now, I’m excited to share it with others who might be facing the same challenge! 🌮

---

## Features

- **Batch Conversion**: Convert multiple images at once using file patterns (e.g., `*.png`, `*.jpg`).
- **Custom Quality**: Set the quality of the output WebP images (0-100).
- **Output Directory**: Automatically saves converted images in a dedicated `webp_output` directory.
- **Cross-Platform**: Works on any system with Python and Pillow installed.

---

## Installation

### Using Nix

If you're using Nix, you can set up the environment with the following `shell.nix` file:

```nix
{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages(p: with p; [
      pillow
    ]))
  ];
}
```

To enter the development environment, run:

```bash
nix-shell
```

### Manual Installation

1. **Install Python**: Ensure you have Python 3.8 or higher installed.
2. **Install Pillow**: Install the Pillow library using pip:

   ```bash
   pip install pillow
   ```

3. **Clone the Repository**:

   ```bash
   git clone https://github.com/wmouton/taco.git
   cd taco
   ```

---

## Usage

Run the script with the following command:

```bash
python taco.py *.png *.jpg
```

This will convert all `.png` and `.jpg` files in the current directory to WebP format and save them in the `webp_output` directory.

### Command-Line Arguments

- **`patterns`**: Specify one or more file patterns (e.g., `*.png`, `*.jpg`) to convert matching images.

Example:

```bash
python taco.py *.png images/*.jpg
```

---

## Configuration

You can customize the following constants in the script:

- **`OUTPUT_DIR`**: The directory where converted WebP images are saved. Default: `webp_output`.
- **`WEBP_QUALITY`**: The quality of the output WebP images (0-100). Default: `90`.

---

## Contributing

Contributions are welcome! If you'd like to contribute to Taco, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push to your fork.
4. Submit a pull request.

---

## License

Taco is licensed under the GNU Affero General Public License. See [LICENSE](LICENSE) for more details.

---

## Support

If you encounter any issues or have questions, please open an issue on the [GitHub repository](https://github.com/wmouton/taco/issues).

---

Enjoy converting your images with Taco! 🌮
