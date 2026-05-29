/* ===== Intro: cortina sobe após a animação ===== */
(function () {
  const overlay = document.getElementById('intro-overlay');
  if (!overlay) return;

  // Animação dura 3.0s, cortina sobe aos 3200ms
  setTimeout(() => {
    overlay.classList.add('saindo');
    overlay.addEventListener('animationend', () => overlay.remove(), { once: true });
  }, 3200);
})();

/* ===== Sistema de abas ===== */
function ativarTab(id) {
  const pagina = document.getElementById('tab-' + id);
  if (!pagina) return;

  document.querySelectorAll('.tab-page').forEach(t => t.classList.remove('active'));
  pagina.classList.add('active');

  document.querySelectorAll('.nav-tab-link').forEach(a => {
    a.classList.toggle('active', a.dataset.tab === id);
  });

  window.history.replaceState(null, '', id === 'home' ? '/' : '#' + id);
  window.scrollTo({ top: 0, behavior: 'instant' });

  // Fecha menu mobile ao navegar
  fecharMenuMobile();
}

function fecharMenuMobile() {
  const mobileNav = document.getElementById('mobile-nav');
  const hamburger = document.getElementById('hamburger');
  if (!mobileNav) return;
  mobileNav.classList.remove('aberto');
  mobileNav.setAttribute('aria-hidden', 'true');
  if (hamburger) {
    hamburger.classList.remove('ativo');
    hamburger.querySelector('i').className = 'fa-solid fa-bars';
  }
}

// Botões de navegação da navbar e do hero
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('[data-tab]').forEach(btn => {
    btn.addEventListener('click', () => ativarTab(btn.dataset.tab));
  });

  // Abre aba correta se vier com hash na URL
  const hash = window.location.hash.slice(1);
  if (hash && document.getElementById('tab-' + hash)) {
    ativarTab(hash);
  }

  // Aplica cores dinâmicas dos ícones de categoria (via data-cor)
  document.querySelectorAll('[data-cor]').forEach(el => {
    el.style.color = el.dataset.cor;
  });

  // Inicializa página de pedido se existir
  if (document.querySelector('.pedido-item')) {
    inicializarPedido();
  }

  // ===== Hamburger menu =====
  const hamburger = document.getElementById('hamburger');
  const mobileNav = document.getElementById('mobile-nav');
  if (hamburger && mobileNav) {
    hamburger.addEventListener('click', () => {
      const aberto = mobileNav.classList.toggle('aberto');
      mobileNav.setAttribute('aria-hidden', String(!aberto));
      hamburger.classList.toggle('ativo', aberto);
      hamburger.querySelector('i').className = aberto
        ? 'fa-solid fa-xmark'
        : 'fa-solid fa-bars';
    });

    // Fecha ao clicar fora
    document.addEventListener('click', (e) => {
      if (!hamburger.contains(e.target) && !mobileNav.contains(e.target)) {
        fecharMenuMobile();
      }
    });
  }
});

/* ===== Toast ===== */
function mostrarToast(mensagem) {
  let toast = document.getElementById('toast');
  if (!toast) {
    toast = document.createElement('div');
    toast.id = 'toast';
    toast.className = 'toast';
    document.body.appendChild(toast);
  }
  toast.textContent = mensagem;
  toast.classList.add('visivel');
  clearTimeout(toast._t);
  toast._t = setTimeout(() => toast.classList.remove('visivel'), 3000);
}

/* ===== Badge do carrinho ===== */
function atualizarBadge(total) {
  const badge = document.getElementById('cart-badge');
  if (!badge) return;
  badge.textContent = total;
  badge.classList.toggle('oculto', total === 0);
}

/* ===== Adicionar ao carrinho ===== */
async function adicionarAoCarrinho(nome, quantidade = 1) {
  try {
    const resp = await fetch('/api/carrinho/adicionar', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ nome, quantidade }),
    });
    const data = await resp.json();
    if (data.sucesso) {
      atualizarBadge(data.total_itens);
      mostrarToast('🍸 ' + nome + ' ' + (window.t ? t('toast.added') : 'adicionado ao pedido!'));
    }
  } catch {
    mostrarToast(window.t ? t('toast.error_add') : 'Erro ao adicionar ao pedido.');
  }
}

