/**
 * Truong Gia Landing Page - Main JavaScript
 * Mobile menu, smooth scroll, form handling
 */

document.addEventListener('DOMContentLoaded', function() {
    // Mobile Menu Toggle
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');

    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', function() {
            mobileMenu.classList.toggle('hidden');
            // Toggle hamburger to X icon
            const icon = mobileMenuBtn.querySelector('svg');
            if (icon) {
                icon.classList.toggle('rotate-90');
            }
        });

        // Close mobile menu when clicking a link
        mobileMenu.querySelectorAll('a').forEach(function(link) {
            link.addEventListener('click', function() {
                mobileMenu.classList.add('hidden');
            });
        });
    }

    // Smooth Scroll for Anchor Links
    document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
        anchor.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                e.preventDefault();
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Navbar Background on Scroll
    const navbar = document.getElementById('navbar');
    if (navbar) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                navbar.classList.add('shadow-lg');
                navbar.classList.remove('shadow-md');
            } else {
                navbar.classList.remove('shadow-lg');
                navbar.classList.add('shadow-md');
            }
        });
    }

    // Contact Form Handling
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            // Form validation
            const name = document.getElementById('name');
            const phone = document.getElementById('phone');
            const service = document.getElementById('service');

            let isValid = true;

            // Simple validation
            if (name && name.value.trim() === '') {
                showError(name, 'Vui lòng nhập họ tên');
                isValid = false;
            } else if (name) {
                clearError(name);
            }

            if (phone && !isValidPhone(phone.value)) {
                showError(phone, 'Số điện thoại không hợp lệ');
                isValid = false;
            } else if (phone) {
                clearError(phone);
            }

            if (service && service.value === '') {
                showError(service, 'Vui lòng chọn dịch vụ');
                isValid = false;
            } else if (service) {
                clearError(service);
            }

            if (!isValid) {
                e.preventDefault();
            }
        });
    }

    // Phone number validation (Vietnamese mobile/landline format)
    function isValidPhone(phone) {
        const cleaned = phone.replace(/\s/g, '');
        // Vietnamese mobile: 03x, 05x, 07x, 08x, 09x (10 digits)
        // Vietnamese landline: 02x (11 digits)
        const mobileRegex = /^(0[35789][0-9]{8})$|^(\+84[35789][0-9]{8})$/;
        const landlineRegex = /^(02[0-9]{9})$|^(\+842[0-9]{9})$/;
        return mobileRegex.test(cleaned) || landlineRegex.test(cleaned);
    }

    // Show form error
    function showError(input, message) {
        const formGroup = input.parentElement;
        let errorEl = formGroup.querySelector('.error-message');

        if (!errorEl) {
            errorEl = document.createElement('p');
            errorEl.className = 'error-message text-red-400 text-sm mt-1';
            formGroup.appendChild(errorEl);
        }

        errorEl.textContent = message;
        input.classList.add('border-red-500');
        input.classList.remove('border-white/30');
    }

    // Clear form error
    function clearError(input) {
        const formGroup = input.parentElement;
        const errorEl = formGroup.querySelector('.error-message');

        if (errorEl) {
            errorEl.remove();
        }

        input.classList.remove('border-red-500');
        input.classList.add('border-white/30');
    }

    // Scroll Animation Observer (for fade-in effects)
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-fade-in');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe elements with data-animate attribute
    document.querySelectorAll('[data-animate]').forEach(function(el) {
        observer.observe(el);
    });
});

