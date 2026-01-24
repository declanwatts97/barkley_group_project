const mobileMenuButton = document.getElementById('mobile-menu-button');
        const mobileMenu = document.getElementById('mobile-menu');
        const openIcon = document.getElementById('open-icon');
        const closeIcon = document.getElementById('close-icon');

        mobileMenuButton.addEventListener('click', () => {
            // Toggle the 'hidden' class on the menu
            mobileMenu.classList.toggle('hidden');
            
            // Toggle the visibility of the open/close icons
            openIcon.classList.toggle('hidden');
            openIcon.classList.toggle('block');
            closeIcon.classList.toggle('hidden');
            closeIcon.classList.toggle('block');
            
            // Update ARIA attribute for accessibility
            const isExpanded = mobileMenuButton.getAttribute('aria-expanded') === 'true';
            mobileMenuButton.setAttribute('aria-expanded', !isExpanded);
        });