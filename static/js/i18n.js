/* ===== Internacionalização ===== */
const TRANSLATIONS = {
  pt: {
    // Intro
    'intro.tagline': 'Tropical Cocktails &amp; Petiscos',
    // Navbar / mobile nav
    'nav.about':   'Sobre',
    'nav.events':  'Eventos',
    'nav.menu':    'Menu',
    'nav.snacks':  'Petiscos',
    'nav.contact': 'Contato',
    'nav.booking': 'Booking',
    'nav.order':   'Pedido',
    // Hero
    'hero.about':   'About us',
    'hero.events':  'Events',
    'hero.contact': 'Contact',
    'hero.booking': 'Booking',
    'hero.menu':    'Menu',
    'hero.snacks':  'Petiscos',
    // About
    'about.title':   'Bem-vindo ao <em>Bombs Bar</em>',
    'about.intro':   'Uma casa de mixologia tropical criada para quem busca mais do que uma bebida — busca uma experiência. Nossos mixologistas combinam técnicas clássicas com ingredientes frescos, frutas exóticas e receitas autorais que surpreendem a cada gole.',
    // Events
    'events.title':   'Events <i class="fa-solid fa-fire"></i>',
    'event.1.title':  'Sunset Tropican',
    'event.1.desc':   'Final de tarde com coquetéis tropicais, frutas frescas e música lounge à beira da piscina ou rooftop.',
    'event.2.title':  'Caipirinha &amp; Samba Night',
    'event.2.desc':   'Noite com caipirinhas de sabores variados e apresentação ao vivo de samba ou bossa nova.',
    'event.3.title':  'Reggaeton &amp; Rum Party',
    'event.3.desc':   'Festa com ritmos caribenhos e drinks à base de rum, servidos em copos decorados.',
    'event.4.title':  'Havana Night',
    'event.4.desc':   'Noite temática cubana, com mojitos, daiquiris e trilha de salsa ao vivo.',
    'event.5.title':  'Exotic Fruits Experience',
    'event.5.desc':   'Degustação de coquetéis autorais feitos com frutas exóticas da estação.',
    // Menu / buttons
    'menu.title':    'Cocktails <i class="fa-solid fa-martini-glass"></i>',
    'snacks.title':  'Petiscos <i class="fa-solid fa-utensils"></i>',
    'btn.details':   'Detalhes',
    'btn.order':     'Pedido',
    // Contact
    'contact.title':   'Contato',
    'contact.address': 'Rua Exemplo, 123<br>Lisboa, Portugal',
    'contact.hours':   'Seg–Qui: 18h–02h<br>Sex–Dom: 18h–04h',
    // Booking
    'booking.title': 'Reserve Now',
    // Order page
    'order.title':         'Meu Pedido',
    'order.empty':         'Seu pedido está vazio.',
    'order.see_menu':      'Ver o menu',
    'order.unit':          '/ unid.',
    'order.total':         'Total',
    'order.glovo':         'Finalizar via Glovo',
    'order.add_more':      'Adicionar mais',
    'order.clear':         'Limpar pedido',
    'order.clear_confirm': 'Limpar o pedido inteiro?',
    // Drink detail
    'drink.back':        'Voltar ao menu',
    'drink.ingredients': 'Ingredientes',
    'drink.add':         'Adicionar ao pedido',
    // Toasts
    'toast.added':        'adicionado ao pedido!',
    'toast.error_add':    'Erro ao adicionar ao pedido. Tente novamente.',
    'toast.error_remove': 'Erro ao remover item.',
    'toast.error_update': 'Erro ao atualizar quantidade.',
  },

  en: {
    'intro.tagline': 'Tropical Cocktails &amp; Snacks',
    'nav.about':   'About',
    'nav.events':  'Events',
    'nav.menu':    'Menu',
    'nav.snacks':  'Snacks',
    'nav.contact': 'Contact',
    'nav.booking': 'Booking',
    'nav.order':   'Order',
    'hero.about':   'About us',
    'hero.events':  'Events',
    'hero.contact': 'Contact',
    'hero.booking': 'Booking',
    'hero.menu':    'Menu',
    'hero.snacks':  'Snacks',
    'about.title':   'Welcome to <em>Bombs Bar</em>',
    'about.intro':   'A tropical mixology house created for those who seek more than a drink — they seek an experience. Our mixologists blend classic techniques with fresh ingredients, exotic fruits and original recipes that surprise with every sip.',
    'events.title':   'Events <i class="fa-solid fa-fire"></i>',
    'event.1.title':  'Sunset Tropican',
    'event.1.desc':   'Late afternoon with tropical cocktails, fresh fruits and lounge music by the pool or rooftop.',
    'event.2.title':  'Caipirinha &amp; Samba Night',
    'event.2.desc':   'Evening with caipirinhas of various flavors and a live samba or bossa nova performance.',
    'event.3.title':  'Reggaeton &amp; Rum Party',
    'event.3.desc':   'Party with Caribbean rhythms and rum-based drinks, served in decorated glasses.',
    'event.4.title':  'Havana Night',
    'event.4.desc':   'Cuban-themed evening with mojitos, daiquiris and live salsa music.',
    'event.5.title':  'Exotic Fruits Experience',
    'event.5.desc':   'Tasting of original cocktails made with exotic seasonal fruits.',
    'menu.title':    'Cocktails <i class="fa-solid fa-martini-glass"></i>',
    'snacks.title':  'Snacks <i class="fa-solid fa-utensils"></i>',
    'btn.details':   'Details',
    'btn.order':     'Order',
    'contact.title':   'Contact',
    'contact.address': 'Rua Exemplo, 123<br>Lisbon, Portugal',
    'contact.hours':   'Mon–Thu: 6pm–2am<br>Fri–Sun: 6pm–4am',
    'booking.title': 'Reserve Now',
    'order.title':         'My Order',
    'order.empty':         'Your order is empty.',
    'order.see_menu':      'See the menu',
    'order.unit':          '/ unit',
    'order.total':         'Total',
    'order.glovo':         'Complete via Glovo',
    'order.add_more':      'Add more',
    'order.clear':         'Clear order',
    'order.clear_confirm': 'Clear the entire order?',
    'drink.back':        'Back to menu',
    'drink.ingredients': 'Ingredients',
    'drink.add':         'Add to order',
    'toast.added':        'added to order!',
    'toast.error_add':    'Error adding to order. Please try again.',
    'toast.error_remove': 'Error removing item.',
    'toast.error_update': 'Error updating quantity.',
  },

  it: {
    'intro.tagline': 'Cocktail Tropicali &amp; Stuzzichini',
    'nav.about':   'Chi Siamo',
    'nav.events':  'Eventi',
    'nav.menu':    'Menu',
    'nav.snacks':  'Stuzzichini',
    'nav.contact': 'Contatto',
    'nav.booking': 'Prenotazione',
    'nav.order':   'Ordine',
    'hero.about':   'Chi Siamo',
    'hero.events':  'Eventi',
    'hero.contact': 'Contatto',
    'hero.booking': 'Prenotazione',
    'hero.menu':    'Menu',
    'hero.snacks':  'Stuzzichini',
    'about.title':   'Benvenuti al <em>Bombs Bar</em>',
    'about.intro':   'Un locale di mixologia tropicale creato per chi cerca più di una bevanda — cerca un\'esperienza. I nostri mixologist fondono tecniche classiche con ingredienti freschi, frutti esotici e ricette originali che sorprendono ad ogni sorso.',
    'events.title':   'Eventi <i class="fa-solid fa-fire"></i>',
    'event.1.title':  'Sunset Tropican',
    'event.1.desc':   'Tardo pomeriggio con cocktail tropicali, frutta fresca e musica lounge a bordo piscina o sul rooftop.',
    'event.2.title':  'Caipirinha &amp; Samba Night',
    'event.2.desc':   'Serata con caipirinhas di vari gusti ed esibizione dal vivo di samba o bossa nova.',
    'event.3.title':  'Reggaeton &amp; Rum Party',
    'event.3.desc':   'Festa con ritmi caraibici e drink a base di rum, serviti in bicchieri decorati.',
    'event.4.title':  'Havana Night',
    'event.4.desc':   'Serata a tema cubano con mojito, daiquiri e musica salsa dal vivo.',
    'event.5.title':  'Exotic Fruits Experience',
    'event.5.desc':   'Degustazione di cocktail originali preparati con frutti esotici di stagione.',
    'menu.title':    'Cocktails <i class="fa-solid fa-martini-glass"></i>',
    'snacks.title':  'Stuzzichini <i class="fa-solid fa-utensils"></i>',
    'btn.details':   'Dettagli',
    'btn.order':     'Ordina',
    'contact.title':   'Contatto',
    'contact.address': 'Rua Exemplo, 123<br>Lisbona, Portogallo',
    'contact.hours':   'Lun–Gio: 18:00–02:00<br>Ven–Dom: 18:00–04:00',
    'booking.title': 'Prenota Ora',
    'order.title':         'Il Mio Ordine',
    'order.empty':         'Il tuo ordine è vuoto.',
    'order.see_menu':      'Vedi il menu',
    'order.unit':          '/ unità',
    'order.total':         'Totale',
    'order.glovo':         'Completa via Glovo',
    'order.add_more':      'Aggiungi altro',
    'order.clear':         'Svuota ordine',
    'order.clear_confirm': 'Svuotare l\'intero ordine?',
    'drink.back':        'Torna al menu',
    'drink.ingredients': 'Ingredienti',
    'drink.add':         'Aggiungi all\'ordine',
    'toast.added':        'aggiunto all\'ordine!',
    'toast.error_add':    'Errore nell\'aggiunta. Riprova.',
    'toast.error_remove': 'Errore nella rimozione.',
    'toast.error_update': 'Errore nell\'aggiornamento.',
  }
};

