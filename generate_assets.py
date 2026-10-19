import json, math, os

os.makedirs('img', exist_ok=True)

C = dict(pink='#f4b6c2', cream='#ecdcc8', green='#5c7a4a', blue='#b5d3e0', red='#d9585a',
         mustard='#f0b84a', yellow='#f5c24a', lilac='#b9a6d3', black='#2e2420',
         coral='#f08a7e', peach='#f6c9a8', white='#fffaf2', kraft='#c9a27a', dark='#3b2a22')


def svg(w, h, body, b1='#f7e6d8', b2='#edcdb7'):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice">'
            f'<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{b1}"/>'
            f'<stop offset="1" stop-color="{b2}"/></linearGradient>'
            f'<filter id="s" x="-20%" y="-20%" width="140%" height="140%">'
            f'<feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#5a3a2a" flood-opacity=".25"/></filter></defs>'
            f'<rect width="{w}" height="{h}" fill="url(#g)"/>{body}</svg>')


def daisy(x, y, r, petal='#fffaf2', ctr='#f4b400', smile=False, n=9):
    s = ''
    for i in range(n):
        s += (f'<ellipse cx="{x}" cy="{y - r * .55:.1f}" rx="{r * .27:.1f}" ry="{r * .45:.1f}" fill="{petal}" '
              f'stroke="#0000001a" stroke-width="2" transform="rotate({i * 360 / n:.1f} {x} {y})"/>')
    s += f'<circle cx="{x}" cy="{y}" r="{r * .3:.1f}" fill="{ctr}"/>'
    if smile:
        s += (f'<circle cx="{x - r * .1:.1f}" cy="{y - r * .05:.1f}" r="{r * .035:.1f}" fill="#3b2a22"/>'
              f'<circle cx="{x + r * .1:.1f}" cy="{y - r * .05:.1f}" r="{r * .035:.1f}" fill="#3b2a22"/>'
              f'<path d="M{x - r * .1:.1f},{y + r * .05:.1f} Q{x},{y + r * .16:.1f} {x + r * .1:.1f},{y + r * .05:.1f}" '
              f'stroke="#3b2a22" stroke-width="2" fill="none" stroke-linecap="round"/>')
    return f'<g filter="url(#s)">{s}</g>'


def rosette(x, y, r, c1, c2=None, n=12):
    c2 = c2 or c1
    s = ''
    for i in range(n):
        a = i * 2 * math.pi / n
        s += f'<circle cx="{x + math.cos(a) * r * .8:.1f}" cy="{y + math.sin(a) * r * .8:.1f}" r="{r * .26:.1f}" fill="{c1}"/>'
    s += f'<circle cx="{x}" cy="{y}" r="{r * .85:.1f}" fill="{c1}"/>'
    for k in (.7, .5, .3):
        s += (f'<circle cx="{x}" cy="{y}" r="{r * k:.1f}" fill="none" stroke="{c2}" stroke-width="{r * .07:.1f}" '
              f'stroke-dasharray="{r * .08:.1f} {r * .07:.1f}" opacity=".75"/>')
    s += f'<circle cx="{x}" cy="{y}" r="{r * .1:.1f}" fill="{c2}"/>'
    return f'<g filter="url(#s)">{s}</g>'


def leaf(x, y, s, c, rot=0):
    return (f'<g filter="url(#s)" transform="translate({x} {y}) rotate({rot}) scale({s})">'
            f'<path d="M0,-100 C75,-60 85,40 0,100 C-85,40 -75,-60 0,-100Z" fill="{c}"/>'
            f'<path d="M0,-90 L0,95" stroke="#00000033" stroke-width="3"/>'
            + ''.join(f'<path d="M0,{k} L{40},{k - 25} M0,{k} L-40,{k - 25}" stroke="#00000026" stroke-width="3" fill="none"/>'
                      for k in range(-50, 80, 30)) + '</g>')


def heart(x, y, s, c):
    return (f'<g filter="url(#s)" transform="translate({x} {y}) scale({s})">'
            f'<path d="M0,40 C-80,-10 -45,-70 0,-30 C45,-70 80,-10 0,40Z" fill="{c}"/></g>')


