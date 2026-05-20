// Shopping Cart Logic
let cart = [];

function addToCart(name, price, img) {
    cart.push({ name, price, img });
    updateCartIcon();
    showNotification(`${name} added to cart!`);
}

function updateCartIcon() {
    document.getElementById('cart-count').innerText = cart.length;
}

function openCart() {
    const modal = document.getElementById('cart-modal');
    const cartItemsDiv = document.getElementById('cart-items');
    const cartTotalPrice = document.getElementById('cart-total-price');
    
    cartItemsDiv.innerHTML = '';
    let total = 0;
    
    if(cart.length === 0) {
        cartItemsDiv.innerHTML = '<p style="color: #94a3b8; text-align: center; padding: 2rem 0;">Your cart is empty.</p>';
    } else {
        cart.forEach((item, index) => {
            total += item.price;
            cartItemsDiv.innerHTML += `
                <div class="cart-item">
                    <img src="${item.img}" alt="${item.name}">
                    <div class="cart-item-info">
                        <div class="cart-item-title">${item.name}</div>
                        <div class="cart-item-price">₹${item.price.toFixed(2)}</div>
                    </div>
                    <button style="background:none;border:none;color:#ef4444;cursor:pointer;" onclick="removeFromCart(${index})">
                        <i class="fas fa-trash"></i>
                    </button>
                </div>
            `;
        });
    }
    
    cartTotalPrice.innerText = `₹${total.toFixed(2)}`;
    modal.style.display = 'block';
}

function closeCart() {
    document.getElementById('cart-modal').style.display = 'none';
}

function removeFromCart(index) {
    cart.splice(index, 1);
    updateCartIcon();
    openCart();
}

function checkout() {
    if(cart.length === 0) {
        alert("Your cart is empty!");
        return;
    }
    alert("Proceeding to checkout with " + cart.length + " items.");
    cart = [];
    updateCartIcon();
    closeCart();
}

function showNotification(msg) {
    const notif = document.createElement('div');
    notif.innerText = msg;
    notif.style.position = 'fixed';
    notif.style.bottom = '20px';
    notif.style.right = '20px';
    notif.style.background = '#10b981';
    notif.style.color = 'white';
    notif.style.padding = '1rem 2rem';
    notif.style.borderRadius = '10px';
    notif.style.boxShadow = '0 4px 12px rgba(0,0,0,0.2)';
    notif.style.zIndex = '9999';
    notif.style.opacity = '0';
    notif.style.transition = 'opacity 0.3s ease';
    
    document.body.appendChild(notif);
    
    setTimeout(() => { notif.style.opacity = '1'; }, 10);
    
    setTimeout(() => {
        notif.style.opacity = '0';
        setTimeout(() => document.body.removeChild(notif), 300);
    }, 3000);
}

function submitForm(e) {
    e.preventDefault();
    alert("Thank you for your inquiry. Our team will contact you shortly.");
    e.target.reset();
}

function toggleMenu() {
    const navLinks = document.querySelector('.nav-links');
    if (navLinks.style.display === 'flex') {
        navLinks.style.display = 'none';
    } else {
        navLinks.style.display = 'flex';
        navLinks.style.flexDirection = 'column';
        navLinks.style.position = 'absolute';
        navLinks.style.top = '70px';
        navLinks.style.right = '5%';
        navLinks.style.background = 'rgba(15, 23, 42, 0.95)';
        navLinks.style.padding = '1rem 2rem';
        navLinks.style.borderRadius = '10px';
        navLinks.style.border = '1px solid var(--glass-border)';
    }
}

// Close modal when clicking outside
window.onclick = function(event) {
    const modal = document.getElementById('cart-modal');
    if (event.target == modal) {
        closeCart();
    }
}
