import os
from pathlib import Path

import jinja2


BASE_DIR = Path(os.path.dirname(__file__)).absolute()
TEMPLATE_DIR = BASE_DIR / 'templates'
EASTER_TEMPLATE = 'easter.sty.j2'
OUT = BASE_DIR / 'easter.sty'


def tex_color(color_hex: str) -> list:
    if color_hex.startswith('#'):
        color_values = color_hex[1:]
    else:
        color_values = color_hex
    color_int = [str(int(color_values[i:i+2], 16)) for i in (0, 2, 4)]
    return f"{{{','.join(color_int)}}}"


def main() -> None:
    # dark mode
    colors = {
        'dark': {
            'foreground': '#f2f0f5',
            'background': '#0c011f',
            'bg-shade-one': '#180736',
            'bg-shade-two': '#26114B',
            'bg-shade-three': '#371F60',
            'bg-shade-four': '#4B3176',
            'text-shade-one': '#b2a0cb',
            'text-shade-two': '#957eb5',
            'text-shade-three': '#7a60a0',
            'text-shade-four': '#61468b',
            'primary': '#c6257d',
            'secondary': '#4dadd8',
            'accent-one': '#60a5f9',
            'accent-two': '#d381f7',
            'accent-three': '#ff7975',
            'error': '#bb2626',
            'success': '#54aa18',
            'warning': '#efb100'
        }
    }
    for mode, color in colors.items():
        for color_key, color_value in color.items():
            color[color_key] = tex_color(color_value)

    templateLoader = jinja2.FileSystemLoader(searchpath=TEMPLATE_DIR)
    templateEnv = jinja2.Environment(loader=templateLoader)
    easter_tpl = templateEnv.get_template(EASTER_TEMPLATE)
    with open(OUT, 'w', encoding='UTF-8') as tpl:
        tpl.write(easter_tpl.render(colors=colors, mode='dark'))


if __name__ == '__main__':
    main()