def bunny(x, y, s, body='#f6ead8', bow='#f08a7e'):
    return (f'<g filter="url(#s)" transform="translate({x} {y}) scale({s})">'
            f'<ellipse cx="-30" cy="-95" rx="16" ry="45" fill="{body}" transform="rotate(-8 -30 -95)"/>'
            f'<ellipse cx="30" cy="-95" rx="16" ry="45" fill="{body}" transform="rotate(8 30 -95)"/>'
            f'<ellipse cx="-30" cy="-95" rx="7" ry="32" fill="#f4b6c2" transform="rotate(-8 -30 -95)"/>'
            f'<ellipse cx="30" cy="-95" rx="7" ry="32" fill="#f4b6c2" transform="rotate(8 30 -95)"/>'
            f'<ellipse cx="0" cy="85" rx="48" ry="52" fill="{body}"/>'
            f'<circle cx="0" cy="0" r="58" fill="{body}"/>'
            f'<circle cx="-20" cy="-4" r="5" fill="#3b2a22"/><circle cx="20" cy="-4" r="5" fill="#3b2a22"/>'
            f'<circle cx="-34" cy="10" r="9" fill="#f4b6c2" opacity=".8"/><circle cx="34" cy="10" r="9" fill="#f4b6c2" opacity=".8"/>'
            f'<ellipse cx="0" cy="8" rx="7" ry="5" fill="#e98a9a"/>'
            f'<path d="M-30,52 L0,66 L-30,80Z M30,52 L0,66 L30,80Z" fill="{bow}"/><circle cx="0" cy="66" r="8" fill="{bow}"/></g>')


def bear(x, y, s, fur='#d9b38c'):
    return (f'<g filter="url(#s)" transform="translate({x} {y}) scale({s})">'
            f'<circle cx="-44" cy="-44" r="22" fill="{fur}"/><circle cx="44" cy="-44" r="22" fill="{fur}"/>'
            f'<circle cx="-44" cy="-44" r="11" fill="#f4c7c3"/><circle cx="44" cy="-44" r="11" fill="#f4c7c3"/>'
            f'<circle cx="0" cy="0" r="60" fill="{fur}"/><ellipse cx="0" cy="18" rx="28" ry="22" fill="#f6ead8"/>'
            f'<circle cx="-22" cy="-8" r="5" fill="#3b2a22"/><circle cx="22" cy="-8" r="5" fill="#3b2a22"/>'
            f'<ellipse cx="0" cy="10" rx="8" ry="6" fill="#3b2a22"/>'
            f'<path d="M-10,24 Q0,32 10,24" stroke="#3b2a22" stroke-width="3" fill="none"/></g>')


def tulip(x, y, s, c, stem=140):
    return (f'<g filter="url(#s)" transform="translate({x} {y}) scale({s})">'
            f'<path d="M0,0 L0,{stem}" stroke="#5c7a4a" stroke-width="7"/>'
            f'<path d="M-26,0 C-34,-48 -12,-62 0,-74 C12,-62 34,-48 26,0 C10,14 -10,14 -26,0Z" fill="{c}"/>'
            f'<path d="M0,-74 C-14,-40 -14,-10 0,10 C14,-10 14,-40 0,-74Z" fill="#ffffff" opacity=".28"/></g>')


def bouquet(x, y, s, cols):
    b = f'<g transform="translate({x} {y}) scale({s})">'
    b += f'<path d="M-90,40 L90,40 L20,260 L-20,260Z" fill="{C["kraft"]}" filter="url(#s)"/>'
    for i, c in enumerate(cols):
        ang = -50 + i * (100 / max(1, len(cols) - 1))
        b += tulip(0, 40, 1, c, 0).replace('<g filter', f'<g transform="rotate({ang} 0 40) translate(0 -60)" filter', 1) if False else ''
    for i, c in enumerate(cols):
        px = -80 + i * (160 / max(1, len(cols) - 1))
        b += tulip(px, -20 + abs(px) * .3, 1.05, c, 70)
    b += daisy(-40, 10, 28, smile=False) + daisy(45, 5, 26) + daisy(0, 25, 24)
    b += f'<path d="M-95,42 L95,42" stroke="#f4b6c2" stroke-width="10" stroke-linecap="round"/>'
    b += '</g>'
    return b


