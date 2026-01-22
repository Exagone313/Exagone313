import cairo
import math


FONT = "Inter"
FONT_SIZE = 14
PADDING_X = 12
PADDING_Y = 6
TOP_MARGIN = 3


def hex_to_cairo_rgb(hex_color: str) -> tuple[float, float, float]:
    """
    Convert an HTML hex color (#RRGGBB or #RGB) to a Cairo RGB tuple (0.0–1.0).
    """
    hex_color = hex_color.lstrip("#")

    if len(hex_color) == 3:
        hex_color = "".join(c * 2 for c in hex_color)
    elif len(hex_color) != 6:
        raise ValueError("Hex color must be in #RGB or #RRGGBB format")

    r = int(hex_color[0:2], 16) / 255.0
    g = int(hex_color[2:4], 16) / 255.0
    b = int(hex_color[4:6], 16) / 255.0

    return (r, g, b)


def create_tag(filename, text, fg, bg):
    text_color = hex_to_cairo_rgb(fg)
    bg_color = hex_to_cairo_rgb(bg)

    tmp_surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1, 1)
    ctx = cairo.Context(tmp_surface)

    ctx.select_font_face(FONT, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(FONT_SIZE)

    text_ext = ctx.text_extents(text)
    ascent, descent, font_height, _, _ = ctx.font_extents()

    width = int(text_ext.width + 2 * PADDING_X)
    real_height = int(font_height + 2 * PADDING_Y)
    height = real_height + TOP_MARGIN
    radius = real_height / 2

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)

    if TOP_MARGIN > 0:
        ctx.set_operator(cairo.OPERATOR_OVER)
        ctx.translate(0, TOP_MARGIN)

    ctx.set_source_rgb(*bg_color)
    ctx.move_to(radius, 0)
    ctx.arc(width - radius, radius, radius, -math.pi / 2, math.pi / 2)
    ctx.arc(radius, radius, radius, math.pi / 2, 3 * math.pi / 2)
    ctx.close_path()
    ctx.fill()

    ctx.set_source_rgb(*text_color)
    ctx.select_font_face(FONT, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(FONT_SIZE)

    x = PADDING_X - text_ext.x_bearing
    y = PADDING_Y + ascent

    ctx.move_to(x, y)
    ctx.show_text(text)

    surface.write_to_png(filename)


# filename text fg bg
create_tag("python.png", "Python", "#fff", "#2b5b84")
create_tag("javascript.png", "JavaScript", "#000", "#ff0")
create_tag("typescript.png", "TypeScript", "#fff", "#3178c6")
#create_tag("deno.png", "Deno", "#000", "#fff")
create_tag("java.png", "Java", "#fff", "#F29111")
create_tag("go.png", "Go", "#fff", "#007d9c")
create_tag("zig.png", "Zig", "#F7A41D", "#121212")
create_tag("gtk.png", "GTK", "#fff", "#000")
#create_tag("c.png", "C", "#a9bacd", "#fff")
create_tag("css.png", "CSS", "#fff", "#639")
create_tag("claude.png", "Claude Opus 4.5", "#fff", "#5b5b57")
create_tag("fastapi.png", "FastAPI", "#fafdfd", "#009688")
create_tag("react.png", "React", "#fff", "#087ea4")
create_tag("shell.png", "shell#", "#0f0", "#000")
create_tag("podman.png", "Podman", "#fafdfd", "#009efe")
create_tag("docker.png", "Docker", "#fff", "#00153c")
create_tag("lua.png", "Lua", "#fff", "#00007f")
create_tag("redis.png", "Redis", "#ff4438", "#07151c")
