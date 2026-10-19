/* Mirth & Mallow — shared behaviour */
(function () {
  const I = {
    truck: '<svg viewBox="0 0 24 24"><path d="M2 6h11v10H2zM13 9h4l3 3v4h-7z"/><circle cx="6" cy="17.5" r="1.8"/><circle cx="17" cy="17.5" r="1.8"/></svg>',
    gift: '<svg viewBox="0 0 24 24"><rect x="3" y="9" width="18" height="5" rx="1"/><path d="M5 14v7h14v-7M12 9v12M12 9c-3 0-5-1-5-3s3-3 5 3c2-6 5-5 5-3s-2 3-5 3"/></svg>',
    search: '<svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg>',
    user: '<svg viewBox="0 0 24 24"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4.5 3.5-7 8-7s8 2.5 8 7"/></svg>',
    cart: '<svg viewBox="0 0 24 24"><path d="M2 3h3l2.5 12h11L21 7H6"/><circle cx="9" cy="20" r="1.5"/><circle cx="18" cy="20" r="1.5"/></svg>',
    heart: '<svg viewBox="0 0 24 24"><path d="M12 21C5 15 3 11 3 8a4.5 4.5 0 0 1 9-1 4.5 4.5 0 0 1 9 1c0 3-2 7-9 13z"/></svg>',
    chev: '<svg class="chev" viewBox="0 0 12 12"><path d="M2 4l4 4 4-4"/></svg>',
    arrowR: '<svg viewBox="0 0 24 24"><path d="M4 12h16M14 6l6 6-6 6"/></svg>',
    leaf: '<svg viewBox="0 0 24 24" style="stroke:#5c7a4a"><path d="M5 19C5 9 11 4 20 4c0 9-5 15-15 15zM5 19c3-5 6-8 10-10"/></svg>',
    star: '<svg viewBox="0 0 24 24" style="stroke:#e8903a"><path d="M12 3l2.7 5.6 6.1.8-4.5 4.3 1.1 6.1L12 17l-5.4 2.8 1.1-6.1L3.2 9.4l6.1-.8z"/></svg>',
    flower: '<svg viewBox="0 0 24 24"><g fill="#fff"><circle cx="12" cy="6" r="3.5"/><circle cx="12" cy="18" r="3.5"/><circle cx="6" cy="12" r="3.5"/><circle cx="18" cy="12" r="3.5"/><circle cx="7.8" cy="7.8" r="3"/><circle cx="16.2" cy="7.8" r="3"/><circle cx="7.8" cy="16.2" r="3"/><circle cx="16.2" cy="16.2" r="3"/></g><circle cx="12" cy="12" r="3" fill="#f4b400" stroke="none"/></svg>',
    sprig: '<svg viewBox="0 0 44 36"><path d="M6 30C14 20 24 14 38 8M16 24c-4-1-6-4-6-7 4 0 6 3 6 7zm8-6c-3-2-4-5-3-8 4 1 5 4 3 8zm9-5c-2-3-2-6 0-8 3 2 3 5 0 8z"/></svg>',
    shopcart: '<svg viewBox="0 0 24 24"><path d="M2 3h3l2.5 12h11L21 7H6"/><circle cx="9" cy="20" r="1.5"/><circle cx="18" cy="20" r="1.5"/></svg>',
  };

  const LOGO = `<svg viewBox="0 0 64 64"><g stroke="#5c7a4a" fill="none" stroke-width="1.6"><path d="M20 58c2-14 8-22 18-30"/><path d="M26 46c-8 0-12-4-12-10 7 0 12 4 12 10zM32 38c6-1 10-5 10-11-6 0-10 5-10 11z"/></g>
    <g transform="translate(36 22)"><g fill="#fff" stroke="#e07a6a" stroke-width="1.6"><circle cx="0" cy="-11" r="7"/><circle cx="10" cy="-4" r="7"/><circle cx="6" cy="9" r="7"/><circle cx="-6" cy="9" r="7"/><circle cx="-10" cy="-4" r="7"/></g><circle r="5" fill="#f4b400"/></g></svg>`;

  const page = document.body.dataset.page || 'home';

  const occasions = ['Birthdays', 'Anniversaries', 'Festive Gifting', 'New Baby', 'Weddings', 'Friendship', 'Corporate Gifting'];
  const shopCats = [['Home Essentials', 'home-essentials.html'], ['Keychains & Charms', '#'], ['Flowers & Bouquets', '#'], ['Car Hangings', '#'], ['Wall Hangings', '#'], ['Handbags & Pouches', '#'], ['Baby Products', '#']];

  const header = `
  <div class="topbar"><div class="wrap">
    <span>${I.truck} Free Pan India Shipping on orders above ₹999</span>
    <span>${I.flower.replace('<svg','<svg style="fill:#fff"')} Handmade with Love</span>
    <span>Custom Orders Available</span>
    <span>${I.gift} Thoughtful Gifts for Every Occasion</span>
  </div></div>
  <header class="site-header"><div class="wrap">
    <a class="logo" href="index.html" aria-label="Mirth and Mallow home">${LOGO}
      <div><div class="name">Mirth <em>and</em> Mallow</div><span class="tag">CROCHET • GIFTS • HAPPY MOMENTS</span></div></a>
    <button class="menu-btn icons" id="menuBtn" aria-label="Menu"><svg viewBox="0 0 24 24" style="width:28px;height:28px;stroke:#3a1f1f;fill:none;stroke-width:1.8"><path d="M3 6h18M3 12h18M3 18h18"/></svg></button>
    <ul class="nav" id="nav">
      <li><a href="index.html" class="${page === 'home' ? 'active' : ''}">Home</a></li>
      <li><button class="${page === 'shop' ? 'active' : ''}" data-toggle>Shop ${I.chev}</button>
        <div class="dropdown">${shopCats.map(c => `<a href="${c[1]}">${c[0]}</a>`).join('')}</div></li>
      <li><button data-toggle>Gifting ${I.chev}</button>
        <div class="dropdown">${occasions.map(o => `<a href="home-essentials.html">${o}</a>`).join('')}</div></li>
      <li><a href="#">About</a></li>
      <li><a href="#">Custom Orders</a></li>
      <li><a href="#">Contact</a></li>
    </ul>
    <div class="icons">
      <button aria-label="Search">${I.search}</button>
      <a href="#" aria-label="Account">${I.user}</a>
      <a href="#" aria-label="Cart">${I.cart}<span class="badge" id="cartCount">0</span></a>
    </div>
  </div></header>`;

  const trust = `
  <section class="wrap trust">
    <div><span class="ic" style="background:#e8eddd">${I.leaf}</span><p><b>100% Handmade</b><small>Crafted with care</small></p></div>
    <div><span class="ic" style="background:#fbe0de"><svg viewBox="0 0 24 24" style="stroke:#c8434a"><path d="M12 21C5 15 3 11 3 8a4.5 4.5 0 0 1 9-1 4.5 4.5 0 0 1 9 1c0 3-2 7-9 13z"/></svg></span><p><b>Sustainable & Long-lasting</b><small>Slow fashion, brighter tomorrow</small></p></div>
    <div><span class="ic" style="background:#e3e9ee"><svg viewBox="0 0 24 24" style="stroke:#5b7184">${I.truck.slice(I.truck.indexOf('>') + 1, -6)}</svg></span><p><b>Pan India Shipping</b><small>Safe & Reliable</small></p></div>
    <div><span class="ic" style="background:#fdeedd">${I.star}</span><p><b>Support Small Business</b><small>Every purchase makes a difference</small></p></div>
  </section>
  <footer class="site-footer">© <span id="yr"></span> Mirth and Mallow · Handmade crochet &amp; gifts</footer>
  <div class="toast" id="toast"></div>`;

  document.getElementById('site-header').innerHTML = header;
  document.getElementById('site-footer').innerHTML = trust;
  document.getElementById('yr').textContent = new Date().getFullYear();

  // mobile nav + dropdown toggle
  document.getElementById('menuBtn').onclick = () => document.getElementById('nav').classList.toggle('open');
  document.querySelectorAll('[data-toggle]').forEach(b => b.onclick = () => b.parentElement.classList.toggle('open'));

  // cart
  const store = {
    get(k, d) { try { return JSON.parse(localStorage.getItem(k)) ?? d; } catch (e) { return d; } },
    set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} }
  };
  let cart = store.get('mm-cart', 0);
  const cartEl = document.getElementById('cartCount');
  const paintCart = () => cartEl.textContent = cart;
  paintCart();
  function toast(msg) {
    const t = document.getElementById('toast');
    t.textContent = msg; t.classList.add('show');
    clearTimeout(toast.t); toast.t = setTimeout(() => t.classList.remove('show'), 1800);
  }

  // occasions carousel (home)
  const track = document.getElementById('occTrack');
  if (track) {
    const step = () => track.clientWidth * .8;
    document.getElementById('occPrev').onclick = () => track.scrollBy({ left: -step(), behavior: 'smooth' });
    document.getElementById('occNext').onclick = () => track.scrollBy({ left: step(), behavior: 'smooth' });
  }

  // shop page
  const gridEl = document.getElementById('grid');
  if (gridEl && window.PRODUCTS) {
    const MAX = 5000;
    const cats = [['all', 'Home Essentials'], ['table-runners', 'Table Runners'], ['placemats', 'Placemat & Table Mats'], ['coasters-cloths', 'Coasters & Cup Cloths'], ['kitchen-essentials', 'Kitchen Essentials'], ['decor-accents', 'Decor Accents']];
    const mats = [['cotton100', '100% Cotton'], ['cottonBlend', 'Cotton Blend'], ['acrylicBlend', 'Acrylic Blend']];
    const swatchList = ['pink', 'cream', 'green', 'blue', 'red', 'mustard', 'yellow', 'lilac', 'black'];
    const wished = new Set(store.get('mm-wish', []));
    const S = { cat: 'all', min: 0, max: MAX, colors: new Set(), mats: new Set(), sort: 'featured' };

    const catEl = document.getElementById('catList');
    catEl.innerHTML = cats.map(([k, n]) => `<button class="${k === 'all' ? '' : 'sub'}" data-cat="${k}">${n}</button>`).join('');
    const catBtns = [...catEl.querySelectorAll('button')];
    catBtns.forEach(b => b.onclick = () => { S.cat = b.dataset.cat; render(); });

    document.getElementById('swatches').innerHTML = swatchList.map(c => `<button class="sw" data-c="${c}" title="${c}" style="background:${COLOR_HEX[c]}"></button>`).join('');
    document.querySelectorAll('.sw').forEach(b => b.onclick = () => {
      const c = b.dataset.c; S.colors.has(c) ? S.colors.delete(c) : S.colors.add(c); render();
    });
    document.getElementById('mats').innerHTML = mats.map(([k, n]) => `<label><input type="checkbox" value="${k}"> ${n}</label>`).join('');
    document.querySelectorAll('#mats input').forEach(i => i.onchange = () => { i.checked ? S.mats.add(i.value) : S.mats.delete(i.value); render(); });

    const lo = document.getElementById('minR'), hi = document.getElementById('maxR'), fill = document.getElementById('fill');
    const onRange = () => {
      let a = +lo.value, b = +hi.value;
      if (a > b) { [a, b] = [b, a]; }
      S.min = a; S.max = b; render();
    };
    lo.oninput = hi.oninput = onRange;
    document.getElementById('sort').onchange = e => { S.sort = e.target.value; render(); };
    document.getElementById('clear').onclick = () => {
      S.cat = 'all'; S.min = 0; S.max = MAX; S.colors.clear(); S.mats.clear();
      lo.value = 0; hi.value = MAX;
      document.querySelectorAll('#mats input').forEach(i => i.checked = false);
      render();
    };

    const heartSvg = '<svg viewBox="0 0 24 24"><path d="M12 21C5 15 3 11 3 8a4.5 4.5 0 0 1 9-1 4.5 4.5 0 0 1 9 1c0 3-2 7-9 13z"/></svg>';
    const fmt = n => '₹' + n.toLocaleString('en-IN');

    function render() {
      catBtns.forEach(b => b.classList.toggle('active', b.dataset.cat === S.cat));
      document.querySelectorAll('.sw').forEach(b => b.classList.toggle('on', S.colors.has(b.dataset.c)));
      document.getElementById('minV').textContent = fmt(S.min);
      document.getElementById('maxV').textContent = fmt(S.max);
      fill.style.left = (S.min / MAX * 100) + '%';
      fill.style.right = (100 - S.max / MAX * 100) + '%';

      let list = PRODUCTS.filter(p =>
        (S.cat === 'all' || p.cat === S.cat) &&
        p.price >= S.min && p.price <= S.max &&
        (!S.colors.size || p.colors.some(c => S.colors.has(c))) &&
        (!S.mats.size || p.materials.some(m => S.mats.has(m))));
      if (S.sort === 'low') list.sort((a, b) => a.price - b.price);
      if (S.sort === 'high') list.sort((a, b) => b.price - a.price);
      if (S.sort === 'az') list.sort((a, b) => a.name.localeCompare(b.name));

      document.getElementById('count').textContent = list.length + ' product' + (list.length === 1 ? '' : 's');
      gridEl.innerHTML = list.length ? list.map(p => `
        <article class="card">
          <div class="img"><img src="${p.img}" alt="${p.name}" loading="lazy">
            <button class="wish ${wished.has(p.id) ? 'on' : ''}" data-id="${p.id}" aria-label="Add to wishlist">${heartSvg}</button></div>
          <div class="info"><h3>${p.name}</h3><div class="price">${fmt(p.price)}</div>
            <div class="cdots">${p.colors.map(c => `<i style="background:${COLOR_HEX[c]}"></i>`).join('')}</div>
            <button class="add" data-name="${p.name}">${I.shopcart} Add to Cart</button></div>
        </article>`).join('') : '<p class="empty">No products match these filters. Try clearing them.</p>';
    }

    gridEl.addEventListener('click', e => {
      const w = e.target.closest('.wish');
      if (w) {
        const id = w.dataset.id; wished.has(id) ? wished.delete(id) : wished.add(id);
        w.classList.toggle('on'); store.set('mm-wish', [...wished]); return;
      }
      const a = e.target.closest('.add');
      if (a) { cart++; store.set('mm-cart', cart); paintCart(); toast(a.dataset.name + ' added to cart'); }
    });
    render();
  }
})();
