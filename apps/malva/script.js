// Renderizar productos dinámicamente por categoría
function renderProducts() {
    const maquillajeGrid = document.getElementById('products-maquillaje');
    const accesoriosGrid = document.getElementById('products-accesorios');
    
    // Filtrar productos por categoría
    const maquillajeProducts = products.filter(p => p.category === 'maquillaje');
    const accesoriosProducts = products.filter(p => p.category === 'accesorios');
    
    // Función para renderizar un producto
    const renderProduct = (product) => `
        <div class="product-card">
            <img src="${product.img}" alt="${product.title}" class="product-image" loading="lazy" decoding="async" width="400" height="400">
            <div class="product-header">
                <span class="product-icon">${product.icon}</span>
                <h3 class="product-title">${product.title}</h3>
            </div>
            <p class="product-desc">${product.desc}</p>
        </div>
    `;
    
    // Renderizar cada categoría
    if (maquillajeGrid) {
        maquillajeGrid.innerHTML = maquillajeProducts.map(renderProduct).join('');
    }
    
    if (accesoriosGrid) {
        accesoriosGrid.innerHTML = accesoriosProducts.map(renderProduct).join('');
    }
}

// Menú móvil toggle
function initMobileMenu() {
    const menuToggle = document.querySelector('.menu-toggle');
    const nav = document.querySelector('.nav');
    
    if (menuToggle && nav) {
        menuToggle.addEventListener('click', () => {
            nav.classList.toggle('active');
        });
        
        // Cerrar menú al hacer clic en un enlace
        const navLinks = nav.querySelectorAll('.nav-link');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                nav.classList.remove('active');
            });
        });
    }
}

// Smooth scroll para enlaces internos
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
                // Cerrar menú móvil si está abierto
                const nav = document.querySelector('.nav');
                if (window.innerWidth <= 767 && nav) {
                    nav.classList.remove('active');
                }
            }
        });
    });
}

// Modal de Mystery Box
function initMysteryBoxModal() {
    const trigger = document.getElementById('mystery-box-trigger');
    const modal = document.getElementById('mystery-box-modal');
    const closeBtn = document.getElementById('modal-close');
    const videosContainer = document.getElementById('videos-container');
    
    // Array de videos de la Mystery Box
    const videos = [
        { 
            url: "videos/uno.mp4", 
            type: "video/mp4" 
        },
        { 
            url: "videos/dos.mp4", 
            type: "video/mp4" 
        },
        { 
            url: "videos/tres.mp4", 
            type: "video/mp4" 
        }
    ];
    
    if (trigger && modal) {
        trigger.addEventListener('click', () => {
            modal.classList.add('active');
            renderVideos();
        });
    }
    
    if (closeBtn) {
        closeBtn.addEventListener('click', () => {
            modal.classList.remove('active');
        });
    }
    
    if (modal) {
        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                modal.classList.remove('active');
            }
        });
    }
    
    function renderVideos() {
        if (!videosContainer) return;
        
        if (videos.length === 0) {
            videosContainer.innerHTML = '<p style="text-align: center; color: #666;">Próximamente: videos de la caja misteriosa</p>';
            return;
        }
        
        videosContainer.innerHTML = videos.map(video => {
            if (video.url.includes('youtube.com') || video.url.includes('youtu.be')) {
                // Convertir URL de YouTube a embed
                let videoId = '';
                if (video.url.includes('youtu.be')) {
                    videoId = video.url.split('youtu.be/')[1].split('?')[0];
                } else {
                    videoId = video.url.split('v=')[1].split('&')[0];
                }
                return `
                    <div class="video-wrapper">
                        <iframe src="https://www.youtube.com/embed/${videoId}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                    </div>
                `;
            } else {
                return `
                    <div class="video-wrapper">
                        <video controls>
                            <source src="${video.url}" type="${video.type || 'video/mp4'}">
                            Tu navegador no soporta el elemento de video.
                        </video>
                    </div>
                `;
            }
        }).join('');
    }
}

// Configurar enlace de WhatsApp
function initWhatsApp() {
    const whatsappLink = document.getElementById('whatsapp-link');
    
    // Reemplaza este número con el número de teléfono real
    // Formato: código de país + número (sin +, sin espacios, sin guiones)
    // Ejemplo: 584121234567 (Venezuela) o 521234567890 (México)
    const phoneNumber = '584120572857'; // CAMBIAR ESTE NÚMERO
    
    if (whatsappLink) {
        // Crear enlace de WhatsApp
        const whatsappUrl = `https://wa.me/${phoneNumber}`;
        whatsappLink.href = whatsappUrl;
        
        // Opcional: agregar mensaje predefinido
        // const message = encodeURIComponent('Hola, me interesa conocer más sobre Malva Shop');
        // whatsappLink.href = `https://wa.me/${phoneNumber}?text=${message}`;
    }
}

// Inicializar cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', () => {
    renderProducts();
    initMobileMenu();
    initSmoothScroll();
    initMysteryBoxModal();
    initWhatsApp();
});

