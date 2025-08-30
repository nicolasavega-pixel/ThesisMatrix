// App.js - Main application JavaScript
document.addEventListener('DOMContentLoaded', function() {
    
    // Initialize form validation
    initializeFormValidation();
    
    // Initialize progress tracking
    initializeProgressTracking();
    
    // Initialize tooltips
    initializeTooltips();
    
    // Auto-save form data
    initializeAutoSave();
});

function initializeFormValidation() {
    // Add custom validation for forms
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
                
                // Show first invalid field
                const firstInvalid = form.querySelector(':invalid');
                if (firstInvalid) {
                    firstInvalid.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    firstInvalid.focus();
                }
            }
            form.classList.add('was-validated');
        });
        
        // Real-time validation
        const inputs = form.querySelectorAll('input, textarea, select');
        inputs.forEach(input => {
            input.addEventListener('blur', function() {
                if (input.checkValidity()) {
                    input.classList.remove('is-invalid');
                    input.classList.add('is-valid');
                } else {
                    input.classList.remove('is-valid');
                    input.classList.add('is-invalid');
                }
            });
        });
    });
}

function initializeProgressTracking() {
    // Update progress bar based on current step
    const progressBar = document.querySelector('.progress-bar');
    if (progressBar) {
        const currentStep = parseInt(progressBar.style.width) / 25; // 25% per step
        animateProgressBar(progressBar, currentStep);
    }
}

function animateProgressBar(progressBar, targetStep) {
    const targetWidth = (targetStep / 4) * 100;
    let currentWidth = 0;
    
    const animate = () => {
        currentWidth += 2;
        if (currentWidth <= targetWidth) {
            progressBar.style.width = currentWidth + '%';
            requestAnimationFrame(animate);
        }
    };
    
    animate();
}

function initializeTooltips() {
    // Initialize Bootstrap tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
}

function initializeAutoSave() {
    // Auto-save form data to localStorage
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        const inputs = form.querySelectorAll('input, textarea, select');
        
        // Load saved data
        inputs.forEach(input => {
            const savedValue = localStorage.getItem(`thesis_${input.name}`);
            if (savedValue && input.value === '') {
                input.value = savedValue;
            }
        });
        
        // Save data on input
        inputs.forEach(input => {
            input.addEventListener('input', function() {
                localStorage.setItem(`thesis_${input.name}`, input.value);
            });
        });
    });
}

// Character counter for textareas
function initializeCharacterCounters() {
    const textareas = document.querySelectorAll('textarea[data-max-length]');
    
    textareas.forEach(textarea => {
        const maxLength = parseInt(textarea.dataset.maxLength);
        const counter = document.createElement('div');
        counter.className = 'form-text text-end';
        counter.textContent = `0/${maxLength} caracteres`;
        
        textarea.parentNode.appendChild(counter);
        
        textarea.addEventListener('input', function() {
            const currentLength = textarea.value.length;
            counter.textContent = `${currentLength}/${maxLength} caracteres`;
            
            if (currentLength > maxLength * 0.9) {
                counter.classList.add('text-warning');
            } else {
                counter.classList.remove('text-warning');
            }
            
            if (currentLength >= maxLength) {
                counter.classList.add('text-danger');
                counter.classList.remove('text-warning');
            } else {
                counter.classList.remove('text-danger');
            }
        });
    });
}

// Dynamic form behavior
function setupDynamicFormBehavior() {
    // Show/hide fields based on selections
    const enfoqueSelect = document.getElementById('enfoque');
    if (enfoqueSelect) {
        enfoqueSelect.addEventListener('change', function() {
            updateMethodologyOptions(this.value);
        });
    }
    
    const disenoSelect = document.getElementById('diseno');
    if (disenoSelect) {
        disenoSelect.addEventListener('change', function() {
            updateDesignHelp(this.value);
        });
    }
}

function updateMethodologyOptions(enfoque) {
    const helpText = document.querySelector('#enfoque + .form-text');
    if (!helpText) return;
    
    const metodologias = {
        'Cuantitativo': 'Perfecto para medir variables, probar hipótesis y generalizar resultados. Usarás estadísticas y números.',
        'Cualitativo': 'Ideal para explorar percepciones, comprender experiencias y analizar significados. Usarás entrevistas, observaciones.',
        'Mixto': 'Combina lo mejor de ambos mundos. Obtienes datos numéricos y comprensión profunda del fenómeno.'
    };
    
    if (metodologias[enfoque]) {
        helpText.innerHTML = `<strong>${enfoque}:</strong> ${metodologias[enfoque]}`;
    }
}

function updateDesignHelp(diseno) {
    const helpText = document.querySelector('#diseno + .form-text');
    if (!helpText) return;
    
    const disenos = {
        'Descriptivo': 'Describe características, propiedades y perfiles de personas, grupos o fenómenos.',
        'Descriptivo-propositivo': 'Describe la situación actual y propone soluciones o mejoras.',
        'Comparativo': 'Compara grupos, situaciones o fenómenos para identificar diferencias o similitudes.',
        'Correlacional': 'Examina relaciones entre variables sin establecer causalidad.',
        'Experimental': 'Manipula variables para establecer relaciones causa-efecto.',
        'Cuasi-experimental': 'Similar al experimental pero sin control total de variables.',
        'Explicativo': 'Explica por qué ocurren los fenómenos y en qué condiciones.'
    };
    
    if (disenos[diseno]) {
        helpText.innerHTML = `<strong>${diseno}:</strong> ${disenos[diseno]}`;
    }
}

// Export functionality
function exportResults() {
    const resultsContent = document.querySelector('.container').innerHTML;
    const printWindow = window.open('', '_blank');
    
    printWindow.document.write(`
        <!DOCTYPE html>
        <html>
        <head>
            <title>Resultados - TesisPlan Asistente</title>
            <link href="https://cdn.replit.com/agent/bootstrap-agent-dark-theme.min.css" rel="stylesheet">
            <style>
                @media print {
                    .btn, .alert { display: none !important; }
                    body { background: white !important; color: black !important; }
                }
            </style>
        </head>
        <body>
            <div class="container">
                ${resultsContent}
            </div>
        </body>
        </html>
    `);
    
    printWindow.document.close();
    printWindow.print();
}

// Initialize additional features when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    initializeCharacterCounters();
    setupDynamicFormBehavior();
});
