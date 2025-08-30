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
            # Generate intelligent variable suggestions based on topic
            variables_sugeridas = self._generate_variable_suggestions(tema.lower())
            
            matriz_operacionalizacion = [
                {
                    'variable': f'Variable Independiente: {variables_sugeridas["independiente"]["nombre"]}',
                    'definicion_conceptual': variables_sugeridas["independiente"]["definicion_conceptual"],
                    'definicion_operacional': variables_sugeridas["independiente"]["definicion_operacional"],
                    'dimensiones': variables_sugeridas["independiente"]["dimensiones"],
                    'indicadores': variables_sugeridas["independiente"]["indicadores"],
                    'elementos_items': variables_sugeridas["independiente"]["items"],
                    'escala': 'Escala de Likert (1-5)',
                    'instrumento': 'Cuestionario'
                },
                {
                    'variable': f'Variable Dependiente: {variables_sugeridas["dependiente"]["nombre"]}',
                    'definicion_conceptual': variables_sugeridas["dependiente"]["definicion_conceptual"],
                    'definicion_operacional': variables_sugeridas["dependiente"]["definicion_operacional"],
                    'dimensiones': variables_sugeridas["dependiente"]["dimensiones"],
                    'indicadores': variables_sugeridas["dependiente"]["indicadores"],
                    'elementos_items': variables_sugeridas["dependiente"]["items"],
                    'escala': 'Escala numérica (0-20)',
                    'instrumento': 'Test/Evaluación'
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
    
    def _generate_variable_suggestions(self, tema):
        """Generate intelligent variable suggestions based on topic"""
        
        # Common topic patterns and their suggested variables
        variable_patterns = {
            'tecnolog': {
                'independiente': {
                    'nombre': 'Uso de tecnologías digitales',
                    'definicion_conceptual': 'Nivel de utilización de herramientas tecnológicas digitales en el proceso estudiado',
                    'definicion_operacional': 'Frecuencia y tipos de tecnologías utilizadas medidas a través de cuestionario',
                    'dimensiones': ['Frecuencia de uso', 'Tipos de tecnología'],
                    'indicadores': ['Horas diarias de uso', 'Número de aplicaciones utilizadas', 'Nivel de competencia digital'],
                    'items': ['¿Con qué frecuencia utiliza dispositivos digitales?', '¿Qué tipos de software maneja?', '¿Cuál es su nivel de competencia tecnológica?']
                },
                'dependiente': {
                    'nombre': 'Rendimiento/Productividad',
                    'definicion_conceptual': 'Nivel de eficacia y eficiencia en el desempeño de actividades',
                    'definicion_operacional': 'Puntaje obtenido en indicadores de desempeño medidos cuantitativamente',
                    'dimensiones': ['Eficacia', 'Eficiencia'],
                    'indicadores': ['Tareas completadas', 'Tiempo empleado', 'Calidad de resultados'],
                    'items': ['Número de tareas completadas por día', 'Tiempo promedio por tarea', 'Calificación de calidad del trabajo']
                }
            },
            'educaci': {
                'independiente': {
                    'nombre': 'Método de enseñanza',
                    'definicion_conceptual': 'Estrategia pedagógica utilizada para facilitar el aprendizaje',
                    'definicion_operacional': 'Tipo de metodología aplicada clasificada según enfoque pedagógico',
                    'dimensiones': ['Tipo de metodología', 'Frecuencia de aplicación'],
                    'indicadores': ['Método tradicional vs. activo', 'Horas de aplicación semanal', 'Recursos utilizados'],
                    'items': ['¿Qué metodología de enseñanza utiliza principalmente?', '¿Con qué frecuencia aplica métodos activos?', '¿Qué recursos pedagógicos emplea?']
                },
                'dependiente': {
                    'nombre': 'Rendimiento académico',
                    'definicion_conceptual': 'Nivel de logro de los objetivos educativos por parte del estudiante',
                    'definicion_operacional': 'Calificaciones numéricas obtenidas en evaluaciones académicas',
                    'dimensiones': ['Notas cuantitativas', 'Competencias desarrolladas'],
                    'indicadores': ['Promedio de calificaciones', 'Número de competencias logradas', 'Nivel de comprensión'],
                    'items': ['Calificación promedio del período', 'Número de objetivos alcanzados', 'Nivel de dominio de competencias']
                }
            },
            'salud': {
                'independiente': {
                    'nombre': 'Programa de intervención',
                    'definicion_conceptual': 'Conjunto de actividades estructuradas dirigidas a mejorar la condición de salud',
                    'definicion_operacional': 'Tipo y duración del programa aplicado según protocolo establecido',
                    'dimensiones': ['Tipo de intervención', 'Duración del programa'],
                    'indicadores': ['Modalidad de intervención', 'Número de sesiones', 'Tiempo por sesión'],
                    'items': ['¿Qué tipo de programa siguió?', '¿Cuántas sesiones completó?', '¿Cuál fue la duración promedio por sesión?']
                },
                'dependiente': {
                    'nombre': 'Estado de salud',
                    'definicion_conceptual': 'Condición física, mental y social de bienestar del individuo',
                    'definicion_operacional': 'Puntajes obtenidos en escalas estandarizadas de evaluación de salud',
                    'dimensiones': ['Salud física', 'Salud mental'],
                    'indicadores': ['Índice de masa corporal', 'Niveles de estrés', 'Calidad de vida percibida'],
                    'items': ['Medición de peso y talla', 'Escala de estrés percibido', 'Cuestionario de calidad de vida']
                }
            },
            'empres': {
                'independiente': {
                    'nombre': 'Estrategia organizacional',
                    'definicion_conceptual': 'Plan de acción implementado para alcanzar objetivos organizacionales',
                    'definicion_operacional': 'Tipo de estrategia aplicada clasificada según modelo teórico',
                    'dimensiones': ['Tipo de estrategia', 'Nivel de implementación'],
                    'indicadores': ['Modalidad estratégica', 'Recursos asignados', 'Tiempo de implementación'],
                    'items': ['¿Qué tipo de estrategia implementó?', '¿Qué recursos destinó a la estrategia?', '¿Cuánto tiempo dedicó a la implementación?']
                },
                'dependiente': {
                    'nombre': 'Desempeño organizacional',
                    'definicion_conceptual': 'Nivel de logro de los objetivos y metas organizacionales',
                    'definicion_operacional': 'Indicadores cuantitativos de rendimiento empresarial',
                    'dimensiones': ['Rentabilidad', 'Productividad'],
                    'indicadores': ['Retorno sobre inversión', 'Productividad laboral', 'Satisfacción del cliente'],
                    'items': ['Porcentaje de ROI', 'Unidades producidas por empleado', 'Índice de satisfacción del cliente']
                }
            }
        }
        
        # Find matching pattern
        for pattern, variables in variable_patterns.items():
            if pattern in tema:
                return variables
        
        # Default variables if no pattern matches
        return {
            'independiente': {
                'nombre': 'Factor de estudio principal',
                'definicion_conceptual': f'Principal elemento que se manipula o analiza en {tema}',
                'definicion_operacional': 'Medición operativa del factor principal según instrumentos establecidos',
                'dimensiones': ['Dimensión primaria', 'Dimensión secundaria'],
                'indicadores': ['Indicador principal 1', 'Indicador principal 2', 'Indicador secundario 1'],
                'items': ['¿Cuál es el nivel del factor principal?', '¿Con qué frecuencia se presenta?', '¿Qué intensidad tiene?']
            },
            'dependiente': {
                'nombre': 'Resultado esperado',
                'definicion_conceptual': f'Efecto o resultado que se busca medir en {tema}',
                'definicion_operacional': 'Puntuación obtenida en la medición del resultado principal',
                'dimensiones': ['Efectividad', 'Impacto'],
                'indicadores': ['Nivel de efectividad', 'Magnitud del impacto', 'Duración del efecto'],
                'items': ['Puntaje de efectividad obtenido', 'Nivel de impacto medido', 'Duración del efecto observado']
            }
        }
    
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
    
    def generate_consistency_matrix_from_existing(self, matriz_data):
        """Generate consistency matrix from existing matrix data"""
        
        # Extract the main components
        problema_general = matriz_data.get('problema_general', '')
        objetivo_general = matriz_data.get('objetivo_general', '')
        hipotesis_general = matriz_data.get('hipotesis', '')
        variables_text = matriz_data.get('variables', '')
        
        metodologia_enfoque = matriz_data.get('metodologia_enfoque', '')
        metodologia_tipo = matriz_data.get('metodologia_tipo', '')
        metodologia_poblacion = matriz_data.get('metodologia_poblacion', '')
        metodologia_muestra = matriz_data.get('metodologia_muestra', '')
        metodologia_tecnicas = matriz_data.get('metodologia_tecnicas', '')
        metodologia_instrumentos = matriz_data.get('metodologia_instrumentos', '')
        
        # Parse variables from text into a list
        variables_list = [var.strip() for var in variables_text.split('\n') if var.strip()]
        
        # Create the methodology dictionary
        metodologia = {
            'enfoque': metodologia_enfoque,
            'tipo': metodologia_tipo,
            'poblacion': metodologia_poblacion,
            'muestra': metodologia_muestra,
            'tecnicas': metodologia_tecnicas,
            'instrumentos': metodologia_instrumentos
        }
        
        matriz = {
            'problema_general': problema_general,
            'objetivo_general': objetivo_general,
            'hipotesis_general': hipotesis_general,
            'variables': variables_list,
            'metodologia': metodologia,
            'metodologia_enfoque': metodologia_enfoque  # Also store separately for easy access
        }
        
        return matriz
    
    def generate_thesis_titles_from_existing(self, matriz_data):
        """Generate thesis titles from existing consistency matrix"""
        
        # Extract information from the existing matrix
        objetivo = matriz_data.get('objetivo_general', '')
        enfoque = matriz_data.get('metodologia_enfoque', '')
        tipo_diseno = matriz_data.get('metodologia_tipo', '')
        
        # Try to extract the main topic from the objective
        tema_principal = objetivo
        if 'analizar' in objetivo.lower():
            tema_principal = objetivo.lower().replace('analizar', '').strip()
        elif 'estudiar' in objetivo.lower():
            tema_principal = objetivo.lower().replace('estudiar', '').strip()
        elif 'evaluar' in objetivo.lower():
            tema_principal = objetivo.lower().replace('evaluar', '').strip()
        elif 'determinar' in objetivo.lower():
            tema_principal = objetivo.lower().replace('determinar', '').strip()
        elif 'describir' in objetivo.lower():
            tema_principal = objetivo.lower().replace('describir', '').strip()
        else:
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
    
    def _generate_title_justification(self, titulo, enfoque, diseno, numero):
        """Generate justification for a specific title"""
        
        justifications = [
            f"Este título es directo y específico, reflejando claramente el {enfoque.lower()} metodológico y el {diseno.lower()} de investigación propuesto.",
            f"La formulación de este título permite delimitar el alcance del estudio y es coherente con el {diseno.lower()} planteado en tu metodología.",
            f"Este título mantiene un equilibrio entre precisión científica y claridad, adecuado para un {enfoque.lower()} de investigación.",
            f"La estructura de este título facilita la comprensión del propósito del estudio y se alinea con los estándares académicos del {diseno.lower()}.",
            f"Este título es conciso pero descriptivo, cumpliendo con los requisitos metodológicos de un {enfoque.lower()} de investigación."
        ]
        
        return justifications[numero - 1] if numero <= len(justifications) else justifications[0]