# 🚗 AutoManager — Proyecto Django

Aplicación web para gestionar un catálogo de autos usando Django y Bootstrap 5.

---

## 📁 Estructura del Proyecto

```
proyecto_autos/
├── manage.py
├── proyecto_autos/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── autos/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── urls.py
    ├── views.py
    ├── migrations/
    │   ├── __init__.py
    │   └── 0001_initial.py
    └── templates/
        └── autos/
            ├── base.html
            ├── lista_autos.html
            └── agregar_auto.html
```

---

## ⚙️ Instalación y Configuración

### 1. Instalar Django
```bash
pip install django
```

### 2. Aplicar migraciones (crea la base de datos SQLite)
```bash
cd proyecto_autos
python manage.py migrate
```

### 3. (Opcional) Crear superusuario para el admin
```bash
python manage.py createsuperuser
```

### 4. Ejecutar el servidor de desarrollo
```bash
python manage.py runserver
```

### 5. Abrir en el navegador
- **Lista de autos:** http://127.0.0.1:8000/
- **Agregar auto:** http://127.0.0.1:8000/agregar/
- **Panel admin:** http://127.0.0.1:8000/admin/

---

## 🗂️ Modelo de Datos

| Campo   | Tipo        | Descripción                  |
|---------|-------------|------------------------------|
| marca   | CharField   | Marca del auto (máx. 50 car) |
| modelo  | CharField   | Modelo del auto (máx. 50 car)|
| año     | IntegerField| Año de fabricación           |
| precio  | DecimalField| Precio (10 dígitos, 2 dec.)  |

---

## 🛣️ URLs Configuradas

| URL          | Vista         | Nombre URL      |
|--------------|---------------|-----------------|
| `/`          | lista_autos   | `lista_autos`   |
| `/agregar/`  | agregar_auto  | `agregar_auto`  |
| `/admin/`    | Admin Django  | —               |
