# Verificaciones locales de la migración — SismoListo

**Tipo de evidencia:** ejecución local de pruebas y revisión estructural. NO demuestra despliegue público ni certificación de las 50 HU.

| Control | Resultado | Alcance |
|---|---|---|
| Único `public/index.html`, 20 módulos CSS, 2 JS, favicon y recursos | PASS | Análisis de rutas y estructura |
| Sintaxis JavaScript (`node --check`) | PASS | `app.js`, `acceptance.js`, `main.js` |
| Pruebas básicas Playwright (`tests/test_ui.py`) | 11 PASS | HTML/CSS/JS montados en memoria de Chromium, anchos 1440, 768, 390 y 320 |
| Pruebas específicas (`tests/test_28_scenarios.py`) | 28 PASS / 0 FAIL | Simulaciones académicas en memoria |
| Alternativas (`tests/test_alternatives.py`) | 7 PASS | Simulaciones de navegación, riesgos, pausa, etc. |
| Servidor HTTP de Python | 8 rutas esenciales HTTP 200 | Acceso a HTML, favicon, estilos, scripts e imagen |
| Chrome visitando localhost | NO COMPROBADO | Este entorno devuelve ERR_BLOCKED_BY_ADMINISTRATOR en URL localhost y dominio interceptado |
| Github Pages public/ | PENDIENTE | Requiere PR y seleccionar Settings → Pages → Source: GitHub Actions |

Las capturas anexas `captura-chromium-memoria-*` corresponden a la interfaz montada en memoria, no al sitio desplegado. No contienen una medición de accesibilidad integral.
