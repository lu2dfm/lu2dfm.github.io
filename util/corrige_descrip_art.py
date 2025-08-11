#!/var/local/claudeVENV/bin/python3
"""
Script para agregar descriptions automáticamente a posts de Hugo
Genera descriptions basadas en el título y las primeras líneas del contenido
"""

import os
import re
import yaml
from pathlib import Path

def extract_frontmatter_and_content(file_path):
    """Extrae el frontmatter YAML y el contenido del archivo markdown"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Buscar el frontmatter YAML
    frontmatter_match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if not frontmatter_match:
        return None, content
    
    frontmatter_text = frontmatter_match.group(1)
    body_content = frontmatter_match.group(2)
    
    try:
        frontmatter = yaml.safe_load(frontmatter_text)
    except yaml.YAMLError:
        return None, content
    
    return frontmatter, body_content

def generate_description(title, content, max_length=160):
    """Genera una description basada en el título y contenido"""
    
    # Limpiar el contenido de markdown
    clean_content = re.sub(r'[#*_`\[\]()]', '', content)
    clean_content = re.sub(r'\n+', ' ', clean_content)
    clean_content = clean_content.strip()
    
    # Tomar las primeras palabras significativas
    words = clean_content.split()[:25]  # Primeras 25 palabras
    description = ' '.join(words)
    
    # Si es muy corto, usar el título como base
    if len(description) < 50:
        description = f"Proyecto de radioafición: {title}. {description}"
    
    # Truncar si es muy largo
    if len(description) > max_length:
        description = description[:max_length-3] + "..."
    
    return description

def process_markdown_files(content_dir):
    """Procesa todos los archivos .md en el directorio de contenido"""
    
    content_path = Path(content_dir)
    
    if not content_path.exists():
        print(f"Error: Directorio {content_dir} no existe")
        return
    
    # Buscar archivos .md recursivamente
    md_files = list(content_path.rglob("*.md"))
    
    print(f"Encontrados {len(md_files)} archivos markdown")
    
    for file_path in md_files:
        print(f"\nProcesando: {file_path}")
        
        frontmatter, content = extract_frontmatter_and_content(file_path)
        
        if frontmatter is None:
            print(f"  ⚠️  No se pudo procesar el frontmatter")
            continue
        
        # Verificar si ya tiene description
        if 'description' in frontmatter:
            print(f"  ✅ Ya tiene description: {frontmatter['description'][:50]}...")
            continue
        
        # Generar description
        title = frontmatter.get('title', file_path.stem)
        description = generate_description(title, content)
        
        # Agregar description al frontmatter
        frontmatter['description'] = description
        
        # Reconstruir el archivo
        new_frontmatter = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True)
        new_content = f"---\n{new_frontmatter}---\n{content}"
        
        # Hacer backup
        backup_path = file_path.with_suffix('.md.backup')
        file_path.rename(backup_path)
        
        # Escribir el nuevo archivo
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"  ✅ Agregada description: {description[:50]}...")

def main():
    """Función principal"""
    print("🚀 Script para agregar descriptions a posts de Hugo")
    print("=" * 50)
    
    # Directorio de contenido (ajustar según tu estructura)
    content_dirs = ['content', 'content/es', 'content/posts']
    
    for content_dir in content_dirs:
        if os.path.exists(content_dir):
            print(f"\n📁 Procesando directorio: {content_dir}")
            process_markdown_files(content_dir)
            break
    else:
        print("❌ No se encontró directorio de contenido")
        print("Directorios buscados:", content_dirs)
        print("\nUso manual:")
        print("python script.py")
        print("Asegúrate de ejecutarlo desde la raíz de tu sitio Hugo")

if __name__ == "__main__":
    main()
