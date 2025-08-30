from flask import render_template, request, session, redirect, url_for, flash, jsonify
from app import app
from thesis_generator import ThesisGenerator
import logging

@app.route('/')
def index():
    """Main landing page"""
    # Clear any existing session data
    session.clear()
    return render_template('index.html')

@app.route('/start', methods=['GET', 'POST'])
def start():
    """Step 1: Check if user has existing matrix"""
    if request.method == 'POST':
        tiene_matriz = request.form.get('tiene_matriz')
        session['tiene_matriz'] = tiene_matriz
        
        if tiene_matriz == 'ya_tengo':
            session['step'] = 'matriz_input'
            flash('Perfecto, ahora ingresa tu matriz de consistencia existente.', 'success')
            return redirect(url_for('matriz_input'))
        else:
            session['step'] = 2
            return redirect(url_for('step2'))
    
    session['step'] = 1
    return render_template('step1.html')

@app.route('/step2', methods=['GET', 'POST'])
def step2():
    """Step 2: Basic thesis information"""
    if session.get('step') != 2:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        session['tema_general'] = request.form.get('tema_general')
        session['tipo_tesis'] = request.form.get('tipo_tesis')
        session['enfoque'] = request.form.get('enfoque')
        session['diseno'] = request.form.get('diseno')
        session['step'] = 3
        return redirect(url_for('step3'))
    
    return render_template('step2.html')

@app.route('/step3', methods=['GET', 'POST'])
def step3():
    """Step 3: Delimit the topic"""
    if session.get('step') != 3:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        session['tema_delimitado'] = request.form.get('tema_delimitado')
        session['step'] = 4
        return redirect(url_for('step4'))
    
    return render_template('step3.html')

@app.route('/step4', methods=['GET', 'POST'])
def step4():
    """Step 4: Problem details"""
    if session.get('step') != 4:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        session['lugar'] = request.form.get('lugar')
        session['publico'] = request.form.get('publico')
        session['periodo'] = request.form.get('periodo')
        session['problema_mod'] = request.form.get('problema_mod')
        session['generar_matriz'] = request.form.get('generar_matriz')
        session['generar_titulos'] = request.form.get('generar_titulos')
        session['step'] = 'complete'
        return redirect(url_for('results'))
    
    return render_template('step4.html')

@app.route('/matriz_input', methods=['GET', 'POST'])
def matriz_input():
    """Step for users who already have their consistency matrix"""
    if session.get('step') != 'matriz_input':
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        # Save the matrix components
        session['matriz_existente'] = {
            'problema_general': request.form.get('problema_general'),
            'objetivo_general': request.form.get('objetivo_general'),
            'hipotesis_general': request.form.get('hipotesis_general'),
            'variables': request.form.get('variables'),
            'metodologia_enfoque': request.form.get('metodologia_enfoque'),
            'metodologia_tipo': request.form.get('metodologia_tipo'),
            'metodologia_poblacion': request.form.get('metodologia_poblacion'),
            'metodologia_muestra': request.form.get('metodologia_muestra'),
            'metodologia_tecnicas': request.form.get('metodologia_tecnicas'),
            'metodologia_instrumentos': request.form.get('metodologia_instrumentos')
        }
        
        # Set basic thesis information from the matrix
        session['tipo_tesis'] = request.form.get('tipo_tesis', 'No especificado')
        session['generar_titulos'] = request.form.get('generar_titulos', 'no')
        
        session['step'] = 'complete'
        return redirect(url_for('results'))
    
    return render_template('matriz_input.html')

@app.route('/results')
def results():
    """Display final results and generated content"""
    if session.get('step') != 'complete':
        return redirect(url_for('index'))
    
    generator = ThesisGenerator()
    
    # Generate matrix if requested, or use existing matrix
    matriz_consistencia = None
    if session.get('generar_matriz') == 'si':
        matriz_consistencia = generator.generate_consistency_matrix(session)
    elif session.get('matriz_existente'):
        # Format existing matrix to match the expected structure
        existing = session.get('matriz_existente')
        matriz_consistencia = {
            'problema_general': existing.get('problema_general'),
            'objetivo_general': existing.get('objetivo_general'),
            'hipotesis_general': existing.get('hipotesis_general'),
            'variables': existing.get('variables', '').split('\n') if existing.get('variables') else [],
            'metodologia': {
                'enfoque': existing.get('metodologia_enfoque'),
                'tipo': existing.get('metodologia_tipo'),
                'poblacion': existing.get('metodologia_poblacion'),
                'muestra': existing.get('metodologia_muestra'),
                'tecnicas': existing.get('metodologia_tecnicas'),
                'instrumentos': existing.get('metodologia_instrumentos')
            }
        }
    
    # Generate titles if requested
    titulos_propuestos = None
    if session.get('generar_titulos') == 'si':
        if session.get('matriz_existente'):
            # Generate titles based on existing matrix
            titulos_propuestos = generator.generate_titles_from_existing_matrix(session.get('matriz_existente'))
        else:
            # Generate titles from collected session data
            titulos_propuestos = generator.generate_thesis_titles(session)
    
    return render_template('results.html', 
                         matriz=matriz_consistencia,
                         titulos=titulos_propuestos,
                         session_data=session)

@app.route('/download_results')
def download_results():
    """Download results as a formatted document"""
    if session.get('step') != 'complete':
        return redirect(url_for('index'))
    
    # This would generate a downloadable document
    # For now, we'll redirect back to results
    flash('Funcionalidad de descarga en desarrollo', 'info')
    return redirect(url_for('results'))

@app.route('/reset')
def reset():
    """Reset the session and start over"""
    session.clear()
    return redirect(url_for('index'))
