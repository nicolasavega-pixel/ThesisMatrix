class ThesisGenerator:
    """Generates thesis-related content based on user input"""
    
    def generate_consistency_matrix(self, session_data):
        """Generate a consistency matrix based on the collected information"""
        
        # Extract relevant information
        tema = session_data.get('tema_delimitado', session_data.get('tema_general', ''))
        enfoque = session_data.get('enfoque', '')
        diseno = session_data.get('diseno', '')
        problema = session_data.get('problema_mod', '')
        
        # Generate problem formulation
        problema_general = f"¿{problema}?"
        
        # Generate objective based on design
        if 'descriptivo' in diseno.lower():
            objetivo_general = f"Describir {tema.lower()}"
        elif 'experimental' in diseno.lower():
            objetivo_general = f"Determinar el efecto de {tema.lower()}"
        elif 'comparativo' in diseno.lower():
            objetivo_general = f"Comparar {tema.lower()}"
        else:
            objetivo_general = f"Analizar {tema.lower()}"
        
        # Generate hypothesis based on approach
        if enfoque.lower() == 'cuantitativo':
            hipotesis = f"Existe una relación significativa en {tema.lower()}"
        elif enfoque.lower() == 'cualitativo':
            hipotesis = "No aplica (estudio cualitativo)"
        else:
            hipotesis = f"Se espera encontrar patrones significativos en {tema.lower()}"
        
        # Generate variables
        if enfoque.lower() == 'cuantitativo':
            variables = ["Variable independiente: (A definir según el tema)",
                        "Variable dependiente: (A definir según el tema)",
                        "Variables de control: (A definir según el contexto)"]
        else:
            variables = ["Categorías de análisis: (A definir según el tema)",
                        "Subcategorías: (A definir durante el análisis)"]
        
        # Generate methodology
        metodologia = {
            'enfoque': enfoque.title(),
            'tipo': diseno.title(),
            'poblacion': session_data.get('publico', 'A definir'),
            'muestra': 'A determinar según criterios de inclusión/exclusión',
            'tecnicas': 'A definir según el enfoque metodológico',
            'instrumentos': 'A desarrollar según las técnicas seleccionadas'
        }
        
        matriz = {
            'problema_general': problema_general,
            'objetivo_general': objetivo_general,
            'hipotesis_general': hipotesis,
            'variables': variables,
            'metodologia': metodologia,
            'lugar': session_data.get('lugar', ''),
            'periodo': session_data.get('periodo', '')
        }
        
        return matriz
    
    def generate_thesis_titles(self, session_data):
        """Generate 5 thesis title suggestions with justifications"""
        
        tema = session_data.get('tema_delimitado', session_data.get('tema_general', ''))
        enfoque = session_data.get('enfoque', '')
        diseno = session_data.get('diseno', '')
        lugar = session_data.get('lugar', '')
        periodo = session_data.get('periodo', '')
        
        # Base title components
        accion_palabras = {
            'descriptivo': ['Análisis', 'Caracterización', 'Descripción', 'Estudio', 'Diagnóstico'],
            'experimental': ['Efecto', 'Impacto', 'Influencia', 'Evaluación experimental', 'Análisis experimental'],
            'comparativo': ['Análisis comparativo', 'Estudio comparativo', 'Comparación', 'Evaluación comparativa', 'Contraste'],
            'correlacional': ['Relación', 'Correlación', 'Asociación', 'Vínculo', 'Correspondencia']
        }
        
        # Determine action words based on design
        design_key = next((key for key in accion_palabras.keys() if key in diseno.lower()), 'descriptivo')
        acciones = accion_palabras[design_key]
        
        titulos = []
        
        for i, accion in enumerate(acciones):
            if lugar and periodo:
                titulo = f"{accion} de {tema} en {lugar} durante el período {periodo}"
            elif lugar:
                titulo = f"{accion} de {tema} en {lugar}"
            elif periodo:
                titulo = f"{accion} de {tema} durante el período {periodo}"
            else:
                titulo = f"{accion} de {tema}"
            
            # Add approach specification for mixed methods
            if enfoque.lower() == 'mixto':
                titulo += f" - Enfoque mixto"
            
            justificacion = self._generate_title_justification(titulo, enfoque, diseno, i+1)
            
            titulos.append({
                'numero': i + 1,
                'titulo': titulo,
                'justificacion': justificacion
            })
        
        return titulos
    
    def generate_operationalization_matrix(self, session_data):
        """Generate operationalization matrix from step-by-step data"""
        
        tema = session_data.get('tema_delimitado', session_data.get('tema_general', ''))
        enfoque = session_data.get('enfoque', '')
        diseno = session_data.get('diseno', '')
        
        # Create basic operationalization structure
        matriz_operacionalizacion = []
        
        if enfoque.lower() == 'cuantitativo':
            # Quantitative approach - focus on variables
            matriz_operacionalizacion = [
                {
                    'variable': 'Variable Independiente',
                    'definicion_conceptual': f'Concepto teórico relacionado con {tema.lower()}',
                    'definicion_operacional': 'Definir cómo se medirá esta variable',
                    'dimensiones': ['Dimensión 1', 'Dimensión 2'],
                    'indicadores': ['Indicador 1.1', 'Indicador 1.2', 'Indicador 2.1', 'Indicador 2.2'],
                    'elementos_items': ['Item 1', 'Item 2', 'Item 3', 'Item 4'],
                    'escala': 'Escala de Likert (1-5)',
                    'instrumento': 'Cuestionario'
                },
                {
                    'variable': 'Variable Dependiente',
                    'definicion_conceptual': f'Resultado esperado en {tema.lower()}',
                    'definicion_operacional': 'Definir cómo se medirá el resultado',
                    'dimensiones': ['Dimensión A', 'Dimensión B'],
                    'indicadores': ['Indicador A.1', 'Indicador A.2', 'Indicador B.1', 'Indicador B.2'],
                    'elementos_items': ['Item A', 'Item B', 'Item C', 'Item D'],
                    'escala': 'Escala numérica',
                    'instrumento': 'Prueba/Test'
                }
            ]
        else:
            # Qualitative or mixed approach - focus on categories
            matriz_operacionalizacion = [
                {
                    'categoria': 'Categoría Principal 1',
                    'definicion_conceptual': f'Primera categoría de análisis para {tema.lower()}',
                    'subcategorias': ['Subcategoría 1.1', 'Subcategoría 1.2'],
                    'indicadores': ['Conducta observable 1', 'Conducta observable 2'],
                    'preguntas_guia': ['¿Pregunta 1?', '¿Pregunta 2?'],
                    'tecnica': 'Entrevista semiestructurada',
                    'instrumento': 'Guía de entrevista'
                },
                {
                    'categoria': 'Categoría Principal 2',
                    'definicion_conceptual': f'Segunda categoría de análisis para {tema.lower()}',
                    'subcategorias': ['Subcategoría 2.1', 'Subcategoría 2.2'],
                    'indicadores': ['Conducta observable 3', 'Conducta observable 4'],
                    'preguntas_guia': ['¿Pregunta 3?', '¿Pregunta 4?'],
                    'tecnica': 'Observación participante',
                    'instrumento': 'Ficha de observación'
                }
            ]
        
        return matriz_operacionalizacion
    
    def generate_operationalization_matrix_from_existing(self, matriz_existente):
        """Generate operationalization matrix from existing consistency matrix"""
        
        variables_text = matriz_existente.get('variables', '')
        enfoque = matriz_existente.get('metodologia_enfoque', '')
        
        # Parse variables from the text
        variables_list = [var.strip() for var in variables_text.split('\n') if var.strip()]
        
        matriz_operacionalizacion = []
        
        if enfoque.lower() == 'cuantitativo':
            # Generate for each variable mentioned
            for i, variable in enumerate(variables_list[:3]):  # Limit to 3 variables
                if 'independiente' in variable.lower():
                    var_type = 'Variable Independiente'
                elif 'dependiente' in variable.lower():
                    var_type = 'Variable Dependiente'
                else:
                    var_type = f'Variable {i+1}'
                
                matriz_operacionalizacion.append({
                    'variable': var_type,
                    'definicion_conceptual': f'Definición teórica de {variable.lower()}',
                    'definicion_operacional': f'Cómo se medirá {variable.lower()} en el estudio',
                    'dimensiones': [f'Dimensión {chr(65+i*2)}', f'Dimensión {chr(65+i*2+1)}'],
                    'indicadores': [f'Indicador {chr(65+i*2)}.1', f'Indicador {chr(65+i*2)}.2', 
                                  f'Indicador {chr(65+i*2+1)}.1', f'Indicador {chr(65+i*2+1)}.2'],
                    'elementos_items': [f'Ítem {i*4+1}', f'Ítem {i*4+2}', f'Ítem {i*4+3}', f'Ítem {i*4+4}'],
                    'escala': 'Escala de Likert (1-5)' if i == 0 else 'Escala numérica',
                    'instrumento': 'Cuestionario' if i == 0 else 'Test/Prueba'
                })
        else:
            # Qualitative approach
            categorias_base = ['Experiencias', 'Percepciones', 'Comportamientos']
            
            for i, categoria in enumerate(categorias_base[:3]):
                matriz_operacionalizacion.append({
                    'categoria': f'Categoría: {categoria}',
                    'definicion_conceptual': f'Análisis de {categoria.lower()} relacionadas con la investigación',
                    'subcategorias': [f'{categoria[:-1]} directa', f'{categoria[:-1]} indirecta'],
                    'indicadores': [f'Manifestación {i*2+1}', f'Manifestación {i*2+2}'],
                    'preguntas_guia': [f'¿Cómo describes {categoria.lower()}?', f'¿Qué factores influyen en {categoria.lower()}?'],
                    'tecnica': 'Entrevista a profundidad' if i == 0 else 'Grupo focal',
                    'instrumento': 'Guía de entrevista' if i == 0 else 'Guía de discusión'
                })
        
        return matriz_operacionalizacion
    
    def _generate_title_justification(self, titulo, enfoque, diseno, numero):
        """Generate justification for each title"""
        
        justificaciones = {
            1: f"Este título es directo y específico, claramente indica el {enfoque} como enfoque metodológico y el diseño {diseno}. Es académicamente sólido y fácil de entender.",
            2: f"Versión más formal que enfatiza el rigor metodológico. Apropiado para {enfoque} y permite flexibilidad en el desarrollo del diseño {diseno}.",
            3: f"Título equilibrado que combina precisión académica con claridad. Ideal para investigaciones con enfoque {enfoque} y diseño {diseno}.",
            4: f"Enfoque más descriptivo que resalta el alcance de la investigación. Especialmente adecuado para estudios {enfoque} con metodología {diseno}.",
            5: f"Versión concisa pero completa que facilita la comprensión del tema. Apropiado para el enfoque {enfoque} seleccionado y el diseño {diseno}."
        }
        
        return justificaciones.get(numero, "Título bien estructurado que refleja el enfoque y diseño metodológico seleccionado.")
    
    def generate_titles_from_existing_matrix(self, matriz_existente):
        """Generate 5 thesis title suggestions based on existing matrix"""
        
        # Extract key information from the existing matrix
        objetivo = matriz_existente.get('objetivo_general', '')
        problema = matriz_existente.get('problema_general', '')
        enfoque = matriz_existente.get('metodologia_enfoque', '')
        tipo_diseno = matriz_existente.get('metodologia_tipo', '')
        
        # Try to extract the main topic from objective or problem
        tema_principal = ""
        if objetivo:
            # Extract topic from objective (usually after the action verb)
            words = objetivo.split()
            if len(words) > 2:
                tema_principal = ' '.join(words[1:])  # Skip the action verb
        elif problema:
            # Extract from problem statement
            problema_clean = problema.replace('¿', '').replace('?', '')
            words = problema_clean.split()
            if len(words) > 5:
                tema_principal = ' '.join(words[2:])  # Skip common question words
        
        if not tema_principal:
            tema_principal = "la investigación planteada"
        
        # Generate title variations based on the methodology
        base_actions = ['Análisis', 'Estudio', 'Investigación', 'Evaluación', 'Examen']
        
        if 'experimental' in tipo_diseno.lower():
            base_actions = ['Evaluación experimental', 'Análisis experimental', 'Estudio experimental', 'Investigación experimental', 'Examen experimental']
        elif 'descriptivo' in tipo_diseno.lower():
            base_actions = ['Análisis descriptivo', 'Estudio descriptivo', 'Caracterización', 'Descripción', 'Diagnóstico']
        elif 'comparativo' in tipo_diseno.lower():
            base_actions = ['Análisis comparativo', 'Estudio comparativo', 'Comparación', 'Evaluación comparativa', 'Contraste']
        
        titulos = []
        
        for i, accion in enumerate(base_actions):
            if enfoque.lower() == 'mixto':
                titulo = f"{accion} de {tema_principal.lower()} - Enfoque mixto"
            else:
                titulo = f"{accion} de {tema_principal.lower()}"
            
            justificacion = f"Este título refleja adecuadamente el {tipo_diseno.lower()} planteado en tu matriz de consistencia, manteniendo coherencia con tu {enfoque.lower()} metodológico y el objetivo general establecido."
            
            titulos.append({
                'numero': i + 1,
                'titulo': titulo,
                'justificacion': justificacion
            })
        
        return titulos
    
    def generate_operationalization_matrix(self, session_data):
        """Generate operationalization matrix from step-by-step data"""
        
        tema = session_data.get('tema_delimitado', session_data.get('tema_general', ''))
        enfoque = session_data.get('enfoque', '')
        diseno = session_data.get('diseno', '')
        
        # Create basic operationalization structure
        matriz_operacionalizacion = []
        
        if enfoque.lower() == 'cuantitativo':
            # Quantitative approach - focus on variables
            matriz_operacionalizacion = [
                {
                    'variable': 'Variable Independiente',
                    'definicion_conceptual': f'Concepto teórico relacionado con {tema.lower()}',
                    'definicion_operacional': 'Definir cómo se medirá esta variable',
                    'dimensiones': ['Dimensión 1', 'Dimensión 2'],
                    'indicadores': ['Indicador 1.1', 'Indicador 1.2', 'Indicador 2.1', 'Indicador 2.2'],
                    'elementos_items': ['Item 1', 'Item 2', 'Item 3', 'Item 4'],
                    'escala': 'Escala de Likert (1-5)',
                    'instrumento': 'Cuestionario'
                },
                {
                    'variable': 'Variable Dependiente',
                    'definicion_conceptual': f'Resultado esperado en {tema.lower()}',
                    'definicion_operacional': 'Definir cómo se medirá el resultado',
                    'dimensiones': ['Dimensión A', 'Dimensión B'],
                    'indicadores': ['Indicador A.1', 'Indicador A.2', 'Indicador B.1', 'Indicador B.2'],
                    'elementos_items': ['Item A', 'Item B', 'Item C', 'Item D'],
                    'escala': 'Escala numérica',
                    'instrumento': 'Prueba/Test'
                }
            ]
        else:
            # Qualitative or mixed approach - focus on categories
            matriz_operacionalizacion = [
                {
                    'categoria': 'Categoría Principal 1',
                    'definicion_conceptual': f'Primera categoría de análisis para {tema.lower()}',
                    'subcategorias': ['Subcategoría 1.1', 'Subcategoría 1.2'],
                    'indicadores': ['Conducta observable 1', 'Conducta observable 2'],
                    'preguntas_guia': ['¿Pregunta 1?', '¿Pregunta 2?'],
                    'tecnica': 'Entrevista semiestructurada',
                    'instrumento': 'Guía de entrevista'
                },
                {
                    'categoria': 'Categoría Principal 2',
                    'definicion_conceptual': f'Segunda categoría de análisis para {tema.lower()}',
                    'subcategorias': ['Subcategoría 2.1', 'Subcategoría 2.2'],
                    'indicadores': ['Conducta observable 3', 'Conducta observable 4'],
                    'preguntas_guia': ['¿Pregunta 3?', '¿Pregunta 4?'],
                    'tecnica': 'Observación participante',
                    'instrumento': 'Ficha de observación'
                }
            ]
        
        return matriz_operacionalizacion
    
    def generate_operationalization_matrix_from_existing(self, matriz_existente):
        """Generate operationalization matrix from existing consistency matrix"""
        
        variables_text = matriz_existente.get('variables', '')
        enfoque = matriz_existente.get('metodologia_enfoque', '')
        
        # Parse variables from the text
        variables_list = [var.strip() for var in variables_text.split('\n') if var.strip()]
        
        matriz_operacionalizacion = []
        
        if enfoque.lower() == 'cuantitativo':
            # Generate for each variable mentioned
            for i, variable in enumerate(variables_list[:3]):  # Limit to 3 variables
                if 'independiente' in variable.lower():
                    var_type = 'Variable Independiente'
                elif 'dependiente' in variable.lower():
                    var_type = 'Variable Dependiente'
                else:
                    var_type = f'Variable {i+1}'
                
                matriz_operacionalizacion.append({
                    'variable': var_type,
                    'definicion_conceptual': f'Definición teórica de {variable.lower()}',
                    'definicion_operacional': f'Cómo se medirá {variable.lower()} en el estudio',
                    'dimensiones': [f'Dimensión {chr(65+i*2)}', f'Dimensión {chr(65+i*2+1)}'],
                    'indicadores': [f'Indicador {chr(65+i*2)}.1', f'Indicador {chr(65+i*2)}.2', 
                                  f'Indicador {chr(65+i*2+1)}.1', f'Indicador {chr(65+i*2+1)}.2'],
                    'elementos_items': [f'Ítem {i*4+1}', f'Ítem {i*4+2}', f'Ítem {i*4+3}', f'Ítem {i*4+4}'],
                    'escala': 'Escala de Likert (1-5)' if i == 0 else 'Escala numérica',
                    'instrumento': 'Cuestionario' if i == 0 else 'Test/Prueba'
                })
        else:
            # Qualitative approach
            categorias_base = ['Experiencias', 'Percepciones', 'Comportamientos']
            
            for i, categoria in enumerate(categorias_base[:3]):
                matriz_operacionalizacion.append({
                    'categoria': f'Categoría: {categoria}',
                    'definicion_conceptual': f'Análisis de {categoria.lower()} relacionadas con la investigación',
                    'subcategorias': [f'{categoria[:-1]} directa', f'{categoria[:-1]} indirecta'],
                    'indicadores': [f'Manifestación {i*2+1}', f'Manifestación {i*2+2}'],
                    'preguntas_guia': [f'¿Cómo describes {categoria.lower()}?', f'¿Qué factores influyen en {categoria.lower()}?'],
                    'tecnica': 'Entrevista a profundidad' if i == 0 else 'Grupo focal',
                    'instrumento': 'Guía de entrevista' if i == 0 else 'Guía de discusión'
                })
        
        return matriz_operacionalizacion
