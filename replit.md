# TesisPlan Asistente

## Overview

TesisPlan Asistente is a Flask-based web application designed to guide students through the systematic process of planning and structuring academic thesis research. The application provides a step-by-step wizard interface that helps users develop their research methodology, generate consistency matrices, and create structured thesis proposals. It serves as an intelligent assistant for academic research planning, supporting multiple thesis types from undergraduate to doctoral levels.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Template Engine**: Jinja2 templates with a modular base template system
- **CSS Framework**: Bootstrap with dark theme for responsive design
- **Icons**: Feather Icons for consistent visual elements
- **JavaScript**: Vanilla JavaScript for form validation, progress tracking, and user interaction
- **UI Pattern**: Multi-step wizard interface with progress tracking and session-based navigation

### Backend Architecture
- **Web Framework**: Flask with session-based state management
- **Session Management**: Flask-Session with filesystem storage for maintaining user progress
- **Routing Pattern**: Modular route handlers for each step of the thesis planning process
- **Data Processing**: ThesisGenerator class for generating academic content based on user inputs
- **State Management**: Session-based workflow with step validation and navigation control

### Application Flow
- **Step-based Workflow**: Linear progression through thesis planning stages
- **Session Persistence**: User data maintained across steps using Flask sessions
- **Conditional Branching**: Different paths based on user's existing research status
- **Content Generation**: Automated generation of thesis matrices and titles based on collected information

### Core Components
- **Route Handler**: Central routing system managing workflow progression
- **Thesis Generator**: Content generation engine for academic materials
- **Session Manager**: State persistence and validation system
- **Template System**: Responsive UI components with consistent styling

## External Dependencies

### Python Packages
- **Flask**: Core web framework for application structure
- **Flask-Session**: Session management for maintaining user state across requests

### Frontend Libraries
- **Bootstrap**: CSS framework loaded via CDN with dark theme customization
- **Feather Icons**: Icon library for user interface elements
- **Bootstrap JavaScript**: Interactive components and form validation

### Development Tools
- **Logging**: Python logging module for debugging and monitoring
- **Static Assets**: CSS and JavaScript files served through Flask's static file handling

### Infrastructure Requirements
- **File System Storage**: Session data persistence through filesystem-based storage
- **Environment Variables**: Configuration management for session secrets and application settings