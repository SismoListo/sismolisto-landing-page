# SismoListo — Landing Page (Challenge WebStorm / AV2)

Landing Page responsive del proyecto académico **SismoListo**, desarrollado en el curso IHC y Tecnologías Móviles de la UPC (2026-2). Su finalidad es representar actividades de preparación situacional ante sismos para **estudiantes universitarios** y **trabajadores de oficina**. Los escenarios, mapas y rutas son ficticios y **no son instrucciones validadas para una emergencia real**.

## Autores del equipo

- Aguilar Aguayo, Jeferson Renzo
- Alminagorda Capcha, Gian Franco
- Espinoza Ricaldi, Ángel
- Homola, Tomás
- Jimenez Abarca, Cristian John
- Vallejos Salazar, Dusting Jhair

## Funcionalidades académicas

Navegación y CTA, explicación del producto, elección de espacio, evaluación guiada, registro de riesgos, mapa simulado, micro-simulacros, checklist, progreso, formularios y estados de retroalimentación. Se utilizan **HTML5, CSS3 y JavaScript** sin CSS frameworks, con módulos independientes y estados de demostración en navegador.

## Estructura principal

```text
public/
  index.html
  favicon.ico
  assets/
    styles/styles.css   # Entrada a los 20 módulos CSS
    scripts/main.js     # Entrada a app.js y acceptance.js
    images/
    fonts/
    icons/
docs/                   # Auditorías y evidencias académicas
.github/workflows/      # Configuración futura de GitHub Pages para public/
tests/                  # Comprobaciones locales (ver nota de alcance)
README.md
CHANGELOG.md
VERSION.md
CONTRIBUTING.md
requirements-dev.txt
```

**No existe un `index.html` paralelo en la raíz**: el único punto de entrada de la web es `public/index.html`.

## Ejecutar localmente desde WebStorm o VS Code

Desde la raíz del repositorio:

```powershell
py -m http.server 8000 --directory public
```

Abrir `http://localhost:8000/`. La mayoría de las funciones de demostración se mantienen en el navegador; no requiere servidor de autenticación, correo electrónico ni GPS real.

Para pruebas estructurales y humo local:

```powershell
py tests/test_structure.py
py -m pip install -r requirements-dev.txt
py -m playwright install chromium
py tests/test_ui.py
```

## GitFlow y publicación

Repositorio del equipo: https://github.com/SismoListo/sismolisto-landing-page

Trabajar en una rama `feature/*` nacida de `develop` y enviar Pull Request a `develop`. **No sustituir el contenido de la rama `main` ni modificar la configuración de GitHub Pages hasta verificar el cambio de despliegue**.

La carpeta `public` se publica mediante el workflow `.github/workflows/deploy-pages.yml`, una vez seleccionado **Settings → Pages → Source: GitHub Actions** y aprobada la integración a `main`. Si GitHub Pages continúa en `Deploy from a branch: main /(root)`, no publicará correctamente esta nueva estructura.

Repositorio separado para Gherkin: https://github.com/JeferSomBlan/sismolisto-acceptance-tests

## Documentación y advertencias

- `docs/MIGRACION_WEBSTORM_PUBLIC.md`: trazabilidad de archivos movidos, validación y despliegue.
- `docs/README_AV2_ORIGINAL_ANTES_MIGRACION.md`: README anterior conservado por trazabilidad.
- `CHANGELOG.md` y `VERSION.md`: historial y versión en preparación.
- `CONTRIBUTING.md`: convenciones de ramas y commits.
- Los reportes de pruebas dentro de `docs/test-logs` son **históricos**, no acreditan automáticamente la ejecución de esta migración.
- Algunos criterios HU están representados parcialmente; no presentar las simulaciones como servicios reales ni rutas institucionales validadas.
