# Migración única a public/ — Challenge WebStorm

## Alcance

Se tomó como origen la versión de los archivos del repositorio `SismoListo/sismolisto-landing-page` para `main` y `develop`, cuya igualdad de los 142 blobs se consultó el 15/11/2026. El código de partida fue el archivo local de proyecto `SismoListo_28_Escenarios_Codigo_Corregido.zip` (133 archivos, con rutas y SHA de los archivos principales iguales a GitHub) más los cuatro documentos raíz y cinco logs históricos de referencia. No se modificó ningún repositorio remoto.

## Mapeo de estructura

- `index.html` → `public/index.html`
- `assets/**` → `public/assets/**`
- `css/**` → `public/assets/styles/**`
- `js/**` → `public/assets/scripts/**`
- CSS modular: 20 hojas referenciadas mediante `public/assets/styles/styles.css`.
- JavaScript modular: `app.js` y `acceptance.js` importados desde `public/assets/scripts/main.js`.
- `public/favicon.ico`: archivo de ícono existente en la preparación previa del challenge.
- `docs/`, `tests/`, control de versiones y documentación permanecen en raíz.

No existe duplicación de index/assets/css/js en raíz. Los CSS y JS originales se conservaron íntegros; únicamente cambiaron las rutas y los archivos de entrada. Los tests que montan HTML en memoria se adaptaron al nuevo origen `public/`.

## Ejecutar

```powershell
py -m http.server 8000 --directory public
```

Acceder a `http://localhost:8000` desde Chrome o Brave. Requiere abrir el repositorio desde WebStorm en la rama `feature/challenge-webstorm-public` y conservar `.git` al actualizar la carpeta.

## GitFlow

No borres ni reemplaces `.git`. En GitHub Desktop, antes de copiar archivos realiza una copia de seguridad y crea la rama `feature/challenge-webstorm-public` **desde `develop`**. Sustituye solo los archivos de trabajo, conservando `.git`. Git registrará las eliminaciones antiguas y adiciones nuevas; abre PR a `develop`.

## GitHub Pages

El despliegue histórico es `main /(root)`. Esta versión **requiere cambiar** Settings → Pages → Build and deployment → Source a **GitHub Actions**, además de integrar `.github/workflows/deploy-pages.yml` en `main`. El workflow entregará solo `public/`. Hasta ese momento no afirmar que está publicado el nuevo sitio; verificar URL y Actions tras integrar.

## Advertencia académica

Rutas, zonas y simulacros son ficticios. La migración de estructura no certifica el cumplimiento de las 50 HU ni de los 100 escenarios.