/* ===== Remover do carrinho ===== */
async function removerDoCarrinho(nome, linha) {
  try {
    const resp = await fetch('/api/carrinho/remover', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ nome }),
    });
    const data = await resp.json();
    if (data.sucesso) {
      atualizarBadge(data.total_itens);
      if (linha) {
        linha.remove();
        recalcularTotal();
        verificarCarrinhoVazio();
      }
    }
  } catch {
    mostrarToast(window.t ? t('toast.error_remove') : 'Erro ao remover item.');
  }
}

/* ===== Atualizar quantidade ===== */
async function atualizarQuantidade(nome, qtd) {
  try {
    const resp = await fetch('/api/carrinho/atualizar', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ nome, quantidade: qtd }),
    });
    const data = await resp.json();
    if (data.sucesso) atualizarBadge(data.total_itens);
  } catch {
    mostrarToast(window.t ? t('toast.error_update') : 'Erro ao atualizar quantidade.');
  }
}

/* ===== Página de pedido ===== */
function inicializarPedido() {
  document.querySelectorAll('.qty-btn-menos').forEach(btn => {
    btn.addEventListener('click', () => {
      const linha = btn.closest('.pedido-item');
      const nome = linha.dataset.nome;
      const display = linha.querySelector('.qty-display');
      const subtotalEl = linha.querySelector('.pedido-item__subtotal');
      const preco = parseFloat(linha.dataset.preco);
      let qtd = parseInt(display.textContent) - 1;
      if (qtd <= 0) { removerDoCarrinho(nome, linha); return; }
      display.textContent = qtd;
      subtotalEl.textContent = '€ ' + (preco * qtd).toFixed(2);
      atualizarQuantidade(nome, qtd);
      recalcularTotal();
    });
  });

  document.querySelectorAll('.qty-btn-mais').forEach(btn => {
    btn.addEventListener('click', () => {
      const linha = btn.closest('.pedido-item');
      const nome = linha.dataset.nome;
      const display = linha.querySelector('.qty-display');
      const subtotalEl = linha.querySelector('.pedido-item__subtotal');
      const preco = parseFloat(linha.dataset.preco);
      let qtd = parseInt(display.textContent) + 1;
      display.textContent = qtd;
      subtotalEl.textContent = '€ ' + (preco * qtd).toFixed(2);
      atualizarQuantidade(nome, qtd);
      recalcularTotal();
    });
  });

  document.querySelectorAll('.pedido-item__remover').forEach(btn => {
    btn.addEventListener('click', () => {
      const linha = btn.closest('.pedido-item');
      removerDoCarrinho(linha.dataset.nome, linha);
    });
  });

  const btnLimpar = document.getElementById('btn-limpar');
  if (btnLimpar) {
    btnLimpar.addEventListener('click', async () => {
      if (!confirm(window.t ? t('order.clear_confirm') : 'Limpar o pedido inteiro?')) return;
      await fetch('/api/carrinho/limpar', { method: 'POST' });
      atualizarBadge(0);
      document.querySelectorAll('.pedido-item').forEach(l => l.remove());
      recalcularTotal();
      verificarCarrinhoVazio();
    });
  }
}

function recalcularTotal() {
  let total = 0;
  document.querySelectorAll('.pedido-item').forEach(linha => {
    const preco = parseFloat(linha.dataset.preco);
    const qtd = parseInt(linha.querySelector('.qty-display').textContent);
    total += preco * qtd;
  });
  const el = document.getElementById('total-valor');
  if (el) el.textContent = '€ ' + total.toFixed(2);
}

function verificarCarrinhoVazio() {
  const itens = document.querySelectorAll('.pedido-item');
  const wrap = document.getElementById('pedido-conteudo');
  const vazio = document.getElementById('pedido-vazio');
  if (!wrap || !vazio) return;
  if (itens.length === 0) {
    wrap.style.display = 'none';
    vazio.style.display = 'block';
  }
}