def rainbow(x, y, s):
    cols = ['#d9585a', '#f0b84a', '#f5e08a', '#7fa56a', '#7fb2cf']
    out = f'<g filter="url(#s)" transform="translate({x} {y}) scale({s})">'
    for i, c in enumerate(cols):
        r = 120 - i * 20
        out += f'<path d="M{-r},0 A{r},{r} 0 0 1 {r},0" stroke="{c}" stroke-width="20" fill="none"/>'
    return out + '</g>' + daisy(x - 110 * s, y + 10, 24 * s, ctr='#f4b400') + daisy(x + 110 * s, y + 10, 24 * s, petal='#f4b6c2')


def bag(x, y, s, c, c2):
    return (f'<g filter="url(#s)" transform="translate({x} {y}) scale({s})">'
            f'<path d="M-50,-30 C-50,-120 50,-120 50,-30" stroke="{c2}" stroke-width="14" fill="none"/>'
            f'<rect x="-95" y="-30" width="190" height="140" rx="22" fill="{c}"/></g>'
            + daisy(x - 40 * s, y + 30 * s, 28 * s) + daisy(x + 35 * s, y + 55 * s, 26 * s, petal='#fde3df'))


def phone(x, y, s, c):
    return (f'<g filter="url(#s)" transform="translate({x} {y}) scale({s})">'
            f'<rect x="-70" y="-130" width="140" height="260" rx="24" fill="{c}"/>'
            f'<rect x="-52" y="-112" width="104" height="224" rx="14" fill="#fdf0e8"/></g>'
            + daisy(x - 20 * s, y - 60 * s, 24 * s) + daisy(x + 18 * s, y, 24 * s, petal='#f4b6c2') + daisy(x - 15 * s, y + 60 * s, 22 * s))


def scrunchie(x, y, r, c):
    s = f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="{c}" stroke-width="{r * .6:.1f}"/>'
    s += f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="#ffffff55" stroke-width="3" stroke-dasharray="6 10"/>'
    return f'<g filter="url(#s)">{s}</g>'


def hoop(x, y, s, c):
    return (f'<g filter="url(#s)" transform="translate({x} {y}) scale({s})">'
            f'<circle cx="0" cy="-60" r="14" fill="none" stroke="#c9a449" stroke-width="5"/>'
            f'<path d="M0,-46 L0,-10" stroke="#c9a449" stroke-width="4"/></g>' + daisy(x, y + 20 * s, 34 * s, petal=c, ctr='#f5c24a', n=6))


def bow(x, y, s, c):
    return (f'<g filter="url(#s)" transform="translate({x} {y}) scale({s})">'
            f'<path d="M0,0 C-70,-60 -110,-30 -100,10 C-95,50 -50,50 0,0Z" fill="{c}"/>'
            f'<path d="M0,0 C70,-60 110,-30 100,10 C95,50 50,50 0,0Z" fill="{c}"/>'
            f'<path d="M-6,8 L-50,95 L-20,85 L-8,110 L6,30Z" fill="{c}"/><path d="M6,8 L50,95 L20,85 L8,110 L-6,30Z" fill="{c}"/>'
            f'<circle cx="0" cy="4" r="20" fill="{c}"/><circle cx="0" cy="4" r="20" fill="#ffffff22"/></g>')


def pot(x, y, s, c='#e0b98f'):
    return (f'<g filter="url(#s)" transform="translate({x} {y}) scale({s})">'
            f'<path d="M-50,0 L50,0 L38,70 L-38,70Z" fill="{c}"/></g>'
            + leaf(x - 25 * s, y - 55 * s, .55 * s, '#5c7a4a', -25) + leaf(x + 25 * s, y - 55 * s, .55 * s, '#6f9158', 25)
            + leaf(x, y - 75 * s, .6 * s, '#4d6b3d', 0))