let currentLang = localStorage.getItem('bombs_lang') || 'pt';

function t(key) {
  return (TRANSLATIONS[currentLang] && TRANSLATIONS[currentLang][key])
    ? TRANSLATIONS[currentLang][key]
    : (TRANSLATIONS.pt[key] || key);
}

function aplicarIdioma(lang) {
  if (!TRANSLATIONS[lang]) return;
  currentLang = lang;
  localStorage.setItem('bombs_lang', lang);

  // Texto simples
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const val = TRANSLATIONS[lang][el.dataset.i18n];
    if (val !== undefined) el.textContent = val;
  });

  // Conteúdo HTML (permite tags como <strong>, <br>, <i>)
  document.querySelectorAll('[data-i18n-html]').forEach(el => {
    const val = TRANSLATIONS[lang][el.dataset.i18nHtml];
    if (val !== undefined) el.innerHTML = val;
  });

  // Botões de idioma
  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.classList.toggle('ativo', btn.dataset.lang === lang);
  });

  document.documentElement.lang = lang === 'pt' ? 'pt-br' : lang;
}

// Expõe globalmente para uso em main.js
window.t = t;

document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.addEventListener('click', () => aplicarIdioma(btn.dataset.lang));
  });
  aplicarIdioma(currentLang);
});
