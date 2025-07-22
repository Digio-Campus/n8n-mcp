# N8N MCP Server

Un servidor MCP (Model Context Protocol) que proporciona herramientas para interactuar con la API de n8n.

## Descripción

Este proyecto implementa un servidor MCP que permite gestionar workflows de n8n a través de herramientas específicas. Incluye funcionalidades para:

- Listar workflows existentes
- Obtener detalles de un workflow específico
- Crear nuevos workflows
- Actualizar workflows existentes

## Instalación

1. Clona el repositorio:
```bash
git clone <url-del-repositorio>
cd n8n-mcp-server
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Configura las variables de entorno:
```bash
# Crea un archivo .env con:
N8N_URL=http://localhost:5678
N8N_API_KEY=tu_api_key_de_n8n
```

## Uso

Ejecuta el servidor MCP:

```bash
python main.py
```

## Herramientas Disponibles

- `list_workflows()`: Lista todos los workflows
- `get_workflow(workflow_id)`: Obtiene un workflow específico
- `create_workflow(name, nodes, connections)`: Crea un nuevo workflow
- `update_workflow(workflow_id, name, nodes, connections)`: Actualiza un workflow

## Configuración

El servidor requiere las siguientes variables de entorno:

- `N8N_URL`: URL de tu instancia de n8n (por defecto: http://localhost:5678)
- `N8N_API_KEY`: Tu clave API de n8n

## Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Añadir nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crea un Pull Request

## Licencia

[Especifica tu licencia aquí]