def lace_strip(x, y, w, h, c, rot=0):
    s = f'<g filter="url(#s)" transform="rotate({rot} {x} {y})"><rect x="{x - w / 2}" y="{y - h / 2}" width="{w}" height="{h}" rx="10" fill="{c}"/>'
    for i in range(int(w // 14)):
        for j in range(int(h // 14)):
            s += f'<circle cx="{x - w / 2 + 8 + i * 14}" cy="{y - h / 2 + 8 + j * 14}" r="3" fill="#00000018"/>'
    return s + '</g>'


def wood(w, h):
    s = f'<rect y="{h * .55}" width="{w}" height="{h * .45}" fill="#b98a5e"/>'
    for i in range(8):
        s += f'<path d="M0,{h * .6 + i * h * .05} H{w}" stroke="#00000012" stroke-width="2"/>'
    return s


# ---------- product scenes (600x490) ----------
W, H = 600, 490


def sc_runner(c1, c2):
    b = wood(W, H) + lace_strip(300, 250, 520, 150, '#f0dcc8', -6)
    for i in range(4):
        b += daisy(120 + i * 120, 250 - i * 12, 40, smile=False) + leaf(120 + i * 120 + 45, 250 - i * 12 + 28, .32, c1, 60)
    return svg(W, H, b, '#f6e4d6', '#e8c9ae')


def sc_placemat(c1, c2):
    b = wood(W, H) + rosette(300, 250, 190, c1, c2, 14) + rosette(420, 300, 80, '#f3e2cc', c2, 10)
    return svg(W, H, b, '#f7e0d8', '#e9c1b8')


def sc_coasters(c1, c2):
    b = daisy(170, 170, 100, smile=True) + daisy(400, 200, 110, smile=True) + daisy(250, 360, 95, petal='#f8b9aa', smile=True) + daisy(470, 370, 80, petal='#fde3df', smile=True)
    return svg(W, H, b, '#f3e1cf', '#e2c4a9')


def sc_cupcloth(c1, c2):
    b = rosette(300, 270, 190, c1, '#f3c7a8', 14) + '<g filter="url(#s)"><ellipse cx="300" cy="190" rx="105" ry="30" fill="#7a4b32"/><path d="M195,190 L205,100 Q300,70 395,100 L405,190Z" fill="#f2ece3"/><ellipse cx="300" cy="115" rx="100" ry="26" fill="#a86a44"/></g>'
    return svg(W, H, b, '#f6e5da', '#ecd0c0')


def sc_scallop(c1, c2):
    b = rosette(210, 280, 130, '#b8452f', '#7a2a1c') + rosette(380, 240, 120, '#e6954f', '#a25d24') + rosette(430, 360, 90, '#f2d9c0', '#c99c75')
    return svg(W, H, b, '#f3dfc8', '#dcb995')


def sc_leaf(c1, c2):
    b = wood(W, H) + leaf(300, 255, 2.0, c1, 90) + '<g filter="url(#s)"><circle cx="300" cy="245" r="115" fill="#ece7df"/><circle cx="300" cy="245" r="85" fill="#f6f2ec"/></g>'
    b += '<rect x="270" y="130" width="14" height="190" rx="6" fill="#2b2b2b"/><rect x="305" y="130" width="14" height="190" rx="6" fill="#444"/>'
    return svg(W, H, b, '#f2e0cf', '#e6c8ac')


def sc_tissue(c1, c2):
    b = '<g filter="url(#s)"><path d="M230,140 Q300,40 380,140Z" fill="#fff"/><rect x="120" y="150" width="360" height="230" rx="26" fill="#f1e1c8"/></g>'
    b += '<rect x="230" y="165" width="140" height="22" rx="11" fill="#6a4a3a"/>'
    for i in range(4):
        for j in range(2):
            b += daisy(165 + i * 90, 245 + j * 85, 30, petal='#fffaf2' if (i + j) % 2 == 0 else '#fde3df', ctr='#f08a2e')
    return svg(W, H, b, '#f7e8d6', '#ead2b5')


def sc_planter(c1, c2):
    b = ''.join(f'<path d="M300,30 L{200 + k * 50},300" stroke="#e9c7bd" stroke-width="4"/>' for k in range(5))
    b += '<g filter="url(#s)"><path d="M185,250 H415 Q415,380 300,410 Q185,380 185,250Z" fill="#f2c2c3"/></g>'
    b += ''.join(f'<path d="M{200 + k * 40},255 L{235 + k * 40},400" stroke="#fff7ee" stroke-width="4" opacity=".7"/>' for k in range(5))
    b += leaf(260, 170, .7, '#5c7a4a', -35) + leaf(300, 140, .8, '#4d6b3d', 0) + leaf(340, 170, .7, '#6f9158', 35)
    return svg(W, H, b, '#f4e4d3', '#e3c7ad')


def sc_hearts(c1, c2):
    b = heart(190, 210, 1.4, c1) + heart(400, 250, 1.4, c2) + heart(300, 360, 1.2, '#f2d9c0')
    return svg(W, H, b, '#f8e6dc', '#ecc9bd')


def sc_mug(c1, c2):
    b = '<g filter="url(#s)"><rect x="170" y="140" width="220" height="230" rx="30" fill="%s"/><path d="M390,200 Q470,210 440,300 Q420,330 390,320" stroke="%s" stroke-width="26" fill="none"/></g>' % (c1, c1)
    b += daisy(280, 255, 52) + daisy(205, 330, 26, petal='#fde3df')
    return svg(W, H, b, '#f4e3d2', '#e5c8ae')


def sc_doily(c1, c2):
    b = rosette(300, 245, 215, '#f6e8d6', c1, 18) + rosette(300, 245, 110, '#f3d9cc', c2, 12)
    return svg(W, H, b, '#e9d8c6', '#d4b99c')


def sc_pot(c1, c2):
    b = pot(300, 250, 3.0, c1) + daisy(250, 330, 32) + daisy(350, 345, 28, petal='#fde3df')
    return svg(W, H, b, '#f6e6d6', '#e7cdb2')


def sc_bottle(c1, c2):
    b = '<g filter="url(#s)"><rect x="240" y="60" width="120" height="360" rx="50" fill="%s"/></g>' % c1
    b += ''.join(daisy(300, 130 + i * 90, 30, petal='#fffaf2' if i % 2 == 0 else '#fde3df') for i in range(3))
    return svg(W, H, b, '#f5e5d5', '#e6cdb5')


SCENES = dict(runner=sc_runner, placemat=sc_placemat, coasters=sc_coasters, cupcloth=sc_cupcloth, scallop=sc_scallop,
              leaf=sc_leaf, tissue=sc_tissue, planter=sc_planter, hearts=sc_hearts, mug=sc_mug, doily=sc_doily,
              pot=sc_pot, bottle=sc_bottle)

# slug, name, price, category, colours, materials, scene
P = [
    ('daisy-table-runner', 'Daisy Table Runner', 1299, 'table-runners', ['green', 'cream', 'pink', 'red'], ['cotton100'], 'runner'),
    ('flower-placemat', 'Flower Placemat (Set of 4)', 899, 'placemats', ['red', 'cream', 'pink'], ['cotton100'], 'placemat'),
    ('daisy-coasters', 'Daisy Coasters (Set of 4)', 499, 'coasters-cloths', ['green', 'cream', 'red', 'pink'], ['cotton100'], 'coasters'),
    ('flower-cup-cloth', 'Flower Cup Cloth', 249, 'coasters-cloths', ['green', 'cream', 'red', 'pink'], ['cottonBlend'], 'cupcloth'),
    ('scallop-coasters', 'Scallop Coasters (Set of 4)', 499, 'coasters-cloths', ['red', 'peach', 'pink', 'mustard'], ['cotton100'], 'scallop'),
    ('leaf-placemat', 'Leaf Placemat (Set of 2)', 799, 'placemats', ['green', 'cream', 'red', 'green'], ['cottonBlend'], 'leaf'),
    ('tissue-box-cover', 'Tissue Box Cover', 699, 'decor-accents', ['green', 'peach', 'red', 'green'], ['acrylicBlend'], 'tissue'),
    ('hanging-planter', 'Hanging Planter', 899, 'decor-accents', ['green', 'pink', 'lilac', 'cream', 'black'], ['cotton100'], 'planter'),
    ('lace-table-runner', 'Lace Table Runner', 1499, 'table-runners', ['cream', 'pink', 'blue'], ['cotton100'], 'runner'),
    ('sunflower-table-runner', 'Sunflower Table Runner', 1399, 'table-runners', ['mustard', 'green', 'cream'], ['cottonBlend'], 'runner'),
    ('round-table-mat', 'Round Table Mat (Set of 2)', 599, 'placemats', ['pink', 'cream', 'lilac'], ['cotton100'], 'placemat'),
    ('rosette-placemat-set', 'Rosette Placemat (Set of 6)', 1599, 'placemats', ['blue', 'cream', 'green'], ['cottonBlend'], 'placemat'),
    ('mug-cozy', 'Mug Cozy', 299, 'kitchen-essentials', ['pink', 'mustard', 'green', 'blue'], ['acrylicBlend'], 'mug'),
    ('teapot-cozy', 'Teapot Cozy', 799, 'kitchen-essentials', ['red', 'cream', 'green'], ['cottonBlend'], 'mug'),
    ('cup-cloth-set', 'Cup Cloth (Set of 3)', 649, 'coasters-cloths', ['pink', 'cream', 'lilac', 'yellow'], ['cotton100'], 'cupcloth'),
    ('heart-coasters', 'Heart Coasters (Set of 4)', 449, 'coasters-cloths', ['red', 'pink', 'cream'], ['cotton100'], 'hearts'),
    ('pot-holder-pair', 'Pot Holder (Pair)', 399, 'kitchen-essentials', ['mustard', 'red', 'cream'], ['cotton100'], 'scallop'),
    ('dish-scrubby-set', 'Dish Scrubby (Set of 3)', 299, 'kitchen-essentials', ['green', 'pink', 'yellow', 'blue'], ['acrylicBlend'], 'coasters'),
    ('bottle-cover', 'Bottle Cover', 349, 'kitchen-essentials', ['pink', 'blue', 'cream'], ['cottonBlend'], 'bottle'),
    ('basket-cover', 'Basket Cover', 549, 'kitchen-essentials', ['cream', 'green', 'peach'], ['cotton100'], 'doily'),
    ('wall-hanging-doily', 'Wall Hanging Doily', 999, 'decor-accents', ['cream', 'pink', 'blue'], ['cotton100'], 'doily'),
    ('plant-pot-cover', 'Plant Pot Cover', 549, 'decor-accents', ['peach', 'green', 'lilac', 'black'], ['cottonBlend'], 'pot'),
    ('remote-holder', 'Remote Holder', 449, 'decor-accents', ['blue', 'cream', 'pink'], ['acrylicBlend'], 'mug'),
    ('daisy-fridge-magnets', 'Daisy Fridge Magnets (Set of 4)', 349, 'decor-accents', ['cream', 'pink', 'mustard', 'green'], ['cotton100'], 'coasters'),
]

COLOR_HEX = dict(C)
products = []
for slug, name, price, cat, cols, mats, scene in P:
    c1 = C.get(cols[0], '#f4b6c2')
    c2 = C.get(cols[1], '#ecdcc8')
    if scene in ('runner', 'leaf', 'placemat') and cols[0] in ('cream',):
        c1 = '#f3e2cc'
    open(f'img/p-{slug}.svg', 'w').write(SCENES[scene](c1, c2))
    products.append(dict(id=slug, name=name, price=price, cat=cat, colors=cols, materials=mats, img=f'img/p-{slug}.svg'))

with open('products.js', 'w') as f:
    f.write('// Generated by generate_assets.py - edit freely, or replace img paths with real photos.\n')
    f.write('window.COLOR_HEX = ' + json.dumps({k: COLOR_HEX[k] for k in ['pink', 'cream', 'green', 'blue', 'red', 'mustard', 'yellow', 'lilac', 'black', 'peach']}, indent=2) + ';\n')
    f.write('window.PRODUCTS = ' + json.dumps(products, indent=2) + ';\n')

# ---------- category tiles (600x390) ----------
cw, ch = 600, 390
cats = {}
cats['home-essentials'] = wood(cw, ch) + lace_strip(300, 230, 520, 110, '#f0dcc8', -4) + ''.join(daisy(110 + i * 95, 230 - i * 4, 30) for i in range(5)) + pot(80, 120, .9)
cats['keychains'] = ''.join(f'<path d="M{x},40 L{x},120" stroke="#c9a449" stroke-width="4"/><circle cx="{x}" cy="40" r="14" fill="none" stroke="#c9a449" stroke-width="5"/>' for x in (130, 300, 470)) + heart(130, 190, 1.0, '#d9585a') + bunny(300, 220, .8) + daisy(470, 190, 60, petal='#f4b6c2')
cats['flowers'] = bouquet(300, 90, 1.15, ['#e8708a', '#f4b6c2', '#f0b84a', '#d9585a', '#f3e2cc'])
cats['car'] = '<rect width="600" height="390" fill="#2c2f33"/><path d="M0,250 Q300,150 600,250 V390 H0Z" fill="#1d2023"/><path d="M300,0 V150" stroke="#ddd" stroke-width="4"/>' + daisy(300, 220, 80, smile=False)
cats['wall'] = '<rect width="600" height="390" fill="#f3e0cf"/>' + rainbow(300, 230, 1.5) + leaf(540, 300, .7, '#5c7a4a', 40)
cats['handbags'] = bag(200, 190, 1.3, '#f08a9c', '#d95f7a') + bag(420, 250, .9, '#f9c9c9', '#e8a0a0')
cats['phone-pouches'] = phone(300, 195, 1.15, '#f2a99a')
cats['baby'] = bunny(220, 190, 1.2) + '<g filter="url(#s)"><ellipse cx="430" cy="300" rx="60" ry="32" fill="#f6ead8"/><ellipse cx="430" cy="280" rx="45" ry="28" fill="#f4b6c2"/></g>'
cats['hair'] = scrunchie(150, 130, 70, '#f19cb3') + scrunchie(330, 210, 85, '#b9a6d3') + scrunchie(480, 120, 65, '#f3e2cc') + scrunchie(200, 300, 55, '#9fc39a')
cats['earrings'] = hoop(130, 100, 1.4, '#f4b6c2') + hoop(260, 110, 1.4, '#d9585a') + hoop(400, 100, 1.4, '#3f6fb0') + hoop(520, 110, 1.2, '#f4b6c2')
cats['scarves'] = '<g filter="url(#s)"><path d="M0,120 Q300,40 600,150 L600,310 Q300,220 0,290Z" fill="#6b8c58"/></g>' + ''.join(daisy(60 + i * 100, 200 + (i % 2) * 20, 28) for i in range(6))
cats['hair-tie'] = bow(300, 180, 1.9, '#f4a3bd')
cats['phone-charms'] = '<path d="M300,30 V300" stroke="#ccc" stroke-width="4"/>' + ''.join(f'<circle cx="300" cy="{60 + i * 38}" r="14" fill="{c}" filter="url(#s)"/>' for i, c in enumerate(['#f4b6c2', '#f0b84a', '#7fb2cf', '#d9585a', '#b9a6d3', '#9fc39a'])) + daisy(300, 310, 38)
cats['airpods'] = bear(210, 190, 1.4, '#e8a3b5') + daisy(430, 170, 55) + daisy(480, 290, 45, petal='#f4b6c2')
cats['specs'] = '<g filter="url(#s)"><rect x="90" y="150" width="420" height="170" rx="28" fill="#f2ece3"/></g>' + ''.join(daisy(130 + i * 70, 235, 24, petal='#fffaf2' if i % 2 else '#fde3df') for i in range(6)) + '<g stroke="#2e2420" stroke-width="8" fill="none"><circle cx="230" cy="110" r="42"/><circle cx="370" cy="110" r="42"/><path d="M272,105 H328"/></g>'
for k, body in cats.items():
    open(f'img/cat-{k}.svg', 'w').write(svg(cw, ch, body))

# ---------- occasion tiles (400x400) ----------
occ = {
    'birthdays': bouquet(200, 90, 1.0, ['#e8708a', '#f4b6c2', '#f3e2cc', '#d9585a']),
    'anniversaries': bear(130, 190, .9, '#d9b38c') + bear(270, 200, .9, '#c89d77') + heart(200, 300, .6, '#d9585a'),
    'festive': heart(110, 200, .8, '#d9585a') + rosette(250, 230, 70, '#e6954f', '#a25d24') + rosette(300, 120, 40, '#d9585a', '#7a2a1c'),
    'new-baby': bunny(150, 190, .95) + '<g filter="url(#s)"><ellipse cx="290" cy="300" rx="50" ry="28" fill="#a9c6dc"/></g>',
    'weddings': bouquet(200, 90, 1.0, ['#f3e2cc', '#fffaf2', '#f4b6c2', '#e8708a']),
    'friendship': ''.join(daisy(x, 200, 50, petal=p) for x, p in ((100, '#f4b6c2'), (200, '#fffaf2'), (300, '#b9a6d3'))) + heart(200, 310, .7, '#d9585a'),
    'corporate': '<g filter="url(#s)"><rect x="110" y="240" width="180" height="120" rx="14" fill="#d9b78a"/></g>' + pot(200, 230, 1.5, '#d9b78a').replace('translate', 'translate') + '',
}
for k, body in occ.items():
    open(f'img/occ-{k}.svg', 'w').write(svg(400, 400, body, '#f7e3d6', '#ebc9b6'))

# ---------- heroes ----------
hero = (f'<rect width="1600" height="700" fill="url(#g)"/>' + ''.join(
    f'<circle cx="{(i * 331) % 1600}" cy="{(i * 197) % 700}" r="{40 + (i * 13) % 60}" fill="#ffffff" opacity=".12"/>' for i in range(14))
    + bouquet(1060, 120, 1.9, ['#e8708a', '#f4b6c2', '#f3e2cc', '#d9585a', '#f4a3bd'])
    + bunny(1380, 470, 1.5)
    + '<g filter="url(#s)"><rect x="1260" y="560" width="230" height="110" rx="10" fill="#c9a27a"/></g>')
open('img/hero.svg', 'w').write(svg(1600, 700, hero, '#f8e6da', '#ecc7b3'))

banner = ('<g filter="url(#s)"><rect x="60" y="90" width="460" height="230" rx="12" fill="#c9a27a"/><rect x="80" y="110" width="420" height="190" rx="8" fill="#f3e2cc"/></g>'
          + ''.join(daisy(120 + i * 70, 160 + (i % 2) * 60, 36, petal=['#f4b6c2', '#fffaf2', '#e8708a'][i % 3]) for i in range(6))
          + bunny(430, 190, .7))
open('img/banner.svg', 'w').write(svg(1200, 360, banner, '#f5dcd2', '#e9b9ac'))

page_hero = (wood(1400, 340) + lace_strip(980, 220, 620, 130, '#f0dcc8', -6)
             + ''.join(daisy(740 + i * 110, 225 - i * 7, 38) for i in range(5))
             + '<g filter="url(#s)"><ellipse cx="1280" cy="190" rx="75" ry="22" fill="#7a4b32"/><path d="M1205,190 L1212,110 Q1280,90 1348,110 L1355,190Z" fill="#f2ece3"/></g>'
             + daisy(700, 90, 60) + daisy(790, 70, 40, petal='#f8b9aa'))
open('img/page-hero.svg', 'w').write(svg(1400, 340, page_hero, '#f6e1d4', '#e8c4ae'))

print('ok', len(os.listdir('img')), 'images,', len(products), 'products')
