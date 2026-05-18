# Pre Entrega Automation Testing - SauceDemo
Proyecto de automatización web utilizando Selenium WebDriver, Pytest y Python.

## Objetivo
Automatizar casos de prueba funcionales sobre el sitio SauceDemo:
- Login exitoso
- Validación de catálogo
- Agregado de productos al carrito

## Tecnologías utilizadas
- Python
- Selenium WebDriver
- Pytest
- Pytest HTML
- WebDriver Manager
- Git/GitHub

---

## Instalación

Clonar repositorio:

```bash
git clone https://github.com/blejj/pre-entrega-automation-testing-franco-bleile.git
```

Ingresar a la carpeta del proyecto:

```bash
cd pre-entrega-automation-testing-franco-bleile
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## Ejecutar pruebas

Ejecutar todos los tests:

```bash
python -m pytest tests/test_saucedemo.py -v
```

Generar reporte HTML:

```bash
python -m pytest tests/test_saucedemo.py -v --html=reports/reporte.html
```

---

## Estructura del proyecto

```text
tests/
utils/
reports/
README.md
requirements.txt
pytest.ini
```

---

## Funcionalidades implementadas

- Login automatizado
- Validación de acceso exitoso
- Validación de productos visibles
- Obtención de nombre y precio del primer producto
- Agregado de productos al carrito
- Validación de contador del carrito
- Verificación de producto agregado
- Generación de reporte HTML
- Capturas automáticas en caso de error

---

## Evidencias

El proyecto genera:

- Reportes HTML automáticos
- Capturas de pantalla automáticas en caso de fallo

Los reportes se almacenan en:

```text
reports/
```

---